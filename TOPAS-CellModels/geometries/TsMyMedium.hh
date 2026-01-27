// TsMyMedium.hh

#ifndef TSMYMEDIUM_HH
#define TSMYMEDIUM_HH

#include "TsVGeometryComponent.hh"
#include "G4ThreeVector.hh"
#include "G4LogicalVolume.hh"
#include "G4VSolid.hh"

class TsMyMedium : public TsVGeometryComponent {
public:
    TsMyMedium(TsParameterManager* pM, TsExtensionManager* eM, TsMaterialManager* mM, TsGeometryManager* gM,
				  TsVGeometryComponent* parentComponent, G4VPhysicalVolume* parentVolume, G4String& name);
    virtual ~TsMyMedium() {}

    virtual G4VPhysicalVolume* Construct();

protected:
    G4double fInnerRadius;
    G4double fOuterRadius;
    G4double fHalfHeight;
    G4double fHLX;
    G4double fHLY;
    G4double fHLZ;
};

#endif

