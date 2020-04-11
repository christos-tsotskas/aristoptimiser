#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright 2020-present Christos Tsotskas

Utilities part of aristoptimiser, https://github.com/christos-tsotskas/aristoptimiser

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


def generate_base_configuration():

    example_output = {
        "name": "just a name",
        "decision_variables": [
            {"name": "just first", "type": "real", "lower_bound": 1.0, "upper_bound": 100.3},
            {"name": "secundo", "type": "real", "lower_bound": 4.1, "upper_bound": 32.3},
            {"name": "tria", "type": "real", "lower_bound": -3.1, "upper_bound": 12.9}
        ],
        "settings_for_optimiser":{
            "optimiser": "MOTS4",
            "starting_point": {
                "just first":3.3,
                "secundo":6.2,
                "tria":9.4
            }
        }

    }

    return json.dumps(example_output)

def generate_base_configuration_to_a_file(name_of_output_file):
    '''
    :name_of_output_file: string of a filename

    :return: configuration in json format
    '''
    #todo the configuration always assumes equality in the bounds
    #todo if starting point is dict, the order of variables could be any,
    #todo if starting point is an array, it is assumed that the order of variables matches the decion variables
    intermediate_data = generate_base_configuration()

    outpute_data = json.loads(intermediate_data)


    with open(name_of_output_file, "w") as write_file:
        json.dump(outpute_data, write_file, indent=4)

if __name__ == "__main__":
    generate_base_configuration_to_a_file("data3.json")