# FROM jupyter/scipy-notebook:137a295ff71b
FROM jupyter/datascience-notebook

COPY env.R env.R
COPY odc.sh odc.sh

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \ 
    libudunits2-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN ./odc.sh

USER $NB_UID
COPY .datacube.conf .datacube.conf

RUN conda install --yes \
    'nb_conda' \
    'r-units' \
    'r-rgdal' \
    'r-sf'

RUN Rscript env.R
