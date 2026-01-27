import os
import math


def write_common_config(filename, InnerRadius, OuterRadius, HalfHeight, HLX, HLY, HLZ):
    """
    通用配置部分，只需要写一次
    """
    template_common = f"""
    b:Ge/QuitIfOverlapDetected="false"

    #### GENERAL ####
    i:Ts/Seed =  545
    i:Ts/NumberOfThreads = -1
    #b:Ts/DumpParameters = "True"
    #b:Ts/DumpNonDefaultParameters = "False"
    #b:Ts/ListUnusedParameters = "True"
    #Ts/PauseBeforeQuit = "True"
    #b:Ts/ShowCPUTime = "True"

    #### GUI ####
    #s:Gr/ViewA/Type = "OpenGL"
    #i:Gr/ViewA/WindowSizeX = 1200
    #i:Gr/ViewA/WindowSizeY = 1000
    #u:Gr/ViewA/Zoom = 2.
    #Ts/UseQt = "True"
    #d:Gr/view/Theta                         = 45 deg
    #d:Gr/view/Phi                           = 30 deg
    #s:Gr/view/ColorBy                       = "ParticleType"
    #sv:Gr/view/ColorByParticleTypeNames     = 4 "e-" "alpha" "proton" "neutron"
    #sv:Gr/view/ColorByParticleTypeColors    = 4 "green" "red" "blue" "grass"
    #s:Gr/view/BackgroundColor               = "White"

    #### WORLD ####
    s:Ge/World/Type = "TsBox"
    d:Ge/World/HLX = 1.76 mm
    d:Ge/World/HLY = 1.76 mm
    d:Ge/World/HLZ = 1.76 mm
    s:Ge/World/Material = "Vacuum"
    #s:Ge/World/Color = "lightBlue"
    #b:Ge/World/Invisible = "true"

    #### MEDIUM ####
    s:Ge/Medium/Type="TsMyMedium"
    s:Ge/Medium/Material="G4_Lu"
    s:Ge/Medium/Parent="World"
    d:Ge/Medium/InnerRadius= {InnerRadius} mm # 内半径
    d:Ge/Medium/OuterRadius= {OuterRadius} mm # 外半径
    d:Ge/Medium/HalfHeight=  {HalfHeight} mm # 半高
    d:Ge/Medium/HLX= 141.5875  um
    d:Ge/Medium/HLY= 124.575  um
    d:Ge/Medium/HLZ= 2.3575  um
    s:Ge/Medium/Color = "white"
    d:Ge/Medium/transX= 0 um
    d:Ge/Medium/transY= 0 um
    d:Ge/Medium/transZ= 437.6425 um
    
    # -- Materials
    s:Ma/G4_HistoneMaterial/CloneFromMaterial   = "G4_WATER"
    d:Ma/G4_HistoneMaterial/CloneWithDensity    = 1.407 g/cm3
    s:Ma/G4_BaseMaterial/CloneFromMaterial      = "G4_WATER"
    d:Ma/G4_BaseMaterial/CloneWithDensity       = 1.0 g/cm3
    s:Ma/G4_BackboneMaterial/CloneFromMaterial  = "G4_WATER"
    d:Ma/G4_BackboneMaterial/CloneWithDensity   = 1.0 g/cm3
    s:Ma/G4_WATER_MODIFIED/CloneFromMaterial    = "G4_WATER"
    d:Ma/G4_WATER_MODIFIED/CloneWithDensity     = 1.0 g/cm3

    #### Physics and Chemistry ####
    sv:Ph/Default/Modules = 4 "g4em-livermore" "g4decay" "g4radioactivedecay" "TsEmDNAChemistry"
    d:Ph/Default/LowestElectronEnergy = 100 eV 
    d:Ph/Default/EMRangeMin = 100. eV
    d:Ph/Default/ProductionCut = 0.2 um
    d:Ph/Default/ForRegion/Nucleus/ProductionCut = 0.2 um
    s:Ph/Default/ForRegion/G4DNA/ActiveG4EmModelFromModule = "g4em-dna_opt2"#g4em-dna,g4em-dna_opt2,g4em-dna-stationary_opt2
    d:Ph/Default/CutForElectron = 0.2 um
    d:Ph/Default/ForRegion/G4DNA/CutForElectron = 0.2 um
    d:Ph/Default/ForRegion/G4DNA/LowestElectronEnergy = 0 eV
    includeFile = /home/liangkun/topas-nbio/TOPAS-nBio-latest/examples/processes/TOPASChemistry.txt
    #includeFile = /home/tdw/MyTOPAS-nBio/TOPAS-nBio/examples/geometry/nucleusModel/supportFiles/TOPASChemistry.txt
    s:Ch/ChemistryName = "TOPASChemistry"
    b:Ch/TOPASChemistry/ChemicalStageTransportActive = "True"
    i:Ph/Verbosity = 0
    d:Ch/TOPASChemistry/ChemicalStageTimeEnd = 2.5 ns
    dv:Ch/TOPASChemistry/ChemicalStageTimeStepsHighEdges = 1 999999 ps
    dv:Ch/TOPASChemistry/ChemicalStageTimeStepsResolutions = 1 2.5 ns
    b:Ch/TOPASChemistry/TestForContactReactions = "True"
    
    b:Ph/Default/Fluorescence = "True"
    b:Ph/Default/Auger = "True"
    b:Ph/Default/AugerCascade = "True"
    b:Ph/Default/DeexcitationIgnoreCut = "True"
    b:Ph/Default/PIXE = "True"
    
    Ts/ShowHistoryCountAtInterval = 1
    
    #### Radionuclide Source for Medium ####
    s:So/RadionuclideSource/Type = "Volumetric"
    s:So/RadionuclideSource/Component = "Medium"  # 如果只是放射性核素在培养基的话，这里可以指定为上面的Medium
    s:So/RadionuclideSource/ActiveMaterial = "G4_Lu"
    b:So/RadionuclideSource/RecursivelyIncludeChildren = "T"
    i:So/RadionuclideSource/NumberOfHistoriesInRun = 150000000
    i:So/RadionuclideSource/MaxNumberOfPointsToSample = 10000000
    s:So/RadionuclideSource/BeamEnergySpectrumType    = "Discrete"
    #s:So/RadionuclideSource/BeamEnergySpectrumType    = "Continuous"
    s:So/RadionuclideSource/BeamParticle = "e-"
    dv:So/RadionuclideSource/BeamEnergySpectrumValues = 36 6.16401E-03 4.74678E-02  6.04010E-02 6.08830E-02 6.20877E-02 6.95470E-02 7.12428E-02 7.16460E-02 1.01705E-01 1.02187E-01 1.03392E-01 1.10851E-01 1.12950E-01 1.25480E-01 1.25962E-01 1.27166E-01 1.34626E-01 1.36725E-01 1.42884E-01 1.84192E-01 1.97121E-01 1.97603E-01 1.98808E-01 2.06267E-01 2.08366E-01 2.38429E-01 2.38911E-01 2.40116E-01 2.47575E-01 2.49674E-01 2.55834E-01 3.10071E-01 3.10553E-01 3.11758E-01 3.19217E-01  3.21316E-01 MeV
    uv:So/RadionuclideSource/BeamEnergySpectrumWeightsUnscaled =  36 1.09753E-03 5.17072E-02 1.18801E-04 4.13544E-05 5.09951E-05 4.84520E-05 2.68020E-04 1.34486E-05 5.52802E-03 3.47404E-02 3.06777E-02 1.77125E-02 4.81564E-03 3.04142E-05 1.03191E-04 8.49289E-05 5.42269E-05 1.48186E-05 5.97023E-03 1.91324E-04 7.69803E-04 1.23382E-04 1.19152E-04 2.31783E-04 6.60486E-05 2.25367E-05 3.53928E-05 2.30467E-05 1.97518E-05 5.45466E-06 6.25701E-05 9.04148E-06 1.13696E-06 7.87446E-07 2.52035E-06 7.27062E-07
    uv:So/RadionuclideSource/BeamEnergySpectrumWeights = 6.46152 * So/RadionuclideSource/BeamEnergySpectrumWeightsUnscaled
    """

    with open(filename, 'w') as file:
        file.write(template_common)


