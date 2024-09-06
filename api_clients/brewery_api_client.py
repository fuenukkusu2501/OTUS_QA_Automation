import allure
import requests


class BreweryApiClient:

    def __init__(self, base_url="https://api.openbrewerydb.org"):
        self.session = requests.Session()
        self.base_url = base_url

    @allure.step("Получаю информацию о пивоварне по ее ID")
    def get_single_brewery(self, brew_id):
        url = f"{self.base_url}/v1/breweries/{brew_id}"
        response = self.session.get(url)
        return response

    @allure.step("Получаю список пивоварен")
    def get_list_breweries(self):
        url = f"{self.base_url}/v1/breweries"
        response = self.session.get(url)
        return response

    @allure.step("Фильтрую пивоварни по городу")
    def get_breweries_by_city(self, city):
        url = f"{self.base_url}/v1/breweries"
        params = {"by_city": city}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Фильтрую пивоварни по координатам")
    def get_breweries_by_distance(self, latitude, longitude):
        url = f"{self.base_url}/v1/breweries"
        params = {"by_dist": f"{latitude},{longitude}"}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Получаю список пивоварен по их IDs")
    def get_breweries_by_ids(self, brewery_ids):
        url = f"{self.base_url}/v1/breweries"
        params = {"by_ids": brewery_ids}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Фильтрую пивоварни по названию")
    def get_breweries_by_name(self, name, per_page=3):
        url = f"{self.base_url}/v1/breweries"
        params = {"by_name": name, "per_page": per_page}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Фильтрую пивоварни по штату")
    def get_breweries_by_state(self, state, per_page=3):
        url = f"{self.base_url}/v1/breweries"
        params = {"by_state": state, "per_page": per_page}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Фильтрую пивоварни по типу")
    def get_breweries_by_type(self, brewery_type, per_page=3):
        url = f"{self.base_url}/v1/breweries"
        params = {"by_type": brewery_type, "per_page": per_page}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Фильтрую пивоварни по индексу")
    def get_breweries_by_postal_code(self, postal_code, per_page=3):
        url = f"{self.base_url}/v1/breweries"
        params = {"by_postal": postal_code, "per_page": per_page}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Получаю список пивоварен с пагинацией")
    def get_breweries_paginated(self, page, per_page):
        url = f"{self.base_url}/v1/breweries"
        params = {"page": page, "per_page": per_page}
        response = self.session.get(url, params=params)
        return response

    @allure.step("Получаю случайную пивоварню")
    def get_random_brewery(self):
        url = f"{self.base_url}/v1/breweries/random"
        response = self.session.get(url)
        return response
