from http import HTTPStatus
from manual_triggers_service.trigger_classification_stage_handler import lambda_handler
import json



def test_correct_processingId():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000300","triggerEvent": "documentClassification"})}
    expected_output = "1"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_missing_processingId():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"triggerEvent": "documentClassification"})}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_missing_triggerevent():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000300"})}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_correct_trigger_event_with_document_classification():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000300","triggerEvent": "documentClassification"})}
    expected_output = "1"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_correct_trigger_event_with_entityExtraction():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000300","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_emty_json():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({})}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output



def test_correct_trigger_event_with_entityExtraction_progress():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000378","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_correct_trigger_event_with_entityExtraction_completed():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000378","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_wrong_trigger_event_with_entityExtraction():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000378","triggerEvent": "entityExtractiond"})}
    expected_output = "1"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_invalid_json_():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
                          "body": " na"}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_correct_trigger_event_with_document_classification_started ():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000403","triggerEvent": "documentClassification"})}
    expected_output = "0"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_correct_trigger_event_with_document_classification_progress ():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS2021000000403","triggerEvent": "documentClassification"})}
    expected_output = "0"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_correct_trigger_wrong_proceesing_id ():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMzA1NjUzMy4wMzEyNTJ9.QgI5CpL6qm3ez6WA1O-KglKqJIOODF0amvDz2asOGIc"},
        "body":json.dumps({"processingId": "CS202100000391","triggerEvent": "entityExtraction"})}
    expected_output = "1"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output