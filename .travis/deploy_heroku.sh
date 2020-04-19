#!/usr/bin/env bash


docker login -u $HEROKU_USER -p $HEROKU_API_KEY registry.heroku.com
docker build  -t registry.heroku.com/aristoptimiser/web -f Dockerfile .
docker push registry.heroku.com/aristoptimiser/web
heroku container:release web --app=aristoptimiser

heroku ps:scale web=1 -a aristoptimiser
pipenv run pytest -v test/test_the_deployment_of_containers.py
heroku ps:scale web=0 -a aristoptimiser