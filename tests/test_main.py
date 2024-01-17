from unittest.mock import patch, MagicMock

import pytest
from flask.testing import FlaskClient

from main import app


@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client


def test_ping(client: FlaskClient):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.get_json() == "Pong"


@patch("main.SampleRequest")
def test_get_sample_route(mock_sample_request, client: FlaskClient):
    mock_sample_request.return_value = MagicMock()

    response = client.get('/sample-route?parameter1=value')

    assert response.status_code == 200
    assert response.get_json() == "Sample Response"

    mock_sample_request.assert_called_once_with(parameter1='value')


def test_get_sample_route_invalid_request(client: FlaskClient):
    response = client.get('/sample-route')

    assert response.status_code == 400
    assert response.get_json()["error"] is not None
