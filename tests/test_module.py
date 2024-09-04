import pytest
import requests


def test_status_code():
    url = pytestconfig.getoption("url")
    expected_status_code = pytestconfig.getoption("status_code")
    response = requests.get(url)
    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"