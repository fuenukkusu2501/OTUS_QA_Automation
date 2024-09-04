import pytest
import requests

"""Тесты для dog.ceo"""


def test_single_random_dog_image(api_client_dog):
    response = api_client_dog.single_random_image()
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["status"] == "success"


@pytest.mark.parametrize("quantity", [1, 3, 50])
def test_multiple_random_dog_images(api_client_dog, quantity):
    response = api_client_dog.multiple_random_image(quantity)
    assert response.status_code == 200
    assert len(response.json()["message"]) == quantity
    assert response.json()["status"] == "success"


@pytest.mark.parametrize("quantity", [51, 999999])
def test_multiple_random_dog_more_than_50(api_client_dog, quantity):
    response = api_client_dog.multiple_random_image(quantity)
    assert response.status_code == 200
    assert len(response.json()["message"]) == 50
    assert response.json()["status"] == "success"


def test_dogs_by_breed_positiv(api_client_dog):
    response = api_client_dog.dogs_by_breed(breed="hound")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["status"] == "success"


@pytest.mark.parametrize("breed", ['hound', "komondor"])
def test_dogs_by_breed(api_client_dog, breed):
    response = api_client_dog.dogs_by_breed(breed)
    json_response = response.json()
    message = json_response['message']
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    for row in message:
        assert breed in row
# 1) assert "i" in "iris"
# 2) all()
# 3) А просто assert с contains в стринге нельзя проверить?
""" Тесты для пивнухи """

# Тест для получения информации о конкретном заводе:
@pytest.mark.parametrize("obdb_id", ['b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'])
def test_single_brewery(api_client_brewery, obdb_id):
    response = api_client_brewery.get_single_brewery(obdb_id)
    assert response.status_code == 200
    brewery_info = response.json()
    assert brewery_info['name'] == "MadTree Brewing 2.0"
    assert brewery_info['city'] == "Cincinnati"


# Тест для получения списка заводов:


def test_list_breweries(api_client_brewery):
    response = api_client_brewery.get_list_breweries()
    assert response.status_code == 200
    breweries_list = response.json()
    assert len(breweries_list) > 0


#  Тест для фильтрации заводов по городу:


@pytest.mark.parametrize("city", ['san_diego'])
def test_breweries_by_city(api_client_brewery, city):
    response = api_client_brewery.get_breweries_by_city(city)
    assert response.status_code == 200
    breweries_list = response.json()
    for brewery in breweries_list:
        assert brewery['city'].replace(" ", "_").lower() == city.lower()


# Тест для сортировки результатов по расстоянию от точки отправления:

@pytest.mark.parametrize("latitude, longitude", [("32.88313237", "-117.1649842")])
def test_breweries_by_distance(api_client_brewery, latitude, longitude):
    response = api_client_brewery.get_breweries_by_distance(latitude, longitude)
    assert response.status_code == 200
    breweries_list = response.json()
    # Здесь можно добавить дополнительные проверки по сортировке списка заводов по расстоянию
    assert len(breweries_list) > 0
    print(response.json())



# Тест для получения заводов по списку идентификаторов:


@pytest.mark.parametrize("brewery_ids", ['701239cb-5319-4d2e-92c1-129ab0b3b440,06e9fffb-e820-45c9-b107-b52b51013e8f'])
def test_breweries_by_ids(api_client_brewery, brewery_ids):
    response = api_client_brewery.get_breweries_by_ids(brewery_ids)
    assert response.status_code == 200
    breweries_list = response.json()
    assert len(breweries_list) == 2  # Проверяем, что вернулись два завода