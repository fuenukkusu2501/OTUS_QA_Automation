import os

import pytest

from api_clients.api_client_placeholder import PlaceholderApiClient
from api_clients.petstore_api_client import PetstoreApiClient
from api_clients.dog_api_client import DogApiClient
from api_clients.brewery_api_client import BreweryApiClient


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        type=int,
        default=200,
        help="Status code url"
    )


# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "url: specify the URL to test"
#     )
#     config.addinivalue_line(
#         "markers", "status_code: specify the expected status code"
#     )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


# @pytest.fixture
# def token(request):
#     return request.config.getoption("--token")


@pytest.fixture()
def api_client_dog(base_url, status_code):
    client = DogApiClient(base_url=base_url,
                          status_code=status_code) #переделать статускод, выяснить почему неожиданный аоргкмент
    return client


@pytest.fixture()
def api_client_brewery(base_url, status_code):
    client = BreweryApiClient()
    return client


@pytest.fixture()
def api_client_placeholder(base_url, status_code):
    client = PlaceholderApiClient()
    return client


# @pytest.fixture(scope="session")
# def api_client_brewery():
#     token = os.getenv("token") # задаем переменную окружения для jenkins
#     client = PetstoreApiClient()
#     return client

#рабочий код
# def pytest_addoption(parser):
#     parser.addoption(
#         "--url",
#         default="https://dog.ceo", #времено, возможно тут должен быть другой url
#         help="This is request url"
#     )
#
#     parser.addoption(
#         "--token",
#         help="token to autorize"
#     )

# рабочтй код
# @pytest.fixture(scope="session")
# def api_client_dog(base_url, token):
#     client = DogApiClient(base_url=base_url, auth_token=token)
#     return client
