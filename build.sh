#!/bin/bash

set -e

# docker network create BDC-JUPYTER-NETWORK

docker-compose rm -f && docker-compose build && docker-compose up -d
