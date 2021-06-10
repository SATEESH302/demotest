from http import HTTPStatus
from process_service.processing_list_handler import lambda_handler
import json

def test_correct_processinglist():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":json.dumps({ "clientId": "1",
                                            "startDate": "2021-05-13",
                                            "endDate": "2021-05-13"})}
    expected_output = "0"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_empty_json():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":json.dumps({})}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_empty_json_data():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":" na"}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_without_clint_id():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":json.dumps({
                                            "startDate": "2021-05-13",
                                            "endDate": "2021-05-13"})}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_without_start_date():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":json.dumps({ "clientId": "1",

                                            "endDate": "2021-05-13"})}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_without_end_date():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":json.dumps({ "clientId": "1",
                                            "startDate": "2021-05-13"
                                            })}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_incorrect_processinglist():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
                         "body":'{ "clientId": "1",,"startDate": "2021-05-13","endDate": "2021-05-13"}'}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
