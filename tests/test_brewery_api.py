import allure
import pytest


@allure.title("Сайт пивоварни по ID")
def test_brewery_website(api_client_brewery):
    response = api_client_brewery.get_single_brewery("06e9fffb-e820-45c9-b107-b52b51013e8f")
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    brewery_info = response.json()
    with allure.step("Проверяю URL сайта пивоварни"):
        assert brewery_info['website_url'] == "http://www.12degree.com"


@allure.title("Проверка названия пивоварни по ID")
@pytest.mark.parametrize("brew_id, expected_name", [
    ('b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0', 'MadTree Brewing 2.0'),
    ('06e9fffb-e820-45c9-b107-b52b51013e8f', '12Degree Brewing')])
def test_single_brewery_name(api_client_brewery, brew_id, expected_name):
    response = api_client_brewery.get_single_brewery(brew_id)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    brewery_info = response.json()
    with allure.step(f"Проверяю название пивоварни: {expected_name}"):
        assert brewery_info['name'] == expected_name


@allure.title("Проверка города пивоварни по ID")
@pytest.mark.parametrize("brew_id, expected_city", [
    ('b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0', 'Cincinnati'),
    ('06e9fffb-e820-45c9-b107-b52b51013e8f', 'Louisville')])
def test_single_brewery_city(api_client_brewery, brew_id, expected_city):
    response = api_client_brewery.get_single_brewery(brew_id)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    brewery_info = response.json()
    with allure.step(f"Проверяю, что город: {expected_city}"):
        assert brewery_info['city'] == expected_city


@allure.title("Координаты пивоварни по ID")
def test_brewery_coordinates(api_client_brewery):
    response = api_client_brewery.get_single_brewery("28945428-2326-41b3-b2d9-97f6e8154783")
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    brewery_info = response.json()
    with allure.step("Проверяю широту"):
        assert brewery_info['latitude'] == "32.7740128"
    with allure.step("Проверяю долготу"):
        assert brewery_info['longitude'] == "-117.1539235"


@allure.title("Получение списка пивоварен")
def test_list_breweries(api_client_brewery):
    response = api_client_brewery.get_list_breweries()
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что список пивоварен не пустой"):
        assert len(breweries_list) > 0


@allure.title("Фильтрация пивоварен по городу")
@pytest.mark.parametrize("city", ['san_diego'])
def test_breweries_by_city(api_client_brewery, city):
    response = api_client_brewery.get_breweries_by_city(city)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что все пивоварни из города San Diego"):
        for brewery in breweries_list:
            assert brewery['city'].replace(" ", "_").lower() == city.lower()


@allure.title("Сортировка пивоварен по расстоянию от точки")
@pytest.mark.parametrize("latitude, longitude", [("32.88313237", "-117.1649842")])
def test_breweries_by_distance(api_client_brewery, latitude, longitude):
    response = api_client_brewery.get_breweries_by_distance(latitude, longitude)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что список пивоварен не пустой"):
        assert len(breweries_list) > 0


@allure.title("Получение пивоварен по списку IDs")
@pytest.mark.parametrize("brewery_ids", ['701239cb-5319-4d2e-92c1-129ab0b3b440,06e9fffb-e820-45c9-b107-b52b51013e8f'])
def test_breweries_by_ids(api_client_brewery, brewery_ids):
    response = api_client_brewery.get_breweries_by_ids(brewery_ids)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что вернулись две пивоварни"):
        assert len(breweries_list) == 2


@allure.title("Фильтрация пивоварен по имени")
@pytest.mark.parametrize("name", ["Gordon", "mikkeller"])
def test_breweries_by_name(api_client_brewery, name):
    response = api_client_brewery.get_breweries_by_name(name)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что список пивоварен не пустой"):
        assert len(breweries_list) > 0
    with allure.step(f"Проверяю, что имя пивоварни содержит {name}"):
        for brewery in breweries_list:
            assert name.replace("_", " ").lower() in brewery['name'].lower()


@allure.title("Фильтрация пивоварен по штату")
@pytest.mark.parametrize("state", ["california", "ohio", "oklahoma", "texas", "mississippi"])
def test_breweries_by_state(api_client_brewery, state):
    response = api_client_brewery.get_breweries_by_state(state)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step(f"Проверяю, что все пивоварни находятся в штате {state}"):
        assert len(breweries_list) > 0
        for brewery in breweries_list:
            assert brewery['state'].lower() == state


@allure.title("Фильтрация пивоварен по типу")
def test_breweries_by_type(api_client_brewery):
    response = api_client_brewery.get_breweries_by_type("micro")
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что все пивоварни типа 'micro'"):
        assert len(breweries_list) > 0
        for brewery in breweries_list:
            assert brewery['brewery_type'] == "micro"


@allure.title("Проверка пагинации пивоварен")
def test_breweries_pagination(api_client_brewery):
    response = api_client_brewery.get_breweries_paginated(1, 3)
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что вернулись 3 пивоварни"):
        assert len(breweries_list) == 3


@allure.title("Фильтрация пивоварен по почтовому индексу")
def test_breweries_by_postal_code(api_client_brewery):
    response = api_client_brewery.get_breweries_by_postal_code("92101")
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    breweries_list = response.json()
    with allure.step("Проверяю, что все пивоварни имеют почтовый индекс 92101"):
        for brewery in breweries_list:
            assert brewery['postal_code'].startswith("92101")


@allure.title("Случайной пивоварня")
def test_random_brewery(api_client_brewery):
    response = api_client_brewery.get_random_brewery()
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    brewery = response.json()[0]  # Ответ API - это список
    with allure.step("Проверяю, что в ответе есть поле 'name'"):
        assert 'name' in brewery
    with allure.step("Проверяю, что в ответе есть поле 'brewery_type'"):
        assert 'brewery_type' in brewery


@allure.title("Наличие полей у случайной пивоварни")
def test_random_brewery_fields(api_client_brewery):
    response = api_client_brewery.get_random_brewery()
    with allure.step("Проверяю статус код"):
        assert response.status_code == 200
    brewery = response.json()[0]
    required_fields = ['name', 'brewery_type', 'city', 'state']
    with allure.step("Проверяю, что поля присутствуют"):
        assert all(field in brewery for field in required_fields)

