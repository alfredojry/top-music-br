#!/bin/bash
yum update -y
yum install -y docker
service docker start
usermod -a -G docker ec2-user
docker pull alfredojry/top-music-br:v1
docker run -d -p 80:8000 alfredojry/top-music-br:v1