def append_cell_config(filename, cell_number, x, y, z, nucleus_radius, nucleus_radiusX, nucleus_radiusY, nucleus_radiusZ):
    """
    动态生成每个细胞的配置，并追加到文件中
    """
    cell_template = f"""
    #### Cell {cell_number} ####
    #### MEMBRANE ####
    s:Ge/Membrane{cell_number}/Type="TsEllipsoidalShell"
    s:Ge/Membrane{cell_number}/Material="G4_Lu"
    s:Ge/Membrane{cell_number}/Parent="World"
    d:Ge/Membrane{cell_number}/OuterX= 28.3175 um
    d:Ge/Membrane{cell_number}/OuterY= 12.4575 um
    d:Ge/Membrane{cell_number}/OuterZ= 2.3575 um
    d:Ge/Membrane{cell_number}/InnerX= 28.31 um
    d:Ge/Membrane{cell_number}/InnerY= 12.45 um
    d:Ge/Membrane{cell_number}/InnerZ= 2.35 um
    s:Ge/Membrane{cell_number}/Color = "white"
    d:Ge/Membrane{cell_number}/transX= {x} um
    d:Ge/Membrane{cell_number}/transY= {y} um
    d:Ge/Membrane{cell_number}/transZ= {z} um

    #### CYTOPLASM ####
    s:Ge/Cytoplasm{cell_number}/Type="TsEllipsoidalShell"
    s:Ge/Cytoplasm{cell_number}/Material="G4_Lu"
    s:Ge/Cytoplasm{cell_number}/Parent="World"
    d:Ge/Cytoplasm{cell_number}/OuterX= 28.31 um
    d:Ge/Cytoplasm{cell_number}/OuterY= 12.45 um
    d:Ge/Cytoplasm{cell_number}/OuterZ= 2.35 um
    d:Ge/Cytoplasm{cell_number}/InnerX= 12 um
    d:Ge/Cytoplasm{cell_number}/InnerY= 8.5 um
    d:Ge/Cytoplasm{cell_number}/InnerZ= 1.9 um
    s:Ge/Cytoplasm{cell_number}/Color = "green"
    d:Ge/Cytoplasm{cell_number}/transX= {x} um
    d:Ge/Cytoplasm{cell_number}/transY= {y} um
    d:Ge/Cytoplasm{cell_number}/transZ= {z} um

     #### Nucleus ####
    s:Ge/Nucleus{cell_number}/Type = "TsNucleus"
    s:Ge/Nucleus{cell_number}/Parent = "World"
    s:Ge/Nucleus{cell_number}/Material = "G4_WATER"
    s:Ge/Nucleus{cell_number}/Color = "White"
    s:Ge/Nucleus{cell_number}/DNAModel = "Sphere"#QuarterCylinder ，HalfCylinder，Sphere
    s:Ge/Nucleus{cell_number}/NucleusType = "Ellipsoid" # Sphere:球体  Ellipsoid:椭球形
    #d:Ge/Nucleus{cell_number}/NucleusRadius = {nucleus_radiusX} um
    d:Ge/Nucleus{cell_number}/NucleusRadiusX = {nucleus_radiusX} um
    d:Ge/Nucleus{cell_number}/NucleusRadiusY = {nucleus_radiusY} um
    d:Ge/Nucleus{cell_number}/NucleusRadiusZ = {nucleus_radiusZ} um 
    d:Ge/Nucleus{cell_number}/VoxelAdd = 75.3 nm
    i:Ge/Nucleus{cell_number}/HilbertCurveLayer = 4
    i:Ge/Nucleus{cell_number}/HilbertCurve3DRepeatX = 63
    i:Ge/Nucleus{cell_number}/HilbertCurve3DRepeatY = 45
    i:Ge/Nucleus{cell_number}/HilbertCurve3DRepeatZ = 10
    s:Ge/Nucleus{cell_number}/HilbertCurveFileName = "/home/liangkun/PaperReproduction/geometry/nucleusModel/supportFiles/HilbertPoints_iteration1.dat"
    #s:Ge/Nucleus{cell_number}/HilbertCurveFileName = "/home/tdw/MyTOPAS-nBio/TOPAS-nBio/examples/geometry/nucleusModel/supportFiles/HilbertPoints_iteration1.dat"
    s:Ge/Nucleus{cell_number}/Voxel/Material = "G4_WATER"
    b:Ge/Nucleus{cell_number}/ShowDNAVoxels = "false"
    s:Ge/Nucleus{cell_number}/ChromatinFiber/Material = "G4_WATER"
    b:Ge/Nucleus{cell_number}/ShowChromatinCylinders = "false"
    s:Ge/Nucleus{cell_number}/Histone/Material = "G4_HistoneMaterial"
    b:Ge/Nucleus{cell_number}/OnlyBuildOneHistone = "false"
    b:Ge/Nucleus{cell_number}/HistoneAsScavenger = "true"
    b:Ge/Nucleus{cell_number}/AddBases = "true"
    s:Ge/Nucleus{cell_number}/Base1/Material = "G4_BaseMaterial"
    s:Ge/Nucleus{cell_number}/Base2/Material = "G4_BaseMaterial"
    b:Ge/Nucleus{cell_number}/AddBackbones = "true"
    s:Ge/Nucleus{cell_number}/Backbone1/Material = "G4_BackboneMaterial"
    s:Ge/Nucleus{cell_number}/Backbone2/Material = "G4_BackboneMaterial"
    b:Ge/Nucleus{cell_number}/AddHydrationShell = "true"
    s:Ge/Nucleus{cell_number}/HydrationShell1/Material = "G4_WATER_MODIFIED"
    s:Ge/Nucleus{cell_number}/HydrationShell2/Material = "G4_WATER_MODIFIED"
    d:Ge/Nucleus{cell_number}/transX = {x} um
    d:Ge/Nucleus{cell_number}/transY = {y} um
    d:Ge/Nucleus{cell_number}/transZ = {z} um
    
    #### Physics and Chemistry ####
    s:Ge/Nucleus{cell_number}/AssignToRegionNamed = "G4DNA"

    """

    with open(filename, 'a') as file:  # 'a' 模式表示追加写入
        file.write(cell_template)
        
        
