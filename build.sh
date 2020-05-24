#!/bin/bash

set -e
docker-compose rm -f && docker-compose build && docker-compose up -d
