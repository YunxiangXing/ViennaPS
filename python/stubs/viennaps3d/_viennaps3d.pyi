from _typeshed import Incomplete
from typing import ClassVar, List, Tuple, overload, Annotated, FixedSize
# from viennals3d import *

Air: Material
Al2O3: Material
Cu: Material
D: int
DEBUG: LogLevel
Dielectric: Material
ERROR: LogLevel
GAS: Material
GaN: Material
INFO: LogLevel
INTERMEDIATE: LogLevel
Mask: Material
Metal: Material
NEG_X: rayTraceDirection
NEG_Y: rayTraceDirection
NEG_Z: rayTraceDirection
POS_X: rayTraceDirection
POS_Y: rayTraceDirection
POS_Z: rayTraceDirection
PolySi: Material
Polymer: Material
Si: Material
Si3N4: Material
SiC: Material
SiGe: Material
SiN: Material
SiO2: Material
SiON: Material
TIMING: LogLevel
TiN: Material
Undefined: Material
W: Material
WARNING: LogLevel
__version__: str

class AdvectionCallback:
    domain: Incomplete
    def __init__(self) -> None: ...
    def applyPostAdvect(self, arg0: float) -> bool: ...
    def applyPreAdvect(self, arg0: float) -> bool: ...

class AnisotropicProcess(ProcessModel):
    @overload
    def __init__(self, materials: List[Tuple[Material, float]]) -> None: ...
    @overload
    def __init__(self, direction100, direction010, rate100: float, rate110: float, rate111: float, rate311: float, materials: List[Tuple[Material, float]]) -> None: ...

