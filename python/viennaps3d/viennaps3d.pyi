import viennals3d.viennals3d
from _typeshed import Incomplete
from typing import Callable, ClassVar, overload

D: int
__version__: str
version: str

class AdvectionCallback:
    domain: Domain
    def __init__(self) -> None: ...
    def applyPostAdvect(self, arg0: float) -> bool: ...
    def applyPreAdvect(self, arg0: float) -> bool: ...

class AdvectionParameters:
    checkDissipation: bool
    dissipationAlpha: float
    ignoreVoids: bool
    integrationScheme: viennals3d.viennals3d.IntegrationSchemeEnum
    timeStepRatio: float
    velocityOutput: bool
    def __init__(self) -> None: ...

class AnisotropicProcess(ProcessModel):
    @overload
    def __init__(self, materials: list[tuple[Material, float]]) -> None: ...
    @overload
    def __init__(
        self,
        direction100,
        direction010,
        rate100: float,
        rate110: float,
        rate111: float,
        rate311: float,
        materials: list[tuple[Material, float]],
    ) -> None: ...

class AtomicLayerProcess:
    def __init__(self) -> None: ...
    def apply(self) -> None: ...
    def disableRandomSeeds(self) -> None: ...
    def enableRandomSeeds(self) -> None: ...
    def setCoverageTimeStep(self, arg0: float) -> None: ...
    def setDesorptionRates(self, arg0: list[float]) -> None: ...
    def setDomain(self, *args, **kwargs): ...
    def setIntegrationScheme(
        self, arg0: viennals3d.viennals3d.IntegrationSchemeEnum
    ) -> None: ...
    def setNumCycles(self, arg0: int) -> None: ...
    def setNumberOfRaysPerPoint(self, arg0: int) -> None: ...
    def setProcessModel(self, arg0: ProcessModel) -> None: ...
    def setPulseTime(self, arg0: float) -> None: ...
    def setSourceDirection(self, arg0: rayTraceDirection) -> None: ...

class BoxDistribution(ProcessModel):
    @overload
    def __init__(
        self, halfAxes, gridDelta: float, mask: viennals3d.viennals3d.Domain
    ) -> None: ...
    @overload
    def __init__(self, halfAxes, gridDelta: float) -> None: ...

class DirectionalEtching(ProcessModel):
    @overload
    def __init__(
        self,
        direction,
        directionalVelocity: float,
        isotropicVelocity: float = ...,
        maskMaterial: Material = ...,
        calculateVisibility: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        direction,
        directionalVelocity: float,
        isotropicVelocity: float,
        maskMaterial: list[Material],
        calculateVisibility: bool = ...,
    ) -> None: ...
    @overload
    def __init__(self, rateSets: list[RateSet]) -> None: ...
    @overload
    def __init__(self, rateSet: RateSet) -> None: ...

class Domain:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, domain: Domain) -> None: ...
    @overload
    def __init__(
        self,
        gridDelta: float,
        xExtent: float,
        yExtent: float,
        boundary: viennals3d.viennals3d.BoundaryConditionEnum = ...,
    ) -> None: ...
    def applyBooleanOperation(
        self,
        arg0: viennals3d.viennals3d.Domain,
        arg1: viennals3d.viennals3d.BooleanOperationEnum,
    ) -> None: ...
    def clear(self) -> None: ...
    def deepCopy(self, arg0: Domain) -> None: ...
    def duplicateTopLevelSet(self, arg0: Material) -> None: ...
    def generateCellSet(self, arg0: float, arg1: Material, arg2: bool) -> None: ...
    def getBoundaryConditions(self, *args, **kwargs): ...
    def getBoundingBox(self, *args, **kwargs): ...
    def getCellSet(self, *args, **kwargs): ...
    def getGrid(self, *args, **kwargs): ...
    def getGridDelta(self) -> float: ...
    def getLevelSets(self) -> list[viennals3d.viennals3d.Domain]: ...
    def getMaterialMap(self, *args, **kwargs): ...
    def getSetup(self, *args, **kwargs): ...
    def insertNextLevelSet(
        self, levelset: viennals3d.viennals3d.Domain, wrapLowerLevelSet: bool = ...
    ) -> None: ...
    def insertNextLevelSetAsMaterial(
        self,
        levelSet: viennals3d.viennals3d.Domain,
        material: Material,
        wrapLowerLevelSet: bool = ...,
    ) -> None: ...
    def print(self) -> None: ...
    def removeLevelSet(self, arg0: int, arg1: bool) -> None: ...
    def removeMaterial(self, arg0: Material) -> None: ...
    def removeTopLevelSet(self) -> None: ...
    def saveHullMesh(
        self, filename: str, wrappingLayerEpsilon: float = ...
    ) -> None: ...
    def saveLevelSetMesh(self, filename: str, width: int = ...) -> None: ...
    def saveLevelSets(self, filename: str) -> None: ...
    def saveSurfaceMesh(self, filename: str, addMaterialIds: bool = ...) -> None: ...
    def saveVolumeMesh(
        self, filename: str, wrappingLayerEpsilon: float = ...
    ) -> None: ...
    def setMaterialMap(self, arg0) -> None: ...
    def setup(
        self,
        gridDelta: float,
        xExtent: float,
        yExtent: float = ...,
        boundary: viennals3d.viennals3d.BoundaryConditionEnum = ...,
    ) -> None: ...

