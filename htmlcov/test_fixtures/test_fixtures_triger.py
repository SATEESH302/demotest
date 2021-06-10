from http import HTTPStatus
from manual_triggers_service import trigger_classification_stage_handler
import json
from login_service.login_handler import lambda_handler
from login_service import login_handler
import pytest

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


    api_gateway_event = { "headers": {
        "Authorization": f},
        "body":json.dumps({"processingId": "CS2021000000300","triggerEvent": "documentClassification"})}
    expected_output = "1"



    actual_output = trigger_classification_stage_handler.lambda_handler(api_gateway_event, '')

    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
