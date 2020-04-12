#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright 2020-present Christos Tsotskas

web_optimiser_configuration, part of aristoptimiser, https://github.com/christos-tsotskas/aristoptimiser

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

Apache 2.0

Leader author: Christos Tsotskas
Created by christos at 11/04/2020

"""

__author__ = 'Christos Tsotskas'
__copyright__ = 'Copyright 2020, Aristo'
__credits__ = ['{credit_list}']
__license__ = 'Apache'
__version__ = '0.1.1'
__maintainer__ = 'Christos Tsotskas'
__email__ = 'c.tsotskas@gmail.com'
__status__ = 'Prototype'

import time
from flask import Flask, request, jsonify

from OptimiserConfigurator import OptimiserConfigurator
import json
import os
import logging
from logging.handlers import RotatingFileHandler

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route('/')
def hello():
    user_agent = request.headers.get('User-Agent')
    return 'Optimiser at your service! I see you are using %s' % user_agent

@app.route('/message')
def agaph():
    user_agent = request.headers.get('User-Agent')
    return 'To paki s agapaei kotoula!!!!1! I see you are using %s' % user_agent


@app.route('/serve_data/', methods=['POST'])
def serve_data():
    data = request.get_json()

    if data == None:
        HTTP_return_code = 405
    else:
        HTTP_return_code = 200

    return 'Data received', HTTP_return_code


@app.route('/configure_optimiser/', methods=['POST'])
def configure_optimiser():
    data = request.get_json()

    r = json.dumps(data)

    testClass = OptimiserConfigurator(json_object=r)

    output = testClass.are_all_decision_variables_within_range()



    if output == True:
        HTTP_return_code = 200
        message = 'all good! '
    else:
        HTTP_return_code = 405
        message = 'Something is wrong'



    return message, HTTP_return_code




if __name__ == '__main__':
    filename_for_log = "web_optimiser_configurator" +".log"
    handler = RotatingFileHandler(filename_for_log, maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    # app.run(host='127.0.0.1', port=int(os.getenv('PORT', 5000)))
    # app.run(host='127.0.0.1', port=5000)
    app.run(debug=True, host='0.0.0.0')