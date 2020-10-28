#!/bin/bash

# IMPORTANT: Make sure the gen3 version of obs_necam is set up before running
# this script:
# >> setup obs_necam gen3

# This should already be set, but doesn't harm to make sure:
export DYLD_LIBRARY_PATH=${LSST_LIBRARY_PATH}

# If developing your own gen3 obs_package, it helps to start with a clean
# DATA_REPO each time:
if [ -f DATA_REPO/butler.yaml ]; then
    rm -rf DATA_REPO
fi

# If DATA_REPO does not exist, create it and register your instrument.
if [ ! -f DATA_REPO/butler.yaml ]; then
    butler create DATA_REPO
    butler register-instrument DATA_REPO lsst.obs.necam.NeCam
fi

# Import the reference catalogues to the butler.
butler import DATA_REPO "${PWD}/../refcats" --export-file "${PWD}/../refcats/export.yaml" --skip-dimensions instrument,physical_filter,detector

if [ ! -d DATA_REPO/NeCam/raw ]; then
    butler ingest-raws DATA_REPO ../rawData/ --ingest-task lsst.obs.necam.ingest.NeCamRawIngestTask
    butler define-visits DATA_REPO lsst.obs.necam.NeCam --collections NeCam/raw/all
fi

pipetask run -d "exposure=1" -b DATA_REPO/butler.yaml --input NeCam/raw/all --register-dataset-types -p "${PIPE_TASKS_DIR}/pipelines/_SingleFrame.yaml" --instrument lsst.obs.necam.NeCam --output-run demo_collection