class AtomicLayerProcess:
    def __init__(self, *args, **kwargs) -> None: ...
    def apply(self) -> None: ...
    @overload
    def setFirstPrecursor(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    @overload
    def setFirstPrecursor(self, arg0, 3>) -> None: ...
    def setMaxLambda(self, arg0: float) -> None: ...
    def setMaxTimeStep(self, arg0: float) -> None: ...
    def setPrintInterval(self, arg0: float) -> None: ...
    def setPurgeParameters(self, arg0: float, arg1: float) -> None: ...
    def setReactionOrder(self, arg0: float) -> None: ...
    @overload
    def setSecondPrecursor(self, arg0: str, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    @overload
    def setSecondPrecursor(self, arg0, 3>) -> None: ...
    def setStabilityFactor(self, arg0: float) -> None: ...

class BoxDistribution(ProcessModel):
    def __init__(self, halfAxes, gridDelta: float) -> None: ...

class DenseCellSet:
    def __init__(self) -> None: ...
    @overload
    def addFillingFraction(self, arg0: int, arg1: float) -> bool: ...
    @overload
    def addFillingFraction(self, arg0: Annotated[List[float], FixedSize(3)], arg1: float) -> bool: ...
    def addFillingFractionInMaterial(self, arg: Annotated[List[float], FixedSize(3)], arg1: float, arg2: int) -> bool: ...
    def addScalarData(self, arg0: str, arg1: float) -> None: ...
    def buildNeighborhood(self, arg0: bool) -> None: ...
    def clear(self) -> None: ...
    def getAverageFillingFraction(self, arg0: Annotated[List[float], FixedSize(3)], arg1: float) -> float: ...
    def getBoundingBox(self) -> Annotated[List[Annotated[List[float], FixedSize(3)]], FixedSize(2)]: ...
    def getCellCenter(self, arg0: int) -> Annotated[List[float], FixedSize(3)]: ...
    def getCellGrid(self): ...
    def getCellSetPosition(self) -> bool: ...
    def getDepth(self) -> float: ...
    def getElement(self, arg0: int): ...
    def getElements(self): ...
    def getFillingFraction(self, arg0: Annotated[List[float], FixedSize(3)]) -> float: ...
    def getFillingFractions(self) -> List[float]: ...
    def getGridDelta(self) -> float: ...
    def getIndex(self, arg0: Annotated[List[float], FixedSize(3)]) -> int: ...
    def getNeighbors(self, arg0: int): ...
    def getNode(self, arg0: int): ...
    def getNodes(self) -> List[Annotated[List[float], FixedSize(3)]]: ...
    def getNumberOfCells(self) -> int: ...
    def getScalarData(self, arg0: str) -> List[float]: ...
    def getScalarDataLabels(self) -> List[str]: ...
    def getSurface(self): ...
    def readCellSetData(self, arg0: str) -> None: ...
    def setCellSetPosition(self, arg0: bool) -> None: ...
    def setCoverMaterial(self, arg0: Material) -> None: ...
    @overload
    def setFillingFraction(self, arg0: int, arg1: float) -> bool: ...
    @overload
    def setFillingFraction(self, arg0, arg1: float) -> bool: ...
    def setPeriodicBoundary(self, arg0: Annotated[List[bool], FixedSize(3)]) -> None: ...
    def updateMaterials(self) -> None: ...
    def updateSurface(self) -> None: ...
    def writeCellSetData(self, arg0: str) -> None: ...
    def writeVTU(self, arg0: str) -> None: ...

class DirectionalEtching(ProcessModel):
    @overload
    def __init__(self, direction, directionalVelocity: float = ..., isotropicVelocity: float = ..., maskMaterial: Material = ...) -> None: ...
    @overload
    def __init__(self, direction, directionalVelocity: float, isotropicVelocity: float, maskMaterial: List[Material]) -> None: ...

class Domain:
    def __init__(self) -> None: ...
    def applyBooleanOperation(self, arg0: lsDomain, arg1: lsBooleanOperationEnum): ...
    def clear(self) -> None: ...
    def duplicateTopLevelSet(self, arg0: Material) -> None: ...
    def generateCellSet(self, arg0: float, arg1: Material, arg2: bool) -> None: ...
    def getCellSet(self, *args, **kwargs): ...
    def getGrid(self, *args, **kwargs): ...
    def getLevelSets(self, *args, **kwargs): ...
    def getMaterialMap(self) -> MaterialMap: ...
    def insertNextLevelSet(self, *args, **kwargs): ...
    def insertNextLevelSetAsMaterial(self, *args, **kwargs): ...
    def print(self) -> None: ...
    def removeTopLevelSet(self) -> None: ...
    def saveLevelSetMesh(self, filename: str, width: int = ...) -> None: ...
    def saveLevelSets(self, arg0: str) -> None: ...
    def saveSurfaceMesh(self, filename: str, addMaterialIds: bool = ...) -> None: ...
    def saveVolumeMesh(self, filename: str) -> None: ...
    def setMaterialMap(self, arg0: MaterialMap) -> None: ...

class FluorocarbonEtching(ProcessModel):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, ionFlux: float, etchantFlux: float, polyFlux: float, meanIonEnergy: float = ..., sigmaIonEnergy: float = ..., ionExponent: float = ..., deltaP: float = ..., etchStopDepth: float = ...) -> None: ...
    @overload
    def __init__(self, parameters: FluorocarbonParameters) -> None: ...
    def getParameters(self) -> FluorocarbonParameters: ...
    def setParameters(self, arg0: FluorocarbonParameters) -> None: ...

class FluorocarbonParameters:
    Ions: FluorocarbonParametersIons
    Mask: FluorocarbonParametersMask
    Polymer: FluorocarbonParametersPolymer
    Si: FluorocarbonParametersSi
    Si3N4: FluorocarbonParametersSi3N4
    SiO2: FluorocarbonParametersSiO2
    delta_p: float
    etchStopDepth: float
    etchantFlux: float
    ionFlux: float
    polyFlux: float
    def __init__(self) -> None: ...

class FluorocarbonParametersIons:
    exponent: float
    inflectAngle: float
    meanEnergy: float
    minAngle: float
    n_l: float
    sigmaEnergy: float
    def __init__(self) -> None: ...

class FluorocarbonParametersMask:
    A_sp: float
    B_sp: float
    Eth_sp: float
    beta_e: float
    beta_p: float
    rho: float
    def __init__(self) -> None: ...

class FluorocarbonParametersPolymer:
    A_ie: float
    Eth_ie: float
    rho: float
    def __init__(self) -> None: ...

class FluorocarbonParametersSi:
    A_ie: float
    A_sp: float
    B_sp: float
    E_a: float
    Eth_ie: float
    Eth_sp: float
    K: float
    rho: float
    def __init__(self) -> None: ...

class FluorocarbonParametersSi3N4:
    A_ie: float
    A_sp: float
    B_sp: float
    E_a: float
    Eth_ie: float
    Eth_sp: float
    K: float
    rho: float
    def __init__(self) -> None: ...

class FluorocarbonParametersSiO2:
    A_ie: float
    A_sp: float
    B_sp: float
    E_a: float
    Eth_ie: float
    Eth_sp: float
    K: float
    rho: float
    def __init__(self) -> None: ...

class GDSGeometry:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, gridDelta: float) -> None: ...
    def getBounds(self, *args, **kwargs): ...
    def layerToLevelSet(self, *args, **kwargs): ...
    def print(self) -> None: ...
    def setBoundaryConditions(self, arg0) -> None: ...
    def setBoundaryPadding(self, arg0: float, arg1: float) -> None: ...
    def setGridDelta(self, arg0: float) -> None: ...

