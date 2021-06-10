from http import HTTPStatus
from process_service import processing_status_handler 
import json

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



def test_correct_processingId(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000381"})}
    expected_output = "0"

    actual_output = processing_status_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_empty_josn(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":{}}
    expected_output = "C_121"

    actual_output = processing_status_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_wrong_spell_processing_id(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
        "body":json.dumps({"processingIdj": "CS2021000000381"})}
    expected_output = "C_122"

    actual_output = processing_status_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_missing_processing_id(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
                         "body":json.dumps({})}
    expected_output = "C_122"

    actual_output = processing_status_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_wrong_spell_processing_id_value(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS202100000038887"})}
    expected_output = "B_100"

    actual_output = processing_status_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output