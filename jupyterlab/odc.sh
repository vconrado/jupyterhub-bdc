#!/bin/bash

set -e
conda create -n odc -c conda-forge python=3.6 datacube pre_commit psycopg2 ipykernel
source activate odc

mkdir ~/Devel && cd ~/Devel && git clone https://github.com/opendatacube/datacube-core.git

conda install -y gdal geopandas matplotlib ipyleaflet
jupyter nbextension enable --py --sys-prefix ipyleaflet

cd datacube-core
pip install --upgrade -e .

pre-commit install