class GDSReader:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: GDSGeometry, arg1: str) -> None: ...
    def apply(self) -> None: ...
    def setFileName(self, arg0: str) -> None: ...
    def setGeometry(self, arg0: GDSGeometry) -> None: ...

class IsotropicProcess(ProcessModel):
    @overload
    def __init__(self, rate: float = ..., maskMaterial: Material = ...) -> None: ...
    @overload
    def __init__(self, rate: float, maskMaterial: List[Material]) -> None: ...

class LogLevel:
    __members__: ClassVar[dict] = ...  # read-only
    DEBUG: ClassVar[LogLevel] = ...
    ERROR: ClassVar[LogLevel] = ...
    INFO: ClassVar[LogLevel] = ...
    INTERMEDIATE: ClassVar[LogLevel] = ...
    TIMING: ClassVar[LogLevel] = ...
    WARNING: ClassVar[LogLevel] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Logger:
    def __init__(self, *args, **kwargs) -> None: ...
    def addDebug(self, arg0: str) -> Logger: ...
    def addError(self, s: str, shouldAbort: bool = ...) -> Logger: ...
    def addInfo(self, arg0: str) -> Logger: ...
    @overload
    def addTiming(self, arg0: str, arg1: float) -> Logger: ...
    @overload
    def addTiming(self, arg0: str, arg1: float, arg2: float) -> Logger: ...
    def addWarning(self, arg0: str) -> Logger: ...
    @staticmethod
    def getInstance() -> Logger: ...
    @staticmethod
    def getLogLevel() -> int: ...
    def print(self) -> None: ...
    @staticmethod
    def setLogLevel(arg0: LogLevel) -> None: ...

class MakeFin:
    def __init__(self, domain: Domain, gridDelta: float, xExtent: float, yExtent: float, finWidth: float, finHeight: float, taperAngle: float = 0.0, baseHeight: float = 0.0, periodicBoundary: bool = False, makeMask: bool = False, material: Material = Undefined) -> None: ...
    def apply(self) -> None: ...

class MakeHole:
    def __init__(self, domain: Domain, gridDelta: float, xExtent: float, yExtent: float, holeRadius: float, holeDepth: float, taperingAngle: float = 0.0, baseHeight: float = 0.0, periodicBoundary: bool = False, makeMask: bool = False, material: Material = Undefined) -> None: ...
    def apply(self) -> None: ...

class MakePlane:
    @overload
    def __init__(self, domain: Domain, gridDelta: float, xExtent: float, yExtent: float, height: float = 0.0, periodicBoundary: bool = False, material: Material = Undefined) -> None: ...
    @overload
    def __init__(self, domain: Domain, height: float = 0.0, material: Material = Undefined) -> None: ...
    def apply(self) -> None: ...

class MakeStack:
    def __init__(self, domain: Domain, gridDelta: float, xExtent: float, yExtent: float, numLayers: int, layerHeight: float, substrateHeight: float, holeRadius: float, trenchWidth: float, maskHeight: float, periodicBoundary: bool = False) -> None: ...
    def apply(self) -> None: ...
    def getHeight(self) -> float: ...
    def getTopLayer(self) -> int: ...

class MakeTrench:
    def __init__(self, domain: Domain, gridDelta: float, xExtent: float, yExtent: float, trenchWidth: float, trenchDepth: float, taperingAngle: float = 0.0, baseHeight: float = 0.0, periodicBoundary: bool = False, makeMask: bool = False, material: Material = Undefined) -> None: ...
    def apply(self) -> None: ...

class Material:
    __members__: ClassVar[dict] = ...  # read-only
    Air: ClassVar[Material] = ...
    Al2O3: ClassVar[Material] = ...
    Cu: ClassVar[Material] = ...
    Dielectric: ClassVar[Material] = ...
    GAS: ClassVar[Material] = ...
    GaN: ClassVar[Material] = ...
    Mask: ClassVar[Material] = ...
    Metal: ClassVar[Material] = ...
    PolySi: ClassVar[Material] = ...
    Polymer: ClassVar[Material] = ...
    Si: ClassVar[Material] = ...
    Si3N4: ClassVar[Material] = ...
    SiC: ClassVar[Material] = ...
    SiGe: ClassVar[Material] = ...
    SiN: ClassVar[Material] = ...
    SiO2: ClassVar[Material] = ...
    SiON: ClassVar[Material] = ...
    TiN: ClassVar[Material] = ...
    Undefined: ClassVar[Material] = ...
    W: ClassVar[Material] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class MaterialMap:
    def __init__(self) -> None: ...
    def getMaterialAtIdx(self, arg0: int) -> Material: ...
    def getMaterialMap(self) -> lsMaterialMap: ...
    def insertNextMaterial(self, material: Material = ...) -> None: ...
    @staticmethod
    def isMaterial(arg0: float, arg1: Material) -> bool: ...
    @staticmethod
    def mapToMaterial(arg0: float) -> Material: ...
    def size(self) -> int: ...

