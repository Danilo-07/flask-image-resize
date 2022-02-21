from unittest import skip

import pytest

from src.api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client


@skip
def test_resize(client):
    response = client.post('/resize', files={'image': 'test'})
    assert response.status == '200 OK'
    assert response.json == {'job_id': 'test'}


def test_resize_bad_request(client):
    response = client.post('/resize')
    assert response.status == '400 BAD REQUEST'
    assert response.json['message'] == 'Missing image file'
