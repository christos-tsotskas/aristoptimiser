#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utilities, part of aristoptimiser, https://github.com/christos-tsotskas/aristoptimiser

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
            {"name": "secundo", "type": "real", "lower_bound": 4.1, "upper_bound": 32.3}
        ],
        "settings_for_optimiser":{
            "optimiser": "MOTS4",
            "starting_point": [
                3.3,
                6.2
            ]
        }

    }



    print(json.dumps(example_output, sort_keys=True, indent=4))


if __name__ == "__main__":
    generate_base_configuration()