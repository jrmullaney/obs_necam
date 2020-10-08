"""Metadata translation code for NeCam FITS headers"""

__all__ = ("NeCamTranslator", )

from .fits import FitsTranslator
from .helpers import altaz_from_degree_headers
from ..translator import cache_translation
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, Angle

class NeCamTranslator(FitsTranslator):
    """Metadata translator for NeCam standard headers.
    """
    name = "NeCam"
    """Name of this translation class"""

    supported_instrument = "NeCam"
    """Supports the Necam instrument."""

    _const_map = {"boresight_rotation_coord": "unknown",
                  "detector_group": None}
    """Properties that you may not know, nor can calculate"""

    """Properties that can be taken directly from header"""
    _trivial_map = {
        "exposure_time": ("EXPTIME", dict(unit=u.s)),
        "boresight_airmass": "AIRMASS",
        "boresight_rotation_angle": "ANGLE",
        "detector_serial": "DETECTOR",
        "object": "OBJECT",
        "temperature": ("OUT-TMP", dict(unit=u.K)),
        "pressure": ("OUT-PRS", dict(unit=u.hPa)),
        "relative_humidity": "OUT-HUM",
        "science_program": "PROPID",
        "observation_type": "OBSTYPE",
        }

    @classmethod
    def can_translate(cls, header, filename=None):
        """Indicate whether this translation class can translate the
        supplied header.
        Checks the INSTRUME and FILTER headers.
        Parameters
        ----------
        header : `dict`-like
            Header to convert to standardized form.
        filename : `str`, optional
            Name of file being translated.
        Returns
        -------
        can : `bool`
            `True` if the header is recognized by this class. `False`
            otherwise.
        """
        # Use INSTRUME. Because of defaulting behavior only do this
        # if we really have an INSTRUME header
        if "INSTRUME" in header:
            via_instrume = super().can_translate(header, filename=filename)
            if via_instrume:
                return via_instrume
        return True

    @cache_translation
    def to_exposure_id(self):
        return 1
    
    @cache_translation
    def to_visit_id(self):
        return self.to_exposure_id()

    @cache_translation
    def to_physical_filter(self):
        return 'Clear'

    @cache_translation 
    def to_datetime_begin(self):
        date = self._header["DATE-OBS"]
        date = [date[0:4], date[4:6], date[6:]]
        date = '-'.join(date)
        t = Time(date, format='iso', scale="utc")
        return t
    
    @cache_translation 
    def to_datetime_end(self):
        datetime_end = self.to_datetime_begin() + self.to_exposure_time()
        return datetime_end

    @cache_translation 
    def to_dark_time(self):
        return 100 * u.s

    @cache_translation
    def to_detector_exposure_id(self):
        return self.to_exposure_id() 

    @cache_translation    
    def to_tracking_radec(self):
        radec = SkyCoord(self._header["RA2000"], self._header["DEC2000"],
                         frame="icrs", unit=(u.hourangle, u.deg))
        return radec

    @cache_translation
    def to_altaz_begin(self):
        return None

    @cache_translation
    def to_instrument(self):
        return 'NeCam'
    
    @cache_translation
    def to_observation_id(self):
        return 'NeCam'

    @cache_translation
    def to_detector_name(self):
        return '1'

    @cache_translation
    def to_detector_num(self):
        return 1
