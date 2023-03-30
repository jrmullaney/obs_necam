#!/bin/bash
docker run -ti \
    -v ${PWD}:/home/lsst/data/ \
    -v /local/ph1jxm/Lsst/obs_necam:/opt/lsst/software/stack/stack/current/Linux64/obs_necam \
    lsst:latest
