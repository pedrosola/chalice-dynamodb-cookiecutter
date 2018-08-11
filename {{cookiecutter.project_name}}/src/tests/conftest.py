import json
import random
import uuid

import pytest


@pytest.fixture
def create_event():
    def create_event_inner(uri, method, path, content_type='application/json'):
        return {
            'requestContext': {
                'httpMethod': method,
                'resourcePath': uri,
            },
            'headers': {
                'Content-Type': content_type,
            },
            'pathParameters': path,
            'queryStringParameters': {},
            'body': '',
            'stageVariables': {},
        }
    return create_event_inner
