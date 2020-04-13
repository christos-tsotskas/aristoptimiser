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

class TestCaseForWebOptimiserConfigurator(unittest.TestCase):
    __URI = 'localhost'
    __port = 5000
    __HTTP_header_for_json = {'Content-type': 'application/json'}


    def get_filepath_from_resouces_starting_from_tests_directory(self, target_filename):
        here = __file__
        path_to_tests, this_file = os.path.split(here)
        path_to_root, dummy = os.path.split(path_to_tests)
        path_to_target_file = os.path.join(path_to_root, 'resources', target_filename)

        return path_to_target_file

    def test_Web_optimiser_configuration_with_good_input(self):

        connection = http.client.HTTPConnection(self.__URI, self.__port, timeout=10)

        print(connection)



        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory('small_good_configuration.json')
        with open(path_to_target_file, "r") as read_file:
            data = json.load(read_file)


            json_data = json.dumps(data)

            connection.request("POST", "/configure_optimiser/", json_data, self.__HTTP_header_for_json)
            response = connection.getresponse()

            headers_from_the_service = response.getheaders()
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint("Headers: {}".format(headers_from_the_service))
            print("Status: {} and reason: {}".format(response.status, response.reason))

            print(response.read().decode())

            self.assertEqual(response.status, 200)
        connection.close()

    def test_Web_optimiser_configuration_with_bad_input(self):

        connection = http.client.HTTPConnection(self.__URI, self.__port, timeout=10)

        print(connection)



        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory('small_bad_configuration.json')
        with open(path_to_target_file, "r") as read_file:
            data = json.load(read_file)


            json_data = json.dumps(data)

            connection.request("POST", "/configure_optimiser/", json_data, self.__HTTP_header_for_json)
            response = connection.getresponse()

            headers = response.getheaders()
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint("Headers: {}".format(headers))
            print("Status: {} and reason: {}".format(response.status, response.reason))

            print(response.read().decode())

            self.assertEqual(response.status, 405)
        connection.close()

    def test_Web_serve_data(self):
        connection = http.client.HTTPConnection(self.__URI, self.__port, timeout=10)

        print(connection)

        headers = {'Content-type': 'application/json'}
        foo = {"text": "Hello HTTP #1 **cool**, and #1!"}



        json_data = json.dumps(foo)

        connection.request("POST", "/serve_data/", json_data, headers)
        response = connection.getresponse()

        headers = response.getheaders()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint("Headers: {}".format(headers))
        print("Status: {} and reason: {}".format(response.status, response.reason))

        print(response.read().decode())
        connection.close()




if __name__ == '__main__':
    unittest.main()
