# Use the official LSST stack as a parent image
# The 43rd weekly build of 2020 is the latest obs_necam has been tested on.
FROM lsstsqre/centos:7-stack-lsst_distrib-v24_0_0

ARG UID=1012
ARG GID=1012
USER root
RUN yum -y install emacs && yum -y clean all  && rm -rf /var/cache
RUN groupmod -g $GID lsst
RUN usermod -g $GID -u $UID lsst
RUN chown -R lsst:lsst /home/lsst
RUN chown lsst:lsst /opt/lsst/software/stack/stack/current
RUN chown lsst:lsst /opt/lsst/software/stack/stack/current/ups_db
COPY --chown=lsst:lsst ./bashrc /home/lsst/.bashrc

USER lsst
RUN mkdir -m 700 /tmp/runtime-lsst
