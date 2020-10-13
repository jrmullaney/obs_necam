'''
Override the default calibrate config parameters by putting them in here.
e.g.:
config.doAstrometry = False
'''

# These are the Gen3 configuration options for reference catalog name...
config.connections.photoRefCat = "ps1_pv3_3pi_20170110"
config.connections.astromRefCat = "ps1_pv3_3pi_20170110"

# ...which must for now be the same as the Gen2 reference catalog names...
# (even though we're not using Gen2).
config.photoRefObjLoader.ref_dataset_name = "ps1_pv3_3pi_20170110"
config.astromRefObjLoader.ref_dataset_name = "ps1_pv3_3pi_20170110"
 
# Don't attempt to do photo or astrometry calibration on simulated NeCam
# images.
config.doPhotoCal = False
config.doAstrometry = False