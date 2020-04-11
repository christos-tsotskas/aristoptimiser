import unittest
import http.client
import pprint
import json
import os

class TestCaseForWebOptimiserConfigurator(unittest.TestCase):
    __URI = 'localhost'
    __port = 5002


    def get_filepath_from_resouces_starting_from_tests_directory(self, target_filename):
        here = __file__
        path_to_tests, this_file = os.path.split(here)
        path_to_root, dummy = os.path.split(path_to_tests)
        path_to_target_file = os.path.join(path_to_root, 'resources', target_filename)

        return path_to_target_file

    def test_Web_optimiser_configuration_with_good_input(self):

        connection = http.client.HTTPConnection(self.__URI, self.__port, timeout=10)

        print(connection)

        headers = {'Content-type': 'application/json'}

        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory('small_good_configuration.json')
        with open(path_to_target_file, "r") as read_file:
            data = json.load(read_file)

            # foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
            json_data = json.dumps(data)

            connection.request("POST", "/configure_optimiser/", json_data, headers)
            response = connection.getresponse()

            headers = response.getheaders()
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint("Headers: {}".format(headers))
            print("Status: {} and reason: {}".format(response.status, response.reason))

            print(response.read().decode())

            self.assertEqual(response.status, 200)
        connection.close()

    def test_Web_optimiser_configuration_with_bad_input(self):

        connection = http.client.HTTPConnection(self.__URI, self.__port, timeout=10)

        print(connection)

        headers = {'Content-type': 'application/json'}

        path_to_target_file = self.get_filepath_from_resouces_starting_from_tests_directory('small_bad_configuration.json')
        with open(path_to_target_file, "r") as read_file:
            data = json.load(read_file)

            # foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
            json_data = json.dumps(data)

            connection.request("POST", "/configure_optimiser/", json_data, headers)
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
