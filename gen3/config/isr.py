'''
Override the default characterise config parameters by putting them in here.
e.g.:
config.doWrite = False
'''
# doWrite needs to be set to True as charImage and calibrate use the postISR 
# images.
config.doWrite = True

config.doOverscan = False
config.doDefect = False
config.doAssembleIsrExposures = False
config.doBias = False
config.doDark = False
config.doFlat = False
config.doSaturationInterpolation = False