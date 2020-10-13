#Use the official LSST stack as a parent image
FROM lsstsqre/centos:7-stack-lsst_distrib-w_2020_41

ARG UID=501
ARG GID=20
USER root
RUN usermod -g $GID -u $UID lsst
RUN chown -R lsst:lsst /home/lsst
RUN chown lsst:lsst /opt/lsst/software/stack/stack/current
RUN chown lsst:lsst /opt/lsst/software/stack/stack/current/ups_db
COPY --chown=lsst:lsst ./bashrc /home/lsst/.bashrc

USER lsst
RUN mkdir -m 700 /tmp/runtime-lsst