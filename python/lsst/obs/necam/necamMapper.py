from __future__ import absolute_import, division, print_function

import os

from lsst.daf.persistence import Policy
from lsst.obs.base import CameraMapper
#import lsst.afw.image.utils as afwImageUtils
#import lsst.afw.image as afwImage
#from .makeNecamRawVisitInfo import MakeNecamRawVisitInfo

class NecamMapper(CameraMapper):
    packageName = 'obs_necam'

    def __init__(self, inputPolicy=None, **kwargs):

        #Declare the policy file...
        policyFile = Policy.defaultPolicyFile(self.packageName, "NecamMapper.yaml", "policy")
        policy = Policy(policyFile)
        #...and add it to the mapper:
        super(NecamMapper, self).__init__(policy, os.path.dirname(policyFile), **kwargs)

    def _computeCcdExposureId(self, dataId):
        '''
        Every exposure needs a unique ID.
        Here, I construct a unique ID by multiplying the visit number by
        64 to accomodate that we may have up to 64 CCDs exposed for every visit.
        processCcd.py will fail with a NotImplementedError() without this.
        ''' 
        pathId = self._transformId(dataId)
        visit = pathId['visit']
        ccd = pathId['ccd']
        visit = int(visit)
        ccd = int(ccd)

        return visit*64 + ccd