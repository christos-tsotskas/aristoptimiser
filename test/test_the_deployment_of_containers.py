#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright 2020-present Christos Tsotskas

test_web_optimiser_configuration, part of aristoptimiser, https://github.com/christos-tsotskas/aristoptimiser

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

import unittest
import http.client
import pprint
import json
import os
import requests

class TestCaseForDeployment(unittest.TestCase):
    __URI = 'localhost'
    __port = 5000
    __HTTP_header_for_json = {'Content-type': 'application/json'}





    def test_Web_serve_data(self):

        request = requests.get('https://aristoptimiser.herokuapp.com/')
        if request.status_code == 200:
            print('Web site exists')
        else:
            print('Web site does not exist')



if __name__ == '__main__':
    unittest.main()
