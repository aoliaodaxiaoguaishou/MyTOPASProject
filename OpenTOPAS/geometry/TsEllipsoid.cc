// ********************************************************************
// *                                                                  *
// * Copyright 2024 The TOPAS Collaboration                           *
// *                                                                  *
// * Permission is hereby granted, free of charge, to any person      *
// * obtaining a copy of this software and associated documentation   *
// * files (the "Software"), to deal in the Software without          *
// * restriction, including without limitation the rights to use,     *
// * copy, modify, merge, publish, distribute, sublicense, and/or     *
// * sell copies of the Software, and to permit persons to whom the   *
// * Software is furnished to do so, subject to the following         *
// * conditions:                                                      *
// *                                                                  *
// * The above copyright notice and this permission notice shall be   *
// * included in all copies or substantial portions of the Software.  *
// *                                                                  *
// * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  *
// * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES  *
// * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND         *
// * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT      *
// * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,     *
// * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     *
// * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR    *
// * OTHER DEALINGS IN THE SOFTWARE.                                  *
// ********************************************************************

#include "TsEllipsoid.hh"

#include "TsParameterManager.hh"
#include "TsSequenceManager.hh"

#include "G4Ellipsoid.hh"

#include "TsParameterisation.hh"

#include "G4Step.hh"
#include "G4GeometryTolerance.hh"
#include "G4SystemOfUnits.hh"
TsEllipsoid::TsEllipsoid(TsParameterManager* pM, TsExtensionManager* eM, TsMaterialManager* mM, TsGeometryManager* gM,
                         TsVGeometryComponent* parentComponent, G4VPhysicalVolume* parentVolume, G4String& name)
        : TsVGeometryComponent(pM, eM, mM, gM, parentComponent, parentVolume, name)
{
    fIsDividable = true;
    fCanCalculateSurfaceArea = true;
    fHasDifferentVolumePerDivision = true;

    fDivisionNames[0] = "Phi";
    fDivisionNames[1] = "Theta";
    fDivisionUnits[0] = "deg";
    fDivisionUnits[1] = "deg";
}

TsEllipsoid::~TsEllipsoid() {}

G4VPhysicalVolume* TsEllipsoid::Construct()
{
    BeginConstruction();

    fDx = fPm->GetDoubleParameter(GetFullParmName("Dx"), "Length");
    fDy = fPm->GetDoubleParameter(GetFullParmName("Dy"), "Length");
    fDz = fPm->GetDoubleParameter(GetFullParmName("Dz"), "Length");

    if (!fIsCopy) {
        for (G4int i = 0; i < 2; i++) {
            if (fPm->ParameterExists(GetBinParmName(i))) {
                fDivisionCounts[i] = fPm->GetIntegerParameter(GetBinParmName(i));
                if (fDivisionCounts[i] <= 0)
                    OutOfRange(GetBinParmName(i), "must be larger than zero");
            }
        }
    }

    G4Ellipsoid* solid = new G4Ellipsoid(fName, fDx, fDy, fDz);
    fEnvelopeLog = CreateLogicalVolume(solid);
    fEnvelopePhys = CreatePhysicalVolume(fEnvelopeLog);

    G4int nDivisions = fDivisionCounts[0] * fDivisionCounts[1];
    fFullWidths[0] = 360. * deg;
    fFullWidths[1] = 180. * deg;

    if (nDivisions > 1)
        SetHasDividedCylinderOrSphere();

    if (nDivisions > 1) {
        G4String divisionName = fName + "_Division";
        G4String matName = GetResolvedMaterialName();
        G4double dPhi = fFullWidths[0] / fDivisionCounts[0];
        G4double dTheta = fFullWidths[1] / fDivisionCounts[1];

        G4Ellipsoid* divSolid = new G4Ellipsoid(divisionName, fDx, fDy, fDz);
        G4LogicalVolume* divLog = CreateLogicalVolume(divisionName, matName, divSolid);
        CreatePhysicalVolume(divisionName, divLog, fEnvelopePhys, kUndefined, nDivisions, new TsParameterisation(this));
        divLog->SetVisAttributes(GetVisAttributes(""));
        fScoringVolume = divLog;
    }

    PreCalculateThetaRatios();
    if (fParentVolume)
        InstantiateChildren();

    return fEnvelopePhys;
}

