import os
from lsst.utils import getPackageDir
from lsst.daf.butler.core.utils import getFullTypeName
from lsst.obs.base import Instrument, yamlCamera
from .necamFilters import NECAM_FILTER_DEFINITIONS
from lsst.afw.cameraGeom import makeCameraFromPath, CameraConfig
# Comment-out the following line if you put .translators/necam.py in the 
# astro_metadata_translator repository:
from .translators import NeCamTranslator

class NeCam(Instrument):
    
    # Filter definitions are needed when registering the filters.
    filterDefinitions = NECAM_FILTER_DEFINITIONS

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Tell it where the config file are:
        packageDir = getPackageDir("obs_necam")
        self.configPaths = [os.path.join(packageDir, "config")]
        
    def getCamera(self):
        '''
        This grabs the camera information in the camera/n1_necam.yaml file.
        '''
        path = os.path.join(
            getPackageDir("obs_necam"), 
            "camera", 
            'n1_necam.yaml')
        return yamlCamera.makeCamera(path)

    @classmethod
    def getName(cls):
        '''
        This must return the instrument name.
        '''
        return "NeCam"

    def getRawFormatter(self, dataId):
        from .rawFormatter import NeCamRawFormatter
        return NeCamRawFormatter

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
        obsMax = 2**5 #NeCam only ever took 32 images!
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
                    "full_name": '01',
                    "name_in_raft": None,
                    "raft": None,
                    "purpose": None
                }
                )

        #Registers the filter(s):
        self._registerFilters(registry)
    