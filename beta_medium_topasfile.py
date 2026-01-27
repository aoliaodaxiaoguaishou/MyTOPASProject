import os
import math


def write_common_config(filename, InnerRadius, OuterRadius, HalfHeight, HLX, HLY, HLZ):
    """
    通用配置部分，只需要写一次
    """
    template_common = f"""
    b:Ge/QuitIfOverlapDetected="false"

    #### GENERAL ####
    i:Ts/Seed =  656
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
    i:So/RadionuclideSource/NumberOfHistoriesInRun = 1000000000
    i:So/RadionuclideSource/MaxNumberOfPointsToSample = 10000000
    #s:So/RadionuclideSource/BeamEnergySpectrumType    = "Discrete"
    s:So/RadionuclideSource/BeamEnergySpectrumType    = "Continuous"
    s:So/RadionuclideSource/BeamParticle = "e-"
    dv:So/RadionuclideSource/BeamEnergySpectrumValues = 101 0.00000 0.00010 0.00011 0.00012 0.00013 0.00014 0.00015 0.00016 0.00018 0.00020 0.00022 0.00024 0.00026 0.00028 0.00030 0.00032 0.00036 0.00040 0.00045 0.00050 0.00055 0.00060 0.00065 0.00070 0.00075 0.00080 0.00085 0.00090 0.00100 0.00110 0.00120 0.00130 0.00140 0.00150 0.00160 0.00180 0.00200 0.00220 0.00240 0.00260 0.00280 0.00300 0.00320 0.00360 0.00400 0.00450 0.00500 0.00550 0.00600 0.00650 0.00700 0.00750 0.00800 0.00850 0.00900 0.01000 0.01100 0.01200 0.01300 0.01400 0.01500 0.01600 0.01800 0.02000 0.02200 0.02400 0.02600 0.02800 0.03000 0.03200 0.03600 0.04000 0.04500 0.05000 0.05500 0.06000 0.06500 0.07000 0.07500 0.08000 0.08500 0.09000 0.10000 0.11000 0.12000 0.13000 0.14000 0.15000 0.16000 0.18000 0.20000 0.22000 0.24000 0.26000 0.28000 0.30000 0.32000 0.36000 0.40000 0.45000 0.49780 MeV
    uv:So/RadionuclideSource/BeamEnergySpectrumWeightsUnscaled = 101 5.707E+00 5.705E+00 5.704E+00 5.704E+00 5.704E+00 5.704E+00 5.703E+00 5.703E+00 5.703E+00 5.702E+00 5.702E+00 5.701E+00 5.701E+00 5.700E+00 5.700E+00 5.699E+00 5.698E+00 5.697E+00 5.696E+00 5.694E+00 5.693E+00 5.692E+00 5.691E+00 5.689E+00 5.688E+00 5.687E+00 5.685E+00 5.684E+00 5.682E+00 5.679E+00 5.676E+00 5.674E+00 5.671E+00 5.669E+00 5.666E+00 5.661E+00 5.656E+00 5.651E+00 5.646E+00 5.641E+00 5.636E+00 5.630E+00 5.625E+00 5.615E+00 5.605E+00 5.592E+00 5.579E+00 5.566E+00 5.554E+00 5.541E+00 5.528E+00 5.515E+00 5.503E+00 5.490E+00 5.477E+00 5.452E+00 5.426E+00 5.401E+00 5.375E+00 5.357E+00 5.338E+00 5.319E+00 5.280E+00 5.240E+00 5.201E+00 5.161E+00 5.122E+00 5.082E+00 5.042E+00 5.002E+00 4.922E+00 4.841E+00 4.739E+00 4.638E+00 4.536E+00 4.434E+00 4.333E+00 4.232E+00 4.131E+00 4.031E+00 3.932E+00 3.834E+00 3.642E+00 3.456E+00 3.276E+00 3.106E+00 2.946E+00 2.797E+00 2.661E+00 2.433E+00 2.223E+00 2.009E+00 1.793E+00 1.578E+00 1.367E+00 1.161E+00 9.643E-01 6.102E-01 3.285E-01 8.584E-02 0.000E+00
    uv:So/RadionuclideSource/BeamEnergySpectrumWeights = 1.0 * So/RadionuclideSource/BeamEnergySpectrumWeightsUnscaled 
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
HalfHeight = 0.44   # 圆柱的半高，圆柱的高是这个的两倍

create_cells_in_box(n_cells, HLX, HLY, HLZ, cell_radius_x, cell_radius_y, cell_radius_z, nucleus_radius, nucleus_radiusX, nucleus_radiusY, nucleus_radiusZ, InnerRadius, OuterRadius, HalfHeight)
