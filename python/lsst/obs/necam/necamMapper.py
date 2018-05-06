from __future__ import absolute_import, division, print_function

import re
import os


from lsst.daf.persistence import Policy
from lsst.obs.base import CameraMapper, exposureFromImage
import lsst.afw.image.utils as afwImageUtils
import lsst.afw.image as afwImage
from lsst.ip.isr import IsrTask
#from .makeNecamRawVisitInfo import MakeNecamRawVisitInfo

class NecamMapper(CameraMapper):
    packageName = 'obs_necam'
