#!/bin/bash
#taking input of base folder location of data

echo "Enter the Data folder base location: "
read location

#create image
docker image build -t python:0.0.1 /Users/btiwari/PycharmProjects/dwh-coding-challenge/solution

#launch the docker
docker run  -v $location:/usr/app/src/data/ python:0.0.1

