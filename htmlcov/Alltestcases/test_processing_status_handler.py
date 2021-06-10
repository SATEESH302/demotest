from http import HTTPStatus
from process_service.processing_status_handler import lambda_handler
import json


def test_correct_processingId():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
        "body":json.dumps({"processingId": "CS2021000000381"})}
    expected_output = "0"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_empty_josn():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":{}}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_wrong_spell_processing_id():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
        "body":json.dumps({"processingIdj": "CS2021000000381"})}
    expected_output = "C_122"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_missing_processing_id():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":json.dumps({})}
    expected_output = "C_122"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_wrong_spell_processing_id_value():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
        "body":json.dumps({"processingId": "CS202100000038887"})}
    expected_output = "B_100"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output