class MeanFreePath:
    def __init__(self) -> None: ...
    def apply(self) -> None: ...
    def disableSmoothing(self) -> None: ...
    def enableSmoothing(self) -> None: ...
    def setBulkLambda(self, arg0: float) -> None: ...
    def setDomain(self, arg0: Domain) -> None: ...
    def setMaterial(self, arg0: Material) -> None: ...
    def setNumRaysPerCell(self, arg0: float) -> None: ...
    def setReflectionLimit(self, arg0: int) -> None: ...
    def setRngSeed(self, arg0: int) -> None: ...

class OxideRegrowth(ProcessModel):
    def __init__(self, nitrideEtchRate: float, oxideEtchRate: float, redepositionRate: float, redepositionThreshold: float, redepositionTimeInt: float, diffusionCoefficient: float, sinkStrength: float, scallopVelocity: float, centerVelocity: float, topHeight: float, centerWidth: float, stabilityFactor: float) -> None: ...

class Particle:
    def __init__(self, *args, **kwargs) -> None: ...
    def getLocalDataLabels(self) -> List[str]: ...
    def getSourceDistributionPower(self) -> float: ...
    def initNew(self, *args, **kwargs): ...
    def surfaceCollision(self, *args, **kwargs): ...
    def surfaceReflection(self, *args, **kwargs): ...

class Planarize:
    def __init__(self, geometry: Domain, cutoffHeight: float = 0.0) -> None: ...
    def apply(self) -> None: ...

class PlasmaDamage(ProcessModel):
    def __init__(self, ionEnergy: float = ..., meanFreePath: float = ..., maskMaterial: Material = ...) -> None: ...

class Precursor:
    adsorptionRate: float
    desorptionRate: float
    duration: float
    inFlux: float
    meanThermalVelocity: float
    name: str
    def __init__(self) -> None: ...

class Process:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, domain: Domain) -> None: ...
    @overload
    def __init__(self, domain: Domain, processModel: ProcessModel, duration: float) -> None: ...
    def setPrintTimeInterval (self, arg0: float): ...
    def apply(self) -> None: ...
    def calculateFlux(self): ...
    def disableFluxSmoothing(self) -> None: ...
    def enableFluxSmoothing(self) -> None: ...
    def getProcessDuration(self) -> float: ...
    def setDomain(self, arg0: Domain): ...
    def setIntegrationScheme(self, arg0: lsIntegrationSchemeEnum) -> None: ...
    def setMaxCoverageInitIterations(self, arg0: int) -> None: ...
    def setNumberOfRaysPerPoint(self, arg0: int) -> None: ...
    def setProcessDuration(self, arg0: float) -> None: ...
    def setProcessModel(self, arg0: ProcessModel) -> None: ...
    def setSourceDirection(self, arg0: rayTraceDirection) -> None: ...
    def setTimeStepRatio(self, arg0: float) -> None: ...

class ProcessModel:
    def __init__(self) -> None: ...
    def getAdvectionCallback(self, *args, **kwargs): ...
    def getGeometricModel(self, *args, **kwargs): ...
    def getParticleLogSize(self, arg0: int) -> int: ...
    def getParticleTypes(self, *args, **kwargs): ...
    def getPrimaryDirection(self, *args, **kwargs): ...
    def getProcessName(self) -> str | None: ...
    def getSurfaceModel(self, *args, **kwargs): ...
    def getVelocityField(self, *args, **kwargs): ...
    def insertNextParticleType(self, arg0) -> None: ...
    def setAdvectionCallback(self, *args, **kwargs): ...
    def setGeometricModel(self, *args, **kwargs): ...
    def setPrimaryDirection(self, arg0) -> None: ...
    def setProcessName(self, arg0: str) -> None: ...
    def setSurfaceModel(self, arg0) -> None: ...
    def setVelocityField(self, arg0) -> None: ...

