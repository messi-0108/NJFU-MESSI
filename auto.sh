#!/bin/bash

docker build -t systeminfo .
docker stop systeminfo
docker rm systeminfo
docker run -d -p 8000:8000 --name systeminfo systeminfo:latest
start http://192.168.99.100:8000/docs/