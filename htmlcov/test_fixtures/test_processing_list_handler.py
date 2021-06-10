from http import HTTPStatus
from process_service import processing_list_handler 

from login_service import login_handler

import pytest
import json

@pytest.fixture
def name1():

    api_gateway_event1 = {"body": '{"clientId": "1", "clientSecret": "abcdef"}'}
    d=login_handler.lambda_handler(api_gateway_event1,' ')
    print(d)
    f="Bearer "+d['headers']['AuthorizationHeader']
    print('key###',f)
    return f




def test_correct_processinglist(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":json.dumps({ "clientId": "1",
                                            "startDate": "2021-05-13",
                                            "endDate": "2021-05-13"})}
    expected_output = "0"

    actual_output = processing_list_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_empty_json(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":json.dumps({})}
    expected_output = "C_121"

    actual_output = processing_list_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_empty_json_data(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":" na"}
    expected_output = "C_121"

    actual_output = processing_list_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_without_clint_id(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":json.dumps({
                                            "startDate": "2021-05-13",
                                            "endDate": "2021-05-13"})}
    expected_output = "C_121"

    actual_output = processing_list_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_without_start_date(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":json.dumps({ "clientId": "1",

                                            "endDate": "2021-05-13"})}
    expected_output = "C_121"

    actual_output = processing_list_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_without_end_date(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":json.dumps({ "clientId": "1",
                                            "startDate": "2021-05-13"
                                            })}
    expected_output = "C_121"

    actual_output = processing_list_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_incorrect_processinglist(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":'{ "clientId": "1",,"startDate": "2021-05-13","endDate": "2021-05-13"}'}
    expected_output = "C_121"

    actual_output = processing_list_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
