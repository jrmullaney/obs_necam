# A bare-bones obs package for the LSST stack 

The [Large Synoptic Sky Survey](https://www.lsst.org "LSST Homepage") (LSST) is a next-generation astronomical survey that will repeatedly survey the entire southern sky to unprecedented depths. A major part of the project is the development of a software pipeline (known as the [LSST stack](https://github.com/lsst "LSST Github")) that will process the raw data from the raft of CCDs that form the LSST's detector.

Whilst the LSST stack is primarily being developed to process data from the LSST telescope, it has been designed in such a way that it can be used to process data from other astronomical surveys. Indeed, an adapted version of the stack is being used as the primary pipeline for Subaru's HyperSupremeCam (see [Bosch et al. 2018](https://arxiv.org/pdf/1705.06766 "arXiv:1705.06766")).

To adapt the LSST stack to process data from other astronomical surveys involves writing a set of scripts and configuration files that are collectively known as an "obs package". An obs packages contains information such as detector dimensions, input/output file locations and formats, as well as a host of configuration parameters that control what the stack does. Obs packages have been written for (among others) [HyperSupremeCam](https://github.com/lsst/obs_subaru), [SDSS](https://github.com/lsst/obs_sdss), [DECam](https://github.com/lsst/obs_decam), and our own [GOTO](https://github.com/GOTO-OBS/obs_goto). However, each of these have been written with their specific detectors and surveys in mind and are perhaps not the _easiest_ place to start if writing a new obs package for your own survey. That is where we think `obs_necam` fits in.

`obs_necam` is a completely stripped down obs package. It is the abosolute minimum that is needed to process a single frame from your survey. The idea is that it will be a starting-off point for others to build-upon when developing their own obs packages. With that in mind, we have included extensive comments throughout the package to help guide others in developing their own obs packages.

## Instructions for use






