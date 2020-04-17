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

# R&D
- possibly use Nameko for microservices (https://www.toptal.com/python/introduction-python-microservices-nameko)
- better client than ( https://docs.python.org/3/library/http.client.html)
- see more from travis ( https://docs.travis-ci.com/user/tutorial/)
- additional rules (https://flask.palletsprojects.com/en/1.1.x/api/)
- check https://www.fullstackpython.com/api-creation.html

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
docker -it -p 5000:5000 ctsotskas/aristohub:latest bash
```

carry on from http://bobcares.com/blog/docker-port-expose/

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
