#!/usr/bin/env bash
docker login --username $DOCKER_USER --password $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
TAG="latest"
else
TAG="$TRAVIS_BRANCH"
fi


echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
docker build --no-cache -t $DOCKER_REPO:$TAG -f Dockerfile .
docker push $DOCKER_REPO:$TAG