#!/bin/bash
docker run -ti \
    -p 9999:9998 \
    -v ${PWD}:/home/lsst/data/ \
    -v /Users/James/Work/LSST/obs_necam:/opt/lsst/software/stack/stack/current/Linux64/obs_necam \
    lsst:weekly
    