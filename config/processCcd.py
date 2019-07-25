import os.path
from lsst.utils import getPackageDir

configDir = os.path.join(getPackageDir("obs_necam"), "config")

#ISR:
config.isr.load(os.path.join(configDir, "isr.py"))

#Load Calibrate configurations
config.doCalibrate = False
config.calibrate.load(os.path.join(configDir, "calibrate.py"))