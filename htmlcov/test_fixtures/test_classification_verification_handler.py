from http import HTTPStatus
from classification_service import classification_verification_handler 
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



def test_correct_parameters(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
        "processingId": "CS202100000031825",
        "documentsData": [{
            "source": {
                "internalDocumentId": "06148770-7929-4c82-8a5d-3c3e2680e048",
                "output": [{
                        "internalSubDocumentId": "a0999397-b18c-434c-8035-85b30bf07006",
                        "updatedDocumentType": "pancard",
                        "classificationVerification": "yes"
                    }
                 ]
            }
        }]
    })}
    expected_output = "0"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_empty_json(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":{}}
    expected_output = "C_121"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_without_proceesing_id(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({

        "documentsData": [{
            "source": {
                "internalDocumentId": "06148770-7929-4c82-8a5d-3c3e2680e048",
                "output": [{
                        "internalSubDocumentId": "a0999397-b18c-434c-8035-85b30bf07006",
                        "updatedDocumentType": "pancard",
                        "classificationVerification": "yes"
                    }
                 ]
            }
        }]
    })}
    expected_output = "C_121"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_wrong_spell_proceesing_id(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
        "processingIdg": "CS2021000000318",
        "documentsData": [{
            "source": {
                "internalDocumentId": "06148770-7929-4c82-8a5d-3c3e2680e048",
                "output": [{
                        "internalSubDocumentId": "a0999397-b18c-434c-8035-85b30bf07006",
                        "updatedDocumentType": "pancard",
                        "classificationVerification": "yes"
                    }
                 ]
            }
        }]
    })}
    expected_output = "C_121"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_wrong_proceesing_id(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
        "processingId": "CS202100000031825",
        "documentsData": [{
            "source": {
                "internalDocumentId": "06148770-7929-4c82-8a5d-3c3e2680e048",
                "output": [{
                        "internalSubDocumentId": "a0999397-b18c-434c-8035-85b30bf07006",
                        "updatedDocumentType": "pancard",
                        "classificationVerification": "yes"
                    }
                 ]
            }
        }]
    })}
    expected_output = "0"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_without_documentsData(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
        "processingId": "CS202100000031825",

    })}
    expected_output = "C_121"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_missing_source(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
        "processingId": "CS202100000031825",
        "documentsData": [{
            "source1": {
                "internalDocumentId": "06148770-7929-4c82-8a5d-3c3e2680e048",
                "output": [{
                        "internalSubDocumentId": "a0999397-b18c-434c-8035-85b30bf07006",
                        "updatedDocumentType": "pancard",
                        "classificationVerification": "yes"
                    }
                 ]
            }
        }]
    })}
    expected_output = "B_100"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_output(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
        "processingId": "CS202100000031825",
        "documentsData": [{
            "source": {
                "internalDocumentId": "06148770-7929-4c82-8a5d-3c3e2680e048",
                "output1": [{
                        "internalSubDocumentId": "a0999397-b18c-434c-8035-85b30bf07006",
                        "updatedDocumentType": "pancard",
                        "classificationVerification": "yes"
                    }
                 ]
            }
        }]
    })}
    expected_output = "B_100"

    actual_output = classification_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
