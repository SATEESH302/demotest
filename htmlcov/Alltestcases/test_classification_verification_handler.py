from http import HTTPStatus
from classification_service.classification_verification_handler import lambda_handler
import json


def test_correct_parameters():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
        "body":json.dumps({
        "processingId": "CS2021000000318",
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

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_empty_json():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
        "body":{}}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_without_proceesing_id():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
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

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_wrong_spell_proceesing_id():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
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

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_wrong_proceesing_id():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
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

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_without_documentsData():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
        "body":json.dumps({
        "processingId": "CS202100000031825",

    })}
    expected_output = "C_121"

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output


def test_missing_source():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
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

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output

def test_missing_output():
    api_gateway_event = { "headers": {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDb25zaW50Iiwic3ViIjoiMiIsImV4cCI6MTYyMjc5NTU3MC4wODcyMzUyfQ.uuCVw8QukyiDor9PuSUrVQR742YO7ptFf-wBma8LHT0"},
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

    actual_output = lambda_handler(api_gateway_event, '')
    actual_output = json.loads(actual_output['body'])['operationOutcome']['errorCode']
    # print(actual_output)
    # print(expected_output)
    assert actual_output == expected_output