TsVGeometryComponent::SurfaceType TsEllipsoid::GetSurfaceID(G4String surfaceName)
{
    G4String lower = surfaceName;
#if GEANT4_VERSION_MAJOR >= 11
    G4StrUtil::to_lower(lower);
#else
    lower.toLower();
#endif

    if (lower == "outercurvedsurface")
        return OuterCurvedSurface;

    G4cerr << "TsEllipsoid: Unknown surface name: " << surfaceName << G4endl;
    fPm->AbortSession(1);
    return None;
}

G4bool TsEllipsoid::IsOnBoundary(G4ThreeVector localpos, G4VSolid* solid, SurfaceType surfaceID)
{
    if (surfaceID != OuterCurvedSurface)
        return false;

    G4double tol = G4GeometryTolerance::GetInstance()->GetSurfaceTolerance();
    G4Ellipsoid* e = dynamic_cast<G4Ellipsoid*>(solid);

    G4double x = localpos.x(), y = localpos.y(), z = localpos.z();
    G4double a = e->GetSemiAxisMax(0), b = e->GetSemiAxisMax(1), c = e->GetSemiAxisMax(2);
    G4double val = (x * x) / (a * a) + (y * y) / (b * b) + (z * z) / (c * c);
    return std::abs(val - 1.0) < tol;
}

G4double TsEllipsoid::GetAreaOfSelectedSurface(G4VSolid* solid, SurfaceType surfaceID, G4int, G4int, G4int)
{
    if (surfaceID != OuterCurvedSurface)
        return 0.;

    G4Ellipsoid* e = dynamic_cast<G4Ellipsoid*>(solid);
    G4double a = e->GetSemiAxisMax(0); // 获取三个方向的半轴
    G4double b = e->GetSemiAxisMax(1);
    G4double c = e->GetSemiAxisMax(2);

    double p = 1.6075;
    return 4. * CLHEP::pi * std::pow((std::pow(a * b, p) + std::pow(a * c, p) + std::pow(b * c, p)) / 3., 1. / p);
}

G4int TsEllipsoid::GetIndex(G4Step* aStep)
{
    if (fDivisionCounts[0] * fDivisionCounts[1] == 1)
        return 0;

    const G4VTouchable* touchable = aStep->GetPreStepPoint()->GetTouchable();

    if (IsParameterized() && !touchable->GetVolume()->IsParameterised()) {
        fPm->GetSequenceManager()->NoteParameterizationError(
            aStep->GetTotalEnergyDeposit(), GetNameWithCopyId(), touchable->GetVolume()->GetName());
        return -1;
    }

    G4int index = touchable->GetReplicaNumber(0);
    if (index < 0 || index >= fDivisionCounts[0] * fDivisionCounts[1]) {
        fPm->GetSequenceManager()->NoteIndexError(
            aStep->GetTotalEnergyDeposit(), GetNameWithCopyId(), "", index,
            fDivisionCounts[0] * fDivisionCounts[1] - 1);
        return -1;
    }

    return index;
}

G4int TsEllipsoid::GetIndex(G4int iPhi, G4int iTheta)
{
    return iPhi * fDivisionCounts[1] + iTheta;
}

G4int TsEllipsoid::GetBin(G4int index, G4int iBin)
{
    G4int iPhi = index / fDivisionCounts[1];
    G4int iTheta = index % fDivisionCounts[1];

    if (iBin == 0) return iPhi;
    if (iBin == 1) return iTheta;
    return -1;
}

void TsEllipsoid::PreCalculateThetaRatios()
{
    G4int nTheta = fDivisionCounts[1];
    fThetaAreaRatios.resize(nTheta, 1.0 / nTheta); // 均匀划分
}

void TsEllipsoid::CreateDefaults(TsParameterManager* pM, G4String& childName, G4String&)
{
    pM->AddParameter("dc:Ge/" + childName + "/Dx", "10. mm");
    pM->AddParameter("dc:Ge/" + childName + "/Dy", "5. mm");
    pM->AddParameter("dc:Ge/" + childName + "/Dz", "3. mm");
    pM->AddParameter("dc:Ge/" + childName + "/TransX", "0. mm");
    pM->AddParameter("dc:Ge/" + childName + "/TransY", "0. mm");
    pM->AddParameter("dc:Ge/" + childName + "/TransZ", "0. mm");
    pM->AddParameter("ic:Ge/" + childName + "/PhiBins", "1");
    pM->AddParameter("ic:Ge/" + childName + "/ThetaBins", "1");
}
