# A bare-bones obs package for the LSST stack 

The [Large Synoptic Sky Survey](https://www.lsst.org "LSST Homepage") (LSST) is a next-generation astronomical survey that will repeatedly survey the entire southern sky to unprecedented depths. A major part of the project is the development of a software pipeline (known as the [LSST stack](https://github.com/lsst "LSST Github")) that will process the raw data from the raft of CCDs that form the LSST's detector.

Whilst the LSST stack is primarily being developed to process data from the LSST telescope, it has been designed in such a way that it can be used to process data from other astronomical surveys. Indeed, an adapted version of the stack is being used as the primary pipeline for Subaru's HyperSupremeCam (see [Bosch et al. 2018](https://arxiv.org/pdf/1705.06766 "arXiv:1705.06766")).

To adapt the LSST stack to process data from other astronomical surveys involves writing a set of scripts and configuration files that are collectively known as an "obs package". An obs packages contains information such as detector dimensions, input/output file locations and formats (October 2020 edit: in gen2, but not gen3), as well as a host of configuration parameters that control what the stack does. Obs packages have been written for (among others) [HyperSupremeCam](https://github.com/lsst/obs_subaru), [SDSS](https://github.com/lsst/obs_sdss), [DECam](https://github.com/lsst/obs_decam), and our own [GOTO](https://github.com/GOTO-OBS/obs_goto). However, each of these have been written with their specific detectors and surveys in mind and are perhaps not the _easiest_ place to start if writing a new obs package for your own survey. That is where we think `obs_necam` fits in.

`obs_necam` is a completely stripped down obs package. It is the absolute minimum that is needed to process a single science frame. The idea is that it will be a starting-off point for others to build-upon when developing their own obs packages. With that in mind, we have included extensive comments throughout the package to help guide others in developing their own obs packages.

In this repository, you'll find two versions of `obs_necam` - one that utilises the Generation 2 (gen2) butler, and one that uses the newer Generation 3 (gen3) butler. You'll also find a `data` directory that contains two subdirectories: `rawData/` and `processedData/`. The first contains a jupyter notebook that you can use to generate a fits image that you can process with `obs_necam`. The `processedData` subdirectory contains another subdirectory `bin` which contains two shell scripts -- one for each of the gen2 and gen3 versions -- that call LSST stack tasks to process the simulated data.

Finally, this repository contains a `docker` directory, which contains a Dockerfile that will build a docker image. Once this image has been built, navigate to `data/` and execute `runLsstDocker_w_2020_41.sh`. If everything has worked ok, you should see something like:
```
>> ./runLsstDocker_w_2020_41.sh
EUPS setup
LSSTStack>
```

## Executing the demo scripts
From within the running docker container, navigate to `/home/lsst/data`, where you'll find the `rawData/` and `processedData/` directories that are mounted from your native filesystem (plus a directory containing a couple of reference catalogues, taken from LSST's [pipelines_check](https://github.com/lsst/pipelines_check) repository, and the `runLsstDocker_w_2020_41.sh` file since the whole `data` directory is mounted):
```
LSSTStack> cd /home/lsst/data/
LSSTStack> ls
processedData  rawData	refcats  runLsstDocker_w_2020_41.sh
```
Next, navigate to `processedData` which, to start with, will only contain a single directory called `bin`:
```
LSSTStack> cd processedData/
LSSTStack> ls
bin
```
Before executing any commands to process the demo data (presuming you've used the aforementioned jupyter notebook to generate it), you need to set up the necam obs package. This is done using the ``setup`` command. You can only have either the gen2 _or_ gen3 obs package setup at any given time. To set up the gen2 package execute:
```
LSSTStack> setup obs_necam gen2
```
whereas to set up the gen3 package execute:
```
LSSTStack> setup obs_necam gen3
```
With one of the necam obs package now setup, you can execute the corresponding demo scripts. If you set up the gen2 obs package, then execute:
```
LSSTStack> ./bin/run_gen2_demo.sh
```
whereas if you instead set up the gen3 obs package, execute:
```
LSSTStack> ./bin/run_gen3_demo.sh
```

If all goes well, the gen2 demo script should finish with a few lines saying something like:
```
processCcd.charImage.repair INFO: Identified 70 cosmic rays.
processCcd.charImage.measurement INFO: Measuring 726 sources (726 parents, 0 children)
processCcd.charImage.measureApCorr INFO: Measuring aperture corrections for 2 flux fields
processCcd.charImage.measureApCorr INFO: Aperture correction for base_GaussianFlux: RMS 0.011359 from 147
processCcd.charImage.measureApCorr INFO: Aperture correction for base_PsfFlux: RMS 0.038920 from 147
processCcd.charImage.applyApCorr INFO: Applying aperture corrections to 2 instFlux fields
```
whereas the gen3 demo script should finish with a few lines saying something like:
```
calibrate.skySources INFO: Added 99 of 100 requested sky sources (99%)
calibrate.deblend INFO: Deblending 4073 sources
calibrate.deblend INFO: Deblended: of 4073 sources, 2452 were deblended, creating 20399 children, total 24472 sources
calibrate.measurement INFO: Measuring 24472 sources (4073 parents, 20399 children)
calibrate.applyApCorr INFO: Applying aperture corrections to 2 instFlux fields
calibrate INFO: Copying flags from icSourceCat to sourceCat for 715 sources
```
Don't worry if your numbers don't match the above exactly; I didn't hardcode a random number seed in the aforementioned jupyter notebook (I know, I know...), so those numbers are subject to statistical variation.


