## LSST Docker Build Files

This directory contains the Dockerfile that you can use to build a docker image containing the LSST stack.

You'll likely need to change the user and group ids (UID, GID) in the Dockerfile to enable you to have the necessary read/write permissions when running the container. UID and GID should be set to the same values that you use natively on your machine. To get these numbers, open a terminal and do:
```
>> id -u
>> id -g
```

Once you've edited your Dockerfile, you need to build it using:
```
docker build --tag lsst:latest .
```
With the 41st weekly release of 2020 being the latest build that I know obs_necam works with.

Don't worry about following the warnings:
```
eups declare: Product obs_necam gen2's productDir /opt/lsst/software/stack/stack/current/Linux64/obs_necam/gen2 is not a directory
eups declare: Product obs_necam gen3's productDir /opt/lsst/software/stack/stack/current/Linux64/obs_necam/gen3 is not a directory
eups declare: Please specify a productDir for obs_necam gen3 (maybe "none")
```