class ProcessParams:
    def __init__(self) -> None: ...
    @overload
    def getScalarData(self, arg0: int) -> float: ...
    @overload
    def getScalarData(self, arg0: int) -> float: ...
    @overload
    def getScalarData(self, arg0: str) -> float: ...
    @overload
    def getScalarData(self) -> List[float]: ...
    @overload
    def getScalarData(self) -> List[float]: ...
    def getScalarDataIndex(self, arg0: str) -> int: ...
    def getScalarDataLabel(self, arg0: int) -> str: ...
    def insertNextScalar(self, arg0: float, arg1: str) -> None: ...

class SF6O2Etching(ProcessModel):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, ionFlux: float, etchantFlux: float, oxygenFlux: float, meanIonEnergy: float = ..., sigmaIonEnergy: float = ..., ionExponent: float = ..., oxySputterYield: float = ..., etchStopDepth: float = ...) -> None: ...
    @overload
    def __init__(self, parameters: SF6O2Parameters) -> None: ...
    def getParameters(self) -> SF6O2Parameters: ...
    def setParameters(self, arg0: SF6O2Parameters) -> None: ...

class SF6O2Parameters:
    Ions: SF6O2ParametersIons
    Mask: SF6O2ParametersMask
    Polymer: SF6O2ParametersPassivation
    Si: SF6O2ParametersSi
    beta_F: float
    beta_O: float
    etchStopDepth: float
    etchantFlux: float
    ionFlux: float
    oxygenFlux: float
    def __init__(self) -> None: ...

class SF6O2ParametersIons:
    exponent: float
    inflectAngle: float
    meanEnergy: float
    minAngle: float
    n_l: float
    sigmaEnergy: float
    def __init__(self) -> None: ...

class SF6O2ParametersMask:
    A_sp: float
    B_sp: float
    Eth_sp: float
    beta_F: float
    beta_O: float
    rho: float
    def __init__(self) -> None: ...

class SF6O2ParametersPassivation:
    A_ie: float
    Eth_ie: float
    def __init__(self) -> None: ...

class SF6O2ParametersSi:
    A_ie: float
    A_sp: float
    B_sp: float
    Eth_ie: float
    Eth_sp: float
    beta_sigma: float
    k_sigma: float
    rho: float
    def __init__(self) -> None: ...

class SegmentCells:
    @overload
    def __init__(self, arg0: DenseCellSet) -> None: ...
    @overload
    def __init__(self, cellSet: DenseCellSet, cellTypeString: str = ..., bulkMaterial: Material = ...) -> None: ...
    def apply(self) -> None: ...
    def setBulkMaterial(self, arg0: Material) -> None: ...
    def setCellSet(self, arg0: DenseCellSet) -> None: ...
    def setCellTypeString(self, arg0: str) -> None: ...

class SingleParticleProcess(ProcessModel):
    @overload
    def __init__(self, rate: float = 1.0, stickingProbability: float = 1.0, sourceExponent: float = 1.0, maskMaterial: Material = Undefined) -> None: ...
    @overload
    def __init__(self, rate: float, stickingProbability: float, sourceExponent: float, maskMaterials: List[Material]) -> None: ...

class SphereDistribution(ProcessModel):
    def __init__(self, radius: float, gridDelta: float) -> None: ...

class TEOSDeposition(ProcessModel):
    def __init__(self, stickingProbabilityP1: float, rateP1: float, orderP1: float, stickingProbabilityP2: float = ..., rateP2: float = ..., orderP2: float = ...) -> None: ...

class Timer:
    def __init__(self) -> None: ...
    def finish(self) -> None: ...
    def reset(self) -> None: ...
    def start(self) -> None: ...
    @property
    def currentDuration(self) -> int: ...
    @property
    def totalDuration(self) -> int: ...

class ToDiskMesh:
    @overload
    def __init__(self, domain: Domain, mesh) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def setDomain(self, arg0: Domain) -> None: ...
    def setMesh(self, arg0) -> None: ...

class WriteVisualizationMesh:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, domain: Domain, fileName: str) -> None: ...
    def apply(self) -> None: ...
    def setDomain(self, arg0: Domain) -> None: ...
    def setFileName(self, arg0: str) -> None: ...

class rayTraceDirection:
    __members__: ClassVar[dict] = ...  # read-only
    NEG_X: ClassVar[rayTraceDirection] = ...
    NEG_Y: ClassVar[rayTraceDirection] = ...
    NEG_Z: ClassVar[rayTraceDirection] = ...
    POS_X: ClassVar[rayTraceDirection] = ...
    POS_Y: ClassVar[rayTraceDirection] = ...
    POS_Z: ClassVar[rayTraceDirection] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def rayReflectionConedCosine(*args, **kwargs): ...
def rayReflectionDiffuse(*args, **kwargs): ...
def rayReflectionSpecular(*args, **kwargs): ...
def setNumThreads(arg0: int) -> None: ...
