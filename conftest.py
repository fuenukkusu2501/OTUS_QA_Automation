import pytest
from api_clients.api_client_placeholder import PlaceholderApiClient
from api_clients.dog_api_client import DogApiClient
from api_clients.brewery_api_client import BreweryApiClient


def pytest_addoption(parser):
    parser.addoption(
        "--dog-url",
        default="https://dog.ceo",
        help="Base URL for Dog API"
    )
    parser.addoption(
        "--brewery-url",
        default="https://api.openbrewerydb.org",
        help="Base URL for Brewery API"
    )
    parser.addoption(
        "--placeholder-url",
        default="https://jsonplaceholder.typicode.com",
        help="Base URL for Placeholder API"
    )


@pytest.fixture()
def dog_url(request):
    return request.config.getoption("--dog-url")


@pytest.fixture()
def brewery_url(request):
    return request.config.getoption("--brewery-url")


@pytest.fixture()
def placeholder_url(request):
    return request.config.getoption("--placeholder-url")


@pytest.fixture()
def api_client_dog(dog_url):
    return DogApiClient(base_url=dog_url)


@pytest.fixture()
def api_client_brewery(brewery_url):
    return BreweryApiClient(base_url=brewery_url)


@pytest.fixture()
def api_client_placeholder(placeholder_url):
    return PlaceholderApiClient(base_url=placeholder_url)
