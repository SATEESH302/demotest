from http import HTTPStatus
from process_service.generate_process_id import lambda_handler
import json


# def test_correct_s3():
#     api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
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
#     actual_output = lambda_handler(api_gateway_event, '')
#     actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
#     # print(actual_output)
#     # print(expected_output)
#     assert actual_output == expected_output

def test_correct_emptys3(): # empty_s3
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_empty_json(): #emptyjson
    api_gateway_event = {
        "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
        'body': ''
    }
    # api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_wrong_conncetor():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},
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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_checking_without_documentjson():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

        'body':json.dumps({"connectorType": "s3",
        "identifierJson": {
            "claimId": "ff",
            "entityId": "value"
        }})
}
    #api_gateway_event = {"body": {}}
    expected_output = "C_121"
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
def test_checking_wrong_spell_documentjson():
    api_gateway_event = {
        "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_checking_without_identifierJson():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_checking_wrongspell__identifierJson():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_claim_id_identifierJson():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},


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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_entity_id_identifierJson():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_connceter_id_identifierJson():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_documentId_identifierJson():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_document_name_identifierJson():
    api_gateway_event = {"headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjcyODM1MS42MDI3MTQzfQ.KCokToJ6J6RTSRwdqCIjJQgo9_BLTEJj7DYuk_HqPBM"},

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
    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


