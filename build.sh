#!/bin/bash
docker build --no-cache -t langchain-projects-base -f Dockerfile.base .
docker-compose build --no-cache