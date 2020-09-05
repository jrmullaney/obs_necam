'''
Override the default characterize config parameters by putting them in here.
e.g.:
config.doWrite = False
'''
# Turn down the minimum flux for PSF source selection because the sources 
# in the simulated image have "fluxes" of just 300 counts 
# (default limit is 12500).
config.measurePsf.starSelector['objectSize'].fluxMin = 100.0