def append_center_cell_config(filename, cell_number, x, y, z, nucleus_radius, nucleus_radiusX, nucleus_radiusY, nucleus_radiusZ):
    """
    动态生成每个细胞的配置，并追加到文件中
    """
    cell_template = f"""
    #### Cell {cell_number} ####
     #### MEMBRANE ####
    s:Ge/Membrane{cell_number}/Type="TsEllipsoidalShell"
    s:Ge/Membrane{cell_number}/Material="G4_Lu"
    s:Ge/Membrane{cell_number}/Parent="World"
    d:Ge/Membrane{cell_number}/OuterX= 28.3175 um
    d:Ge/Membrane{cell_number}/OuterY= 12.4575 um
    d:Ge/Membrane{cell_number}/OuterZ= 2.3575 um
    d:Ge/Membrane{cell_number}/InnerX= 28.31 um
    d:Ge/Membrane{cell_number}/InnerY= 12.45 um
    d:Ge/Membrane{cell_number}/InnerZ= 2.35 um
    s:Ge/Membrane{cell_number}/Color = "white"
    d:Ge/Membrane{cell_number}/transX= {x} um
    d:Ge/Membrane{cell_number}/transY= {y} um
    d:Ge/Membrane{cell_number}/transZ= {z} um

    #### CYTOPLASM ####
    s:Ge/Cytoplasm{cell_number}/Type="TsEllipsoidalShell"
    s:Ge/Cytoplasm{cell_number}/Material="G4_Lu"
    s:Ge/Cytoplasm{cell_number}/Parent="World"
    d:Ge/Cytoplasm{cell_number}/OuterX= 28.31 um
    d:Ge/Cytoplasm{cell_number}/OuterY= 12.45 um
    d:Ge/Cytoplasm{cell_number}/OuterZ= 2.35 um
    d:Ge/Cytoplasm{cell_number}/InnerX= 12 um
    d:Ge/Cytoplasm{cell_number}/InnerY= 8.5 um
    d:Ge/Cytoplasm{cell_number}/InnerZ= 1.9 um
    s:Ge/Cytoplasm{cell_number}/Color = "green"
    d:Ge/Cytoplasm{cell_number}/transX= {x} um
    d:Ge/Cytoplasm{cell_number}/transY= {y} um
    d:Ge/Cytoplasm{cell_number}/transZ= {z} um

    #### Nucleus ####
    s:Ge/Nucleus{cell_number}/Type     = "TsEllipsoid"
    s:Ge/Nucleus{cell_number}/Parent   = "World"
    s:Ge/Nucleus{cell_number}/Material = "G4_WATER"
    d:Ge/Nucleus{cell_number}/Dx  = {nucleus_radiusX} um
    d:Ge/Nucleus{cell_number}/Dy  = {nucleus_radiusY} um
    d:Ge/Nucleus{cell_number}/Dz  = {nucleus_radiusZ} um
    d:Ge/Nucleus{cell_number}/TransX   = {x} um
    d:Ge/Nucleus{cell_number}/TransY   = {y} um
    d:Ge/Nucleus{cell_number}/TransZ   = {z} um
    s:Ge/Nucleus{cell_number}/Color    = "skyblue"
    
    s:Sc/PhaseSpaceAtVacFilm/Quantity                    = "PhaseSpace"
    b:Sc/PhaseSpaceAtVacFilm/OutputToConsole             = "True"
    s:Sc/PhaseSpaceAtVacFilm/Surface                     = "Nucleus{cell_number}/OuterCurvedSurface"
    s:Sc/PhaseSpaceAtVacFilm/OutputType                  = "ASCII" # ASCII, Binary, Limited or ROOT
    s:Sc/PhaseSpaceAtVacFilm/OutputFile                  = "ASCIIOutput"
    i:Sc/PhaseSpaceAtVacFilm/OutputBufferSize            = 1000
    #s:Sc/PhaseSpaceAtVacFilm/OnlyIncludeParticlesGoing  = "In"
    b:Sc/PhaseSpaceAtVacFilm/IncludeTOPASTime            = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeTimeOfFlight         = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeRunID                = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeEventID              = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeTrackID              = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeParentID             = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeCreatorProcess       = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeVertexInfo           = "True"
    b:Sc/PhaseSpaceAtVacFilm/IncludeSeed                 = "True"
    #sv:Sc/PhaseSpaceAtVacFilm/OnlyIncludeParticlesNamed = 1 "Proton"
    #d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV
    s:Sc/PhaseSpaceAtVacFilm/IfOutputFileAlreadyExists   = "Overwrite"

    """

    with open(filename, 'a') as file:  # 'a' 模式表示追加写入
        file.write(cell_template)


