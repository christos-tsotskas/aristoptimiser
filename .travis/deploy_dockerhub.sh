#!/usr/bin/env bash
docker login --username $DOCKER_USER --password $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
TAG="latest"
else
TAG="$TRAVIS_BRANCH"
fi

docker login -u $HEROKU_USER -p $HEROKU_API_KEY registry.heroku.com
docker build  -t registry.heroku.com/aristoptimiser/web -f Dockerfile .
docker push registry.heroku.com/aristoptimiser/web
heroku container:release web --app=aristoptimiser


#echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
#docker build --no-cache -t $DOCKER_REPO:$TAG -f Dockerfile .
#docker push $DOCKER_REPO:$TAG