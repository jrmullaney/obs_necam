# Use the official LSST stack as a parent image
# obs_necam works with v24.0.0 of the LSST stack - the latest stable distro
FROM lsstsqre/centos:7-stack-lsst_distrib-v24_0_0

ARG UID=1012
ARG GID=1012
USER root
##
#The following two lines aren't necessary, but I like to have access to a basic
#text editor (emacs) and jupyter notebooks from within the container.
RUN yum -y install emacs && yum -y clean all  && rm -rf /var/cache
RUN source /opt/lsst/software/stack/loadLSST.bash && \
    conda install -c conda-forge -y jupyterlab
##
RUN groupmod -g $GID lsst
RUN usermod -g $GID -u $UID lsst
RUN chown -R lsst:lsst /home/lsst
RUN chown lsst:lsst /opt/lsst/software/stack/stack/current
RUN chown lsst:lsst /opt/lsst/software/stack/stack/current/ups_db
COPY --chown=lsst:lsst ./bashrc /home/lsst/.bashrc

USER lsst
RUN mkdir -m 700 /tmp/runtime-lsst