class DomainSetup:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        gridDelta: float,
        xExtent: float,
        yExtent: float,
        boundary: viennals3d.viennals3d.BoundaryConditionEnum = ...,
    ) -> None: ...
    def boundaryCons(self, *args, **kwargs): ...
    def bounds(self, *args, **kwargs): ...
    def check(self) -> None: ...
    def grid(self, *args, **kwargs): ...
    def gridDelta(self) -> float: ...
    def halveXAxis(self) -> None: ...
    def halveYAxis(self) -> None: ...
    def hasPeriodicBoundary(self) -> bool: ...
    def isValid(self) -> bool: ...
    def print(self) -> None: ...
    def xExtent(self) -> float: ...
    def yExtent(self) -> float: ...

class FaradayCageEtching(ProcessModel):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, maskMaterials: list[Material]) -> None: ...
    @overload
    def __init__(
        self, maskMaterials: list[Material], parameters: FaradayCageParameters
    ) -> None: ...
    def getParameters(self) -> FaradayCageParameters: ...
    def setParameters(self, arg0: FaradayCageParameters) -> None: ...

class FaradayCageParameters:
    cageAngle: float
    ibeParams: IBEParameters
    def __init__(self) -> None: ...

class FluorocarbonEtching(ProcessModel):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        ionFlux: float,
        etchantFlux: float,
        polyFlux: float,
        meanIonEnergy: float = ...,
        sigmaIonEnergy: float = ...,
        ionExponent: float = ...,
        deltaP: float = ...,
        etchStopDepth: float = ...,
    ) -> None: ...
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
    def layerToLevelSet(
        self, layer: int, baseHeight: float, height: float, mask: bool = ...
    ) -> viennals3d.viennals3d.Domain: ...
    def print(self) -> None: ...
    def setBoundaryConditions(
        self, arg0: list[viennals3d.viennals3d.BoundaryConditionEnum]
    ) -> None: ...
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

class GeometryFactory:
    def __init__(self, *args, **kwargs) -> None: ...
    def makeBoxStencil(
        self, position, width: float, height: float, angle: float
    ) -> viennals3d.viennals3d.Domain: ...
    def makeCylinderStencil(
        self, position, radius: float, height: float, angle: float
    ) -> viennals3d.viennals3d.Domain: ...
    def makeMask(self, base: float, height: float) -> viennals3d.viennals3d.Domain: ...
    def makeSubstrate(self, base: float) -> viennals3d.viennals3d.Domain: ...

class HoleShape:
    __members__: ClassVar[dict] = ...  # read-only
    Full: ClassVar[HoleShape] = ...
    Half: ClassVar[HoleShape] = ...
    Quarter: ClassVar[HoleShape] = ...
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

class IBEParameters:
    exponent: float
    inflectAngle: float
    meanEnergy: float
    minAngle: float
    n_l: float
    planeWaferRate: float
    redepositionRate: float
    redepositionThreshold: float
    sigmaEnergy: float
    thresholdEnergy: float
    tiltAngle: float
    yieldFunction: Callable[[float], float]
    def __init__(self) -> None: ...

class IonBeamEtching(ProcessModel):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, maskMaterials: list[Material]) -> None: ...
    @overload
    def __init__(
        self, maskMaterials: list[Material], parameters: IBEParameters
    ) -> None: ...
    def getParameters(self) -> IBEParameters: ...
    def setParameters(self, arg0: IBEParameters) -> None: ...

class IsotropicProcess(ProcessModel):
    @overload
    def __init__(self, rate: float = ..., maskMaterial: Material = ...) -> None: ...
    @overload
    def __init__(self, rate: float, maskMaterial: list[Material]) -> None: ...

class Length:
    def __init__(self, *args, **kwargs) -> None: ...
    def convertAngstrom(self) -> float: ...
    def convertCentimeter(self) -> float: ...
    def convertMeter(self) -> float: ...
    def convertMicrometer(self) -> float: ...
    def convertMillimeter(self) -> float: ...
    def convertNanometer(self) -> float: ...
    @staticmethod
    def getInstance() -> Length: ...
    @staticmethod
    def setUnit(arg0: str) -> None: ...
    def toShortString(self) -> str: ...
    def toString(self) -> str: ...

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
    @overload
    def __init__(
        self,
        domain: Domain,
        finWidth: float,
        finHeight: float,
        finTaperAngle: float = 0.0,
        maskHeight: float = 0.0,
        maskTaperAngle: float = 0.0,
        halfFin: bool = False,
        material: Material = Material.Si,
        maskMaterial: Material = Material.Mask,
    ) -> None: ...
    @overload
    def __init__(
        self,
        domain: Domain,
        gridDelta: float,
        xExtent: float,
        yExtent: float,
        finWidth: float,
        finHeight: float,
        taperAngle: float = 0.0,
        baseHeight: float = 0.0,
        periodicBoundary: bool = False,
        makeMask: bool = False,
        material: Material = Material.Si,
    ) -> None: ...
    def apply(self) -> None: ...

class MakeHole:
    @overload
    def __init__(
        self,
        domain: Domain,
        holeRadius: float,
        holeDepth: float,
        holeTaperAngle: float = 0.0,
        maskHeight: float = 0.0,
        maskTaperAngle: float = 0.0,
        holeShape: HoleShape = HoleShape.Full,
        material: Material = Material.Si,
        maskMaterial: Material = Material.Mask,
    ) -> None: ...
    @overload
    def __init__(
        self,
        domain: Domain,
        gridDelta: float,
        xExtent: float,
        yExtent: float,
        holeRadius: float,
        holeDepth: float,
        taperingAngle: float = 0.0,
        baseHeight: float = 0.0,
        periodicBoundary: bool = False,
        makeMask: bool = False,
        material: Material = Material.Si,
        holeShape: HoleShape = HoleShape.Full,
    ) -> None: ...
    def apply(self) -> None: ...

class MakePlane:
    @overload
    def __init__(
        self,
        domain: Domain,
        gridDelta: float,
        xExtent: float,
        yExtent: float,
        height: float = 0.0,
        periodicBoundary: bool = False,
        material: Material = Material.Si,
    ) -> None: ...
    @overload
    def __init__(
        self,
        domain: Domain,
        height: float = 0.0,
        material: Material = Material.Si,
        addToExisting: bool = False,
    ) -> None: ...
    def apply(self) -> None: ...

class MakeStack:
    @overload
    def __init__(
        self,
        domain: Domain,
        numLayers: int,
        layerHeight: float,
        substrateHeight: float = 0,
        holeRadius: float = 0,
        trenchWidth: float = 0,
        maskHeight: float = 0,
        taperAngle: float = 0,
        halfStack: bool = False,
        maskMaterial: Material = Material.Mask,
    ) -> None: ...
    @overload
    def __init__(
        self,
        domain: Domain,
        gridDelta: float,
        xExtent: float,
        yExtent: float,
        numLayers: int,
        layerHeight: float,
        substrateHeight: float,
        holeRadius: float,
        trenchWidth: float,
        maskHeight: float,
        periodicBoundary: bool = False,
    ) -> None: ...
    def apply(self) -> None: ...
    def getHeight(self) -> float: ...
    def getTopLayer(self) -> int: ...

class MakeTrench:
    @overload
    def __init__(
        self,
        domain: Domain,
        trenchWidth: float,
        trenchDepth: float,
        trenchTaperAngle: float = 0.0,
        maskHeight: float = 0.0,
        maskTaperAngle: float = 0.0,
        halfTrench: bool = False,
        material: Material = Material.Si,
        maskMaterial: Material = Material.Mask,
    ) -> None: ...
    @overload
    def __init__(
        self,
        domain: Domain,
        gridDelta: float,
        xExtent: float,
        yExtent: float,
        trenchWidth: float,
        trenchDepth: float,
        taperingAngle: float = 0.0,
        baseHeight: float = 0.0,
        periodicBoundary: bool = False,
        makeMask: bool = False,
        material: Material = Material.Si,
    ) -> None: ...
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
    def getMaterialMap(self) -> viennals3d.viennals3d.MaterialMap: ...
    @staticmethod
    def getMaterialName(arg0: Material) -> str: ...
    def insertNextMaterial(self, material: Material = ...) -> None: ...
    @staticmethod
    def isMaterial(arg0: float, arg1: Material) -> bool: ...
    @staticmethod
    def mapToMaterial(arg0: float) -> Material: ...
    def size(self) -> int: ...

