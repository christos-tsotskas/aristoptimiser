#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright 2020-present Christos Tsotskas

Test configuration of optimiser, part of aristoptimiser, https://github.com/christos-tsotskas/aristoptimiser

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

Apache 2.0

Leader author: Christos Tsotskas



"""

__author__ = 'Christos Tsotskas'
__copyright__ = 'Copyright 2020, Aristo'
__credits__ = ['{credit_list}']
__license__ = 'Apache'
__version__ = '0.1.0'
__maintainer__ = 'Christos Tsotskas'
__email__ = 'c.tsotskas@gmail.com'
__status__ = 'Prototype'

import unittest
import json
import os

from aristoptimiser.utilities import generate_base_configuration_to_a_file
from aristoptimiser.OptimiserConfigurator import OptimiserConfigurator

class MyTestCase(unittest.TestCase):
    def setUp(self):

        pass

    def tearDown(self):
        pass


    def get_bounds(self):
        pass

    def is_decision_variable_within_its_bounds(self, name, value, configuration):
        output = False

        for decision_variable in configuration:
            if decision_variable['name'] == name:
                lower = decision_variable["lower_bound"]
                upper = decision_variable["upper_bound"]


        if lower<=value and value<=upper:
            output = True

        return output

    def test_starting_point_is_within_range(self):
        test_filename = "test2.json"
        check = False

        generate_base_configuration_to_a_file(test_filename)

        with open(test_filename, "r") as read_file:
            data = json.load(read_file)

            for decision_variable in data["settings_for_optimiser"]["starting_point"].items():
                check = self.is_decision_variable_within_its_bounds(decision_variable[0], decision_variable[1], data["decision_variables"])
                self.assertTrue(check)

    def get_filepath_from_resouces_starting_from_tests_directory(self, target_filename):
        here = __file__
        path_to_tests, this_file = os.path.split(here)
        path_to_root, dummy = os.path.split(path_to_tests)
        path_to_target_file = os.path.join(path_to_root, 'resources', target_filename)

        return path_to_target_file

    def test_good_configuration_file(self):

        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory('small_good_configuration.json')

        with open(path_to_target_file, "r") as read_file:
            data = json.load(read_file)

            for decision_variable in data["settings_for_optimiser"]["starting_point"].items():
                check = self.is_decision_variable_within_its_bounds(decision_variable[0], decision_variable[1],
                                                                    data["decision_variables"])
                self.assertTrue(check)


    def test_good_configuration_file_by_using_OptimiserConfigurator(self):


        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory('small_good_configuration.json')

        testClass = OptimiserConfigurator(path_to_target_file)

        self.assertTrue(testClass.are_all_decision_variables_within_range())

    def test_bad_configuration_file_by_using_OptimiserConfigurator(self):


        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory('small_bad_configuration.json')

        testClass = OptimiserConfigurator(path_to_target_file)

        self.assertFalse(testClass.are_all_decision_variables_within_range())


    def test_bad_configuration_file(self):
        number_of_expected_bad_decision_variables = 2
        currently_found_bad_decision_variables = 0

        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory(
            'small_bad_configuration.json')

        with open(path_to_target_file, "r") as read_file:
            data = json.load(read_file)

            for decision_variable in data["settings_for_optimiser"]["starting_point"].items():
                check = self.is_decision_variable_within_its_bounds(decision_variable[0], decision_variable[1],
                                                                    data["decision_variables"])
                if check == False:
                    currently_found_bad_decision_variables += 1

        self.assertEqual(currently_found_bad_decision_variables, number_of_expected_bad_decision_variables)



if __name__ == '__main__':
    unittest.main()
