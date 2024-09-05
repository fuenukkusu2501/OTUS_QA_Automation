import pytest


@pytest.mark.parametrize("obdb_id", ['b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'])
def test_single_brewery(api_client_brewery, obdb_id):
    response = api_client_brewery.get_single_brewery(obdb_id)
    assert response.status_code == 200
    brewery_info = response.json()
    assert brewery_info['name'] == "MadTree Brewing 2.0"
    assert brewery_info['city'] == "Cincinnati"


def test_list_breweries(api_client_brewery):
    response = api_client_brewery.get_list_breweries()
    assert response.status_code == 200
    breweries_list = response.json()
    assert len(breweries_list) > 0


@pytest.mark.parametrize("city", ['san_diego'])
def test_breweries_by_city(api_client_brewery, city):
    response = api_client_brewery.get_breweries_by_city(city)
    assert response.status_code == 200
    breweries_list = response.json()
    for brewery in breweries_list:
        assert brewery['city'].replace(" ", "_").lower() == city.lower()


@pytest.mark.parametrize("latitude, longitude", [("32.88313237", "-117.1649842")])
def test_breweries_by_distance(api_client_brewery, latitude, longitude):
    response = api_client_brewery.get_breweries_by_distance(latitude, longitude)
    assert response.status_code == 200
    breweries_list = response.json()
    assert len(breweries_list) > 0
    print(response.json())


@pytest.mark.parametrize("brewery_ids", ['701239cb-5319-4d2e-92c1-129ab0b3b440,06e9fffb-e820-45c9-b107-b52b51013e8f'])
def test_breweries_by_ids(api_client_brewery, brewery_ids):
    response = api_client_brewery.get_breweries_by_ids(brewery_ids)
    assert response.status_code == 200
    breweries_list = response.json()
    assert len(breweries_list) == 2