class MultiParticleProcess(ProcessModel):
    def __init__(self) -> None: ...
    def addIonParticle(
        self,
        sourcePower: float,
        thetaRMin: float = ...,
        thetaRMax: float = ...,
        minAngle: float = ...,
        B_sp: float = ...,
        meanEnergy: float = ...,
        sigmaEnergy: float = ...,
        thresholdEnergy: float = ...,
        inflectAngle: float = ...,
        n: float = ...,
        label: str = ...,
    ) -> None: ...
    @overload
    def addNeutralParticle(
        self, stickingProbability: float, label: str = ...
    ) -> None: ...
    @overload
    def addNeutralParticle(
        self,
        materialSticking: dict[Material, float],
        defaultStickingProbability: float = ...,
        label: str = ...,
    ) -> None: ...
    def setRateFunction(
        self, arg0: Callable[[list[float], Material], float]
    ) -> None: ...

class NormalizationType:
    __members__: ClassVar[dict] = ...  # read-only
    MAX: ClassVar[NormalizationType] = ...
    SOURCE: ClassVar[NormalizationType] = ...
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

class OxideRegrowth(ProcessModel):
    def __init__(
        self,
        nitrideEtchRate: float,
        oxideEtchRate: float,
        redepositionRate: float,
        redepositionThreshold: float,
        redepositionTimeInt: float,
        diffusionCoefficient: float,
        sinkStrength: float,
        scallopVelocity: float,
        centerVelocity: float,
        topHeight: float,
        centerWidth: float,
        stabilityFactor: float,
    ) -> None: ...

class Particle:
    def __init__(self, *args, **kwargs) -> None: ...
    def getLocalDataLabels(self) -> list[str]: ...
    def getSourceDistributionPower(self) -> float: ...
    def initNew(self, *args, **kwargs): ...
    def surfaceCollision(self, *args, **kwargs): ...
    def surfaceReflection(self, *args, **kwargs): ...

class Planarize:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, geometry: Domain, cutoffHeight: float = ...) -> None: ...
    def apply(self) -> None: ...
    def setCutoffPosition(self, arg0: float) -> None: ...
    def setDomain(self, arg0: Domain) -> None: ...

class Process:
    def __init__(self) -> None: ...
    def apply(self) -> None: ...
    def calculateFlux(self) -> viennals3d.viennals3d.Mesh: ...
    def disableAdvectionVelocityOutput(self) -> None: ...
    def disableFluxSmoothing(self) -> None: ...
    def disableRandomSeeds(self) -> None: ...
    def enableAdvectionVelocityOutput(self) -> None: ...
    def enableFluxSmoothing(self) -> None: ...
    def enableRandomSeeds(self) -> None: ...
    def getAdvectionParameters(self) -> AdvectionParameters: ...
    def getProcessDuration(self) -> float: ...
    def getRayTracingParameters(self) -> RayTracingParameters: ...
    def setAdvectionParameters(self, arg0: AdvectionParameters) -> None: ...
    def setCoverageDeltaThreshold(self, arg0: float) -> None: ...
    def setDomain(self, *args, **kwargs): ...
    def setIntegrationScheme(
        self, arg0: viennals3d.viennals3d.IntegrationSchemeEnum
    ) -> None: ...
    def setMaxCoverageInitIterations(self, arg0: int) -> None: ...
    def setNumberOfRaysPerPoint(self, arg0: int) -> None: ...
    def setProcessDuration(self, arg0: float) -> None: ...
    def setProcessModel(self, arg0: ProcessModel) -> None: ...
    def setRayTracingDiskRadius(self, arg0: float) -> None: ...
    def setRayTracingParameters(self, arg0: RayTracingParameters) -> None: ...
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
    def setVelocityField(self, *args, **kwargs): ...

class ProcessParams:
    def __init__(self) -> None: ...
    @overload
    def getScalarData(self, arg0: int) -> float: ...
    @overload
    def getScalarData(self, arg0: int) -> float: ...
    @overload
    def getScalarData(self, arg0: str) -> float: ...
    @overload
    def getScalarData(self) -> list[float]: ...
    @overload
    def getScalarData(self) -> list[float]: ...
    def getScalarDataIndex(self, arg0: str) -> int: ...
    def getScalarDataLabel(self, arg0: int) -> str: ...
    def insertNextScalar(self, arg0: float, arg1: str) -> None: ...

