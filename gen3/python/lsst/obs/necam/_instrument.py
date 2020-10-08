#import os
#from lsst.utils import getPackageDir
from lsst.daf.butler.core.utils import getFullTypeName
from lsst.obs.base import Instrument
from .necamFilters import NECAM_FILTER_DEFINITIONS

class NeCam(Instrument):
    #policyName = "NeCam"
    #obsDataPackage = "obs_necam_data"
    filterDefinitions = NECAM_FILTER_DEFINITIONS

    def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        #packageDir = getPackageDir("obs_necam")
        #self.configPaths = [os.path.join(packageDir, "config"),
        #                    os.path.join(packageDir, "config", self.policyName)]
        pass

    def getCamera(self):
        '''
        Needed to register instrument
        '''
        pass

    @classmethod
    def getName(cls):
        '''
        Needed to register instrument and must return the instrument name.
        '''
        return "NeCam"

    def getRawFormatter(self, dataId):
        '''
        Needed to register instrument
        '''
        pass

    def makeDataIdTranslatorFactory(self):
        '''
        Needed to register instrument
        '''
        pass
    
    def register(self, registry):
        '''
        This populates the database with instrument and detector-specific information, and is implemented with:
        butler register-instrument DATA_REPO lsst.obs.necam.NeCam
        '''
        #Register the instrument:
        obsMax = 2**31
        registry.insertDimensionData(
            "instrument",
            {
                "name": self.getName(),
                "detector_max": 1,
                "visit_max": obsMax,
                "exposure_max": obsMax,
                "class_name": getFullTypeName(self)
            }   
            )
        
        #Register the detector(s):
        registry.insertDimensionData(
                "detector",
                {
                    "instrument": self.getName(),
                    "id":1,
                    "full_name": '1',
                    "name_in_raft": '1',
                    "raft": None,
                    "purpose": None
                }
                )

        #Registers the filter(s):
        self._registerFilters(registry)
    