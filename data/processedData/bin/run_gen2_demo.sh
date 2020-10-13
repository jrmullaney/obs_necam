#!/bin/bash

if [ -d DATA ]; then
    rm -rf DATA
fi

if [ ! -d DATA ]; then
    mkdir -p DATA/CALIB
    echo "lsst.obs.necam.necamMapper.NecamMapper" > DATA/_mapper
fi

ingestImages.py DATA ../rawData/*.fits --mode=copy --ignore-ingested
processCcd.py DATA --calib DATA/CALIB --rerun outPC --id ccd=1 --clobber-config