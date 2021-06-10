from http import HTTPStatus
from manual_triggers_service import entity_extraction_verification_handler
import json
from login_service import login_handler

import pytest
import json

@pytest.fixture
def name1():

    api_gateway_event1 = {"body": '{"clientId": "1", "clientSecret": "abcdef"}'}
    d=login_handler.lambda_handler(api_gateway_event1,' ')

    f="Bearer "+d['headers']['AuthorizationHeader']

    return f


def test_correct_parameters(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
     "processingId": "CS2021000000398",
        "documentsData": [{
            "source": {
                "internalDocumentId": "e2aa5b13-a824-401b-8c8a-86bddd6f8516",
                "output": [{
                    "internalSubDocumentId": "17e915d1-a4ec-4827-9316-651132e7013d",
                    "entityVerification": "yes",
                    "docExtract": [{
                        "entityId": "3e35295e-bdfd-4e98-a876-5a14e32273b8",
                        "updatedValue": "icici bank"
                        }
                     ]
                    },
                    {
                    "internalSubDocumentId": "6e6f88dc-76ec-4627-8f91-63cbace4f744",
                    "entityVerification": "yes"
                }]
            }
        }]
    })}
    expected_output = "0"

    actual_output = entity_extraction_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_wrong_processing_id(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
     "processingId1": "CS2021000000398",
        "documentsData": [{
            "source": {
                "internalDocumentId": "e2aa5b13-a824-401b-8c8a-86bddd6f8516",
                "output": [{
                    "internalSubDocumentId": "17e915d1-a4ec-4827-9316-651132e7013d",
                    "entityVerification": "yes",
                    "docExtract": [{
                        "entityId": "3e35295e-bdfd-4e98-a876-5a14e32273b8",
                        "updatedValue": "icici bank"
                        }
                     ]
                    },
                    {
                    "internalSubDocumentId": "6e6f88dc-76ec-4627-8f91-63cbace4f744",
                    "entityVerification": "yes"
                }]
            }
        }]
    })}
    expected_output = "C_121"

    actual_output = entity_extraction_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_empty_processing_id(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
     "processingId": ",",
        "documentsData": [{
            "source": {
                "internalDocumentId": "e2aa5b13-a824-401b-8c8a-86bddd6f8516",
                "output": [{
                    "internalSubDocumentId": "17e915d1-a4ec-4827-9316-651132e7013d",
                    "entityVerification": "yes",
                    "docExtract": [{
                        "entityId": "3e35295e-bdfd-4e98-a876-5a14e32273b8",
                        "updatedValue": "icici bank"
                        }
                     ]
                    },
                    {
                    "internalSubDocumentId": "6e6f88dc-76ec-4627-8f91-63cbace4f744",
                    "entityVerification": "yes"
                }]
            }
        }]
    })}
    expected_output = "0"

    actual_output = entity_extraction_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_wrong_documentsData(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":json.dumps({
     "processingId": "CS2021000000398",
        "documentsData4": [{
            "source": {
                "internalDocumentId": "e2aa5b13-a824-401b-8c8a-86bddd6f8516",
                "output": [{
                    "internalSubDocumentId": "17e915d1-a4ec-4827-9316-651132e7013d",
                    "entityVerification": "yes",
                    "docExtract": [{
                        "entityId": "3e35295e-bdfd-4e98-a876-5a14e32273b8",
                        "updatedValue": "icici bank"
                        }
                     ]
                    },
                    {
                    "internalSubDocumentId": "6e6f88dc-76ec-4627-8f91-63cbace4f744",
                    "entityVerification": "yes"
                }]
            }
        }]
    })}
    expected_output = "C_121"

    actual_output = entity_extraction_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_emptyjson(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},
        "body":''}
    expected_output = "C_121"

    actual_output = entity_extraction_verification_handler.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
