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

from aristoptimiser.utilities import generate_base_configuration_to_a_file


class MyTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
