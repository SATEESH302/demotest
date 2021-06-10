from http import HTTPStatus
from process_service import generate_process_id 
import json
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


# def test_correct_s3():
#     api_gateway_event = {"headers": {"Authorization": f},
#         'body': json.dumps({"connectorType": "s3",
#         "documentJson": [
#             {
#                 "connectorId": "58",
#                 "documentId": "n/a",
#                 "documentName": "incomingDocuments/img10-merged.pdf",
#                 "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
#             }
#         ],
#         "identifierJson": {
#             "claimId": "ff",
#             "entityId": "value"
#         }})
#     }
#     # api_gateway_event = {"body": {}}
#     expected_output = "C_121"
#     actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
#     actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
#     # print(actual_output)
#     # print(expected_output)
#     assert actual_output == expected_output

def test_correct_emptys3(name1): # empty_s3

    f = name1
    api_gateway_event = {"headers": {"Authorization": f},
        'body':json.dumps({"connectorType": "",
        "documentJson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
        "identifierJson": {
            "claimId": "ff",
            "entityId": "value"
        }})
    }
    # api_gateway_event = {"body": {}}
    expected_output = "C_122"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_empty_json(name1): #emptyjson
    f = name1
    api_gateway_event = {
        "headers": {"Authorization": f},
        'body': ''
    }
    # api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_wrong_conncetor(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},
        'body':json.dumps({"connectorType": "satish",
        "documentJson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
        "identifierJson": {
            "claimId": "ff",
            "entityId": "value"
        }})
    }
    # api_gateway_event = {"body": {}}
    expected_output = "C_122"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_checking_without_documentjson(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},

        'body':json.dumps({"connectorType": "s3",
        "identifierJson": {
            "claimId": "ff",
            "entityId": "value"
        }})
}
    #api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_checking_wrong_spell_documentjson(name1):
    f=name1
    api_gateway_event = {
        "headers": {"Authorization": f},

        'body': json.dumps({"connectorType": "s3",
            "aocumentkoson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
        "identifierJson": {
            "claimId": "ff",
            "entityId": "value"
        }})
}
    #api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_checking_without_identifierJson(name1):
    f=name1
    api_gateway_event = { "headers": {"Authorization": f},

        'body':json.dumps({"connectorType": "s3",
                          "documentJson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
        })
}
    #api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_checking_wrongspell__identifierJson(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},

        'body':json.dumps({"connectorType": "s3",
            "documentJson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
            "identifierpJson": {
                "claimId": "ff",
                "entityId": "value"
            }})

}
    #api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_claim_id_identifierJson(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},


        'body':json.dumps({"connectorType": "s3",
            "documentJson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
            "identifierJson": {

                "entityId": "value"
            }})

}
    #api_gateway_event = {"body": {}}
    expected_output = "C_126"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_entity_id_identifierJson(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},

        'body':json.dumps({"connectorType": "s3",
            "documentJson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
            "identifierJson": {

                 "claimId": "ff"
            }})

}
    #api_gateway_event = {"body": {}}
    expected_output = "C_127"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_connceter_id_identifierJson(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},

        'body':json.dumps({"connectorType": "s3",
            "documentJson": [
            {
                "connectorId": "",
                "documentId": "n/a",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
            "identifierpJson": {
                "entityId": "value",
                 "claimId": "ff"

            }})

}
    #api_gateway_event = {"body": {}}
    expected_output = "C_123"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_documentId_identifierJson(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},

        'body':json.dumps({"connectorType": "s3",
            "documentJson": [
            {
                "connectorId": "58",
                "documentId": "",
                "documentName": "incomingDocuments/img10-merged.pdf",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
            "identifierpJson": {
                "entityId": "value",
                 "claimId": "ff"

            }})

}
    #api_gateway_event = {"body": {}}
    expected_output = "C_124"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_document_name_identifierJson(name1):
    f=name1
    api_gateway_event = {"headers": {"Authorization": f},

        'body':json.dumps({"connectorType": "s3",
            "documentJson": [
            {
                "connectorId": "58",
                "documentId": "n/a",
                "documentName": "",
                "documentUrl": "https://document-cdn.s3.us-east-2.amazonaws.com/incomingDocuments/class.pdf"
            }
        ],
            "identifierpJson": {
                "entityId": "value",
                 "claimId": "ff"

            }})

}
    #api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = generate_process_id.lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