def create_cells_in_box(n, HLX, HLY, HLZ, cell_radius_x, cell_radius_y, cell_radius_z, nucleus_radius, nucleus_radiusX, nucleus_radiusY, nucleus_radiusZ, InnerRadius, OuterRadius, HalfHeight):
    """
    生成 n 个细胞的配置文件，所有细胞写在一个文件中
    """
    filename = "./topas_file/topas_cells.txt"  # 输出文件

    # 写入通用的配置（World 和其他物理、化学参数）
    write_common_config(filename, InnerRadius, OuterRadius, HalfHeight, HLX, HLY, HLZ)

    # 计算可放置的细胞数量
    numCellsX = int(2 * HLX / (2 * cell_radius_x))
    numCellsY = int(2 * HLY / (2 * cell_radius_y))
    numCellsZ = int(2 * HLZ / (2 * cell_radius_z))

    cell_count = 0
    center_index= math.ceil(n / 2)

    for i in range(numCellsX):
        for j in range(numCellsY):
            for k in range(numCellsZ):
                if cell_count >= n:
                    break

                x = -HLX + cell_radius_x + i * 2 * cell_radius_x
                y = -HLY + cell_radius_y + j * 2 * cell_radius_y
                z = -HLZ + cell_radius_z + k * 2 * cell_radius_z
                
                cell_number= cell_count + 1
                # 追加写入每个细胞的参数
                if cell_number == center_index:
                	append_center_cell_config(filename, cell_count + 1, x, y, z, nucleus_radius, nucleus_radiusX, nucleus_radiusY, nucleus_radiusZ)
                	print(f"Generated **Center** cell {cell_count + 1} at position ({x}, {y}, {z})")		
                else:
                	append_cell_config(filename, cell_count + 1, x, y, z, nucleus_radius, nucleus_radiusX, nucleus_radiusY, nucleus_radiusZ)
                	print(f"Generated cell {cell_count + 1} at position ({x}, {y}, {z})")

                cell_count += 1
    print("x方向细胞个数：{}个，y方向细胞个数：{}个，z方向的细胞个数：{}个".format(numCellsX, numCellsY, numCellsZ))


# Example usage
n_cells = 50  # 需要生成的细胞数目
HLX = 141.5875 # 外部方框X方向半长
HLY = 124.575 # 外部方框Y方向半长
HLZ = 2.3575  # 外部方框Z方向半长
cell_radius_x = 28.3175 # 每个细胞 x方向的半长
cell_radius_y = 12.4575  # 每个细胞 y方向的半长
cell_radius_z = 2.3575 # 每个细胞 z方向的半长
nucleus_radius = 12  # 细胞核半径
nucleus_radiusX = 12  # 细胞核半径
nucleus_radiusY = 8.5
nucleus_radiusZ = 1.9
# 以下长度单位为mm
InnerRadius = 0  # 内半径，默认0，表示我们要的是个完整的圆柱
OuterRadius = 0.44  # 外半径，圆柱底面的半径
HalfHeight = 0.44  # 圆柱的半高，圆柱的高是这个的两倍

create_cells_in_box(n_cells, HLX, HLY, HLZ, cell_radius_x, cell_radius_y, cell_radius_z, nucleus_radius, nucleus_radiusX, nucleus_radiusY, nucleus_radiusZ, InnerRadius, OuterRadius, HalfHeight)
