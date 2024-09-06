import pytest
from api_clients.brewery_api_client import BreweryApiClient


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://api.openbrewerydb.org",
        help="Base URL for Brewery API"
    )


@pytest.fixture()
def brewery_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def api_client_brewery(brewery_url):
    return BreweryApiClient(base_url=brewery_url)

