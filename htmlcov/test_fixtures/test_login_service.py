from http import HTTPStatus
from unittest import TestCase
from login_service.login_handler import lambda_handler


def test_incorrect_payload():
        api_gateway_event = {"body": '{ds}'}
        expected_output = HTTPStatus.BAD_REQUEST

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        # print(actual_output)
        # print(expected_output)
        assert actual_output == expected_output
        #self.assertEqual(actual_output, expected_output, msg="output is not as expected.")
def test_blank_payload():
        api_gateway_event = {"body": '{}'}
        expected_output = HTTPStatus.UNAUTHORIZED

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        assert actual_output== expected_output
        #self.assertEqual(actual_output, expected_output, msg="output is not as expected.")
def test_missing_payload_parameter():
        api_gateway_event = {"body": '{"clientId": "1"}'}
        expected_output = HTTPStatus.UNAUTHORIZED

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        assert actual_output == expected_output
        #self.assertEqual(actual_output, expected_output, msg="output is not as expected.")
def test_blank_payload_parameter():
        api_gateway_event = {"body": '{"clientId": "1", "clientSecret": ""}'}
        expected_output = HTTPStatus.UNAUTHORIZED

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        assert actual_output == expected_output
        #self.assertEqual(actual_output, expected_output, msg="output is not as expected.")
def test_incorrect_payload_parameter_value():
        api_gateway_event = {"body": '{"clientId": "1", "clientSecret": "abc"}'}
        expected_output = HTTPStatus.UNAUTHORIZED

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        assert actual_output == expected_output
        #self.assertEqual(actual_output, expected_output, msg="output is not as expected.")
def test_correct_payload_parameter_value():
        api_gateway_event = {"body": '{"clientId": "1", "clientSecret": "Regal"}'}
        expected_output = HTTPStatus.UNAUTHORIZED

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        assert actual_output == expected_output
        #self.assertEqual(actual_output, expected_output, msg="output is not as expected.")

def test_blank_payload_empatyc_clint_id():
        api_gateway_event = {"body": '{"clientId": "", "clientSecret": "adbcdef"}'}
        expected_output = HTTPStatus.UNAUTHORIZED

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        assert actual_output == expected_output


def test_correct1_payload_parameter():
        api_gateway_event = {"body": '{"clientId": "1", "clientSecret": "abcdef"}'}
        expected_output = HTTPStatus.OK

        actual_output = lambda_handler(api_gateway_event, '')
        actual_output = actual_output['statusCode']
        assert actual_output == expected_output