class RateSet:
    calculateVisibility: bool
    direction: Incomplete
    directionalVelocity: float
    isotropicVelocity: float
    maskMaterials: list[Material]
    def __init__(
        self,
        direction=...,
        directionalVelocity: float = ...,
        isotropicVelocity: float = ...,
        maskMaterials: list[Material] = ...,
        calculateVisibility: bool = ...,
    ) -> None: ...
    def print(self) -> None: ...

class RayTracingParameters:
    diskRadius: float
    ignoreFluxBoundaries: bool
    normalizationType: NormalizationType
    raysPerPoint: int
    smoothingNeighbors: int
    sourceDirection: rayTraceDirection
    useRandomSeeds: bool
    def __init__(self) -> None: ...

class SF6O2Etching(ProcessModel):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        ionFlux: float,
        etchantFlux: float,
        oxygenFlux: float,
        meanIonEnergy: float = ...,
        sigmaIonEnergy: float = ...,
        ionExponent: float = ...,
        oxySputterYield: float = ...,
        etchStopDepth: float = ...,
    ) -> None: ...
    @overload
    def __init__(self, parameters: SF6O2Parameters) -> None: ...
    def getParameters(self) -> SF6O2Parameters: ...
    def setParameters(self, arg0: SF6O2Parameters) -> None: ...

class SF6O2Parameters:
    Ions: SF6O2ParametersIons
    Mask: SF6O2ParametersMask
    Passivation: SF6O2ParametersPassivation
    Si: SF6O2ParametersSi
    beta_F: dict[int, float]
    beta_O: dict[int, float]
    etchStopDepth: float
    etchantFlux: float
    fluxIncludeSticking: bool
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
    rho: float
    def __init__(self) -> None: ...

class SF6O2ParametersPassivation:
    A_ie: float
    Eth_ie: float
    def __init__(self) -> None: ...

class SF6O2ParametersSi:
    A_ie: float
    A_sp: float
    B_ie: float
    B_sp: float
    Eth_ie: float
    Eth_sp: float
    beta_sigma: float
    k_sigma: float
    rho: float
    theta_g_ie: float
    theta_g_sp: float
    def __init__(self) -> None: ...

class SingleParticleALD(ProcessModel):
    def __init__(
        self,
        stickingProbability: float,
        numCycles: float,
        growthPerCycle: float,
        totalCycles: float,
        coverageTimeStep: float,
        evFlux: float,
        inFlux: float,
        s0: float,
        gasMFP: float,
    ) -> None: ...

class SingleParticleProcess(ProcessModel):
    @overload
    def __init__(
        self,
        rate: float = ...,
        stickingProbability: float = ...,
        sourceExponent: float = ...,
        maskMaterial: Material = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        rate: float,
        stickingProbability: float,
        sourceExponent: float,
        maskMaterials: list[Material],
    ) -> None: ...
    @overload
    def __init__(
        self,
        materialRates: dict[Material, float],
        stickingProbability: float,
        sourceExponent: float,
    ) -> None: ...

class SphereDistribution(ProcessModel):
    @overload
    def __init__(
        self, radius: float, gridDelta: float, mask: viennals3d.viennals3d.Domain
    ) -> None: ...
    @overload
    def __init__(self, radius: float, gridDelta: float) -> None: ...

class TEOSDeposition(ProcessModel):
    def __init__(
        self,
        stickingProbabilityP1: float,
        rateP1: float,
        orderP1: float,
        stickingProbabilityP2: float = ...,
        rateP2: float = ...,
        orderP2: float = ...,
    ) -> None: ...

class TEOSPECVD(ProcessModel):
    def __init__(
        self,
        stickingProbabilityRadical: float,
        depositionRateRadical: float,
        depositionRateIon: float,
        exponentIon: float,
        stickingProbabilityIon: float = ...,
        reactionOrderRadical: float = ...,
        reactionOrderIon: float = ...,
        minAngleIon: float = ...,
    ) -> None: ...

class Time:
    def __init__(self, *args, **kwargs) -> None: ...
    def convertMillisecond(self) -> float: ...
    def convertMinute(self) -> float: ...
    def convertSecond(self) -> float: ...
    @staticmethod
    def getInstance() -> Time: ...
    @staticmethod
    def setUnit(arg0: str) -> None: ...
    def toShortString(self) -> str: ...
    def toString(self) -> str: ...

class ToDiskMesh:
    @overload
    def __init__(self, domain: Domain, mesh: viennals3d.viennals3d.Mesh) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def setDomain(self, arg0: Domain) -> None: ...
    def setMesh(self, arg0: viennals3d.viennals3d.Mesh) -> None: ...

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

def setNumThreads(arg0: int) -> None: ...
