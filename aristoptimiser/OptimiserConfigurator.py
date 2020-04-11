#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright 2020-present Christos Tsotskas

Optimiser Configurator, part of aristoptimiser, https://github.com/christos-tsotskas/aristoptimiser

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


import json

#todo add functionality to throw exceptions for bad inputs

class OptimiserConfigurator:
    '''

    Expecting a configuration file such as:

    {
        "name": "just a name",
        "decision_variables": [
            {"name": "just first", "type": "real", "lower_bound": 1.0, "upper_bound": 100.3},
            {"name": "secundo", "type": "real", "lower_bound": 4.1, "upper_bound": 32.3},
            {"name": "tria", "type": "real", "lower_bound": -3.1, "upper_bound": 12.9}
        ],
        "settings_for_optimiser":{
            "optimiser": "MOTS4",
            "starting_point": {
                "just first":1.3,
                "secundo":5.2,
                "tria":9.4
            }
        }

    }

    '''

    configuration = None


    def is_decision_variable_within_its_bounds(self, name, value):
        output = False

        for decision_variable in self.configuration["decision_variables"]:
            if decision_variable['name'] == name:
                lower = decision_variable["lower_bound"]
                upper = decision_variable["upper_bound"]


        if lower<=value and value<=upper:
            output = True

        return output

    def are_all_decision_variables_within_range(self):
        '''

        :return: True if everything is ok, False otherwise
        '''
        check = True

        for decision_variable in self.configuration["settings_for_optimiser"]["starting_point"].items():
            temp = self.is_decision_variable_within_its_bounds(decision_variable[0], decision_variable[1])
            check = temp and check

        return check

    def __init__(self, configuration_filename):
        '''

        :param configuration_filename: path to configuration file as a string
        '''

        with open(configuration_filename, "r") as read_file:
            self.configuration = json.load(read_file)



        pass


