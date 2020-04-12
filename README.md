# aristoptimiser
optimisation algorithm

Solver for an optimisation problem


# todo
- add coverage reports
```bash
            coverage run src/FizzBuzzer/testFizzBuzzer.py
            coverage report -m
            coverage html
            coverage xml -i
```

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


# R&D
- possibly use Nameko for microservices (https://www.toptal.com/python/introduction-python-microservices-nameko)
- better client than ( https://docs.python.org/3/library/http.client.html)
- see more from travis ( https://docs.travis-ci.com/user/tutorial/)
- additional rules (https://flask.palletsprojects.com/en/1.1.x/api/)
- check https://www.fullstackpython.com/api-creation.html

#Utilities

## connect to container via ssh
###approach 1
```bash
docker run -d -p 22 mysnapshot /usr/sbin/sshd -D
```

###approach2
run
```bash
docker exec -it busy_williamson bash
```

and then connect with
```bash
docker exec -it busy_williamson bash
```

carry on from http://bobcares.com/blog/docker-port-expose/

#Instructions to build the service

build with
```bash
docker build --no-cache -t web_optimiser:latest -f Dockerfile .
```

run with
```bash
docker run -d -p 5000:5000 web_optimiser:latest
```
