#import os
#from lsst.utils import getPackageDir

from lsst.obs.base import Instrument
from lsst.obs.base import FilterDefinition, FilterDefinitionCollection

class NeCam(Instrument):
    #policyName = "necam"
    #obsDataPackage = "obs_necam_data"
    filterDefinitions = FilterDefinitionCollection(
        FilterDefinition(
            physical_filter="NECAM-Clear",
            abstract_filter="clear",
            lambdaEff=535.5, alias={'Clear'}
            )
    )

    def __init__(self, **kwargs):

        #super().__init__(**kwargs)
        #packageDir = getPackageDir("obs_necam")
        #self.configPaths = [os.path.join(packageDir, "config"),
        #                    os.path.join(packageDir, "config", self.policyName)]
        pass

    def getCamera(self):
        #path = os.path.join(getPackageDir("obs_necam"), "camera")
        #return self._getCameraFromPath(path)
        pass
        
    def getName(cls):
        #return "NECAM"
        pass

    def getRawFormatter(self, dataId):
        # Docstring inherited from Instrument.getRawFormatter
        # Import the formatter here to prevent a circular dependency.
        #from .rawFormatter import HyperSuprimeCamRawFormatter, HyperSuprimeCamCornerRawFormatter
        #if dataId["detector"] in (100, 101, 102, 103):
        #    return HyperSuprimeCamCornerRawFormatter
        #else:
        #    return HyperSuprimeCamRawFormatter
        pass
    
    def makeDataIdTranslatorFactory(self):# -> TranslatorFactory:
        # Docstring inherited from lsst.obs.base.Instrument.
        #factory = TranslatorFactory()
        #factory.addGenericInstrumentRules(self.getName())
        # Translate Gen2 `filter` to band if it hasn't been consumed
        # yet and gen2keys includes tract.
        #factory.addRule(PhysicalFilterToBandKeyHandler(self.filterDefinitions),
        #                instrument=self.getName(), gen2keys=("filter", "tract"), consume=("filter",))
        pass
    
    def register(self, resgistry):
        pass

    