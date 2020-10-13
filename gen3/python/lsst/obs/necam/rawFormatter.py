from lsst.obs.base import FitsRawFormatterBase
from ._instrument import NeCam
from .necamFilters import NECAM_FILTER_DEFINITIONS
# Comment-out the following line if you put .translators/necam.py in the 
# astro_metadata_translator repository: 
from .translators import NeCamTranslator
# ...and uncomment the following:
# from astro_metadata_translator import NeCamTranslator

class NeCamRawFormatter(FitsRawFormatterBase):
    """
    Gen3 Butler formatter for NeCam raw data.
    """
    translatorClass = NeCamTranslator
    filterDefinitions = NECAM_FILTER_DEFINITIONS

    def getDetector(self, id):
        return NeCam().getCamera()[id]