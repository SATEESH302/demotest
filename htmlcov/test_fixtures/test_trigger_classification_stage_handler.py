from http import HTTPStatus
from manual_triggers_service import trigger_classification_stage_handler
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
        "body":json.dumps({"processingId": "CS2021000000300","triggerEvent": "documentClassification"})}
    expected_output = "1"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_missing_processingId(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"triggerEvent": "documentClassification"})}
    expected_output = "C_121"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_missing_triggerevent(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000300"})}
    expected_output = "C_121"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_correct_trigger_event_with_document_classification(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000300","triggerEvent": "documentClassification"})}
    expected_output = "1"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_correct_trigger_event_with_entityExtraction(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000300","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_emty_json(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({})}
    expected_output = "C_121"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_correct_trigger_event_with_entityExtraction_progress(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000378","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_correct_trigger_event_with_entityExtraction_completed(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000378","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_wrong_trigger_event_with_entityExtraction(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000378","triggerEvent": "entityExtractiond"})}
    expected_output = "1"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_invalid_json_(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
                          "body": " na"}
    expected_output = "C_121"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_correct_trigger_event_with_document_classification_started (name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000403","triggerEvent": "documentClassification"})}
    expected_output = "0"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_correct_trigger_event_with_document_classification_progress (name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000403","triggerEvent": "documentClassification"})}
    expected_output = "0"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_correct_trigger_wrong_proceesing_id (name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({"processingId": "CS202100000391","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output