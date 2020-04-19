# aristoptimiser
optimisation algorithm

Solver for an optimisation problem

# how to contribute

## CI/CD

github -> circleCI -> sonarcloud -> docker -> heroku

# todo

- build containers and registry
- deploy on heroku (https://docs.travis-ci.com/user/deployment/heroku/)
- log better/more structured
- add fixtures for the web-based tests
- encrypt communication
- pass settings about deployed server to the test case
- capture the uris from heroku and pass to the apps
- populate setup
- use better pytest
- better settings on travis per branch ( https://docs.travis-ci.com/user/languages/python/ )
- add all other classes from (https://dspace.lib.cranfield.ac.uk/bitstream/handle/1826/12354/Tsotskas_C_2016.pdf?sequence=1&isAllowed=y)

- on circleci store test coverage results as an artifact
- link coverage to https://codecov.io/ with instructions from https://github.com/codecov/example-python and https://codecov.io/gh/christos-tsotskas/aristoptimiser
- add flake8 in the CI pipeline
- add some badges
- https://docs.docker.com/engine/reference/commandline/login/#credentials-store
- more configuration for the webserver ( such as https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04)

# R&D
- possibly use Nameko for microservices (https://www.toptal.com/python/introduction-python-microservices-nameko)
- better client than ( https://docs.python.org/3/library/http.client.html)
- see more from travis ( https://docs.travis-ci.com/user/tutorial/)
- additional rules (https://flask.palletsprojects.com/en/1.1.x/api/)
- check https://www.fullstackpython.com/api-creation.html
- check Zappa, serverless python (from zappa.io)

# Utilities

## connect to container via ssh
### approach 1
```bash
docker run -d -p 22 mysnapshot /usr/sbin/sshd -D
```

### approach2
run
```bash
docker exec -it busy_williamson bash
```

and then connect with
```bash
docker exec -it busy_williamson bash
```

### approach3

```bash
docker run -it -p 5000:5000 ctsotskas/aristohub:latest bash
```

carry on from http://bobcares.com/blog/docker-port-expose/

## executing containers

run docker with PORT as environment variable (this is needed for deploying on Heroku)
```bash
docker run -d -p 4000:4000 -e PORT=4000 registry.heroku.com/aristoptimiser/web
```

# Instructions to build the service

build with
```bash
docker build --no-cache -t ctsotskas/aristohub:latest -f Dockerfile .
```

run with
```bash
docker run -rm -d -p 5000:5000 ctsotskas/aristohub:latest
```


push
```bash
echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
docker build --no-cache -t ctsotskas/aristohub:latest -f Dockerfile .
docker push ctsotskas/aristohub:latest

```

tag (for Heroku) & push to Heroku

HEROKU_APP_NAME: <APP_NAME>
HEROKU_REGISTRY_IMAGE: registry.heroku.com/${HEROKU_APP_NAME}/web

```bash
docker login -u $HEROKU_USER -p $HEROKU_API_KEY registry.heroku.com
docker build  -t registry.heroku.com/aristoptimiser/web -f Dockerfile .
docker push registry.heroku.com/aristoptimiser/web
heroku container:release web --app=aristoptimiser

```




# CI

## appveyor

instructions: https://www.appveyor.com/docs/appveyor-yml/
https://www.appveyor.com/docs/build-configuration/


# other guide
https://sweetcode.io/flask-app-github-travis-heroku/

# operations

## Heroku

run (after pushing)
```bash
heroku container:release -a aristoptimiser web
```

check from broswer https://aristoptimiser.herokuapp.com/

stop all activity
```bash
heroku ps:scale web=0 -a aristoptimiser
```

### references
https://devcenter.heroku.com/categories/deploying-with-docker
https://devcenter.heroku.com/articles/build-docker-images-heroku-yml
https://devcenter.heroku.com/articles/dynos
https://devcenter.heroku.com/articles/container-registry-and-runtime
https://www.merixstudio.com/blog/deploying-docker-heroku-tutorial/
https://devcenter.heroku.com/articles/runtime-principles

# other
https://testdriven.io/blog/deploying-flask-to-heroku-with-docker-and-gitlab/
https://stackabuse.com/deploying-a-flask-application-to-heroku/?fbclid=IwAR1UjkOizjJOQU_X7KwfZ1Hn7SMWeSnAJN3SrQMprwaMIhxDlKZKiC5nQfI
https://stackoverflow.com/questions/60013369/deploying-flask-with-celery-app-on-heroku-using-heroku-yml
https://sweetcode.io/flask-app-github-travis-heroku/