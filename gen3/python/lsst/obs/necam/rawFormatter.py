from lsst.obs.base import FitsRawFormatterBase
#from astro_metadata_translator import NeCamTranslator
#from ._instrument import NeCam
#from .necamFilters import NECAM_FILTER_DEFINITIONS

class NeCamRawFormatter(FitsRawFormatterBase):
    """
    Gen3 Butler formatter for NeCam raw data.
    This isn't strictly needed for instrument registration or ingestion.
    """
    pass
    #translatorClass = NeCamTranslator
    #filterDefinitions = NECAM_FILTER_DEFINITIONS
    
    #def getDetector(self, id):
        #pass
        #return NeCam().getCamera()[id]