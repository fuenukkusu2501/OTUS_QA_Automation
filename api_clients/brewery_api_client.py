import requests

class BreweryApiClient:

    def __init__(self, base_url="https://api.openbrewerydb.org"):
        self.session = requests.Session()
        self.base_url = base_url

    def get_single_brewery(self, obdb_id):
        response = self.session.get(url=f"{self.base_url}/v1/breweries/{obdb_id}"
                                    )
        return response

    def get_list_breweries(self):
        url = f"{self.base_url}/breweries"
        response = self.session.get(url)
        return response

    def get_breweries_by_city(self, city):
        url = f"{self.base_url}/breweries"
        params = {"by_city": city}
        response = self.session.get(url, params=params)
        return response

    def get_breweries_by_distance(self, latitude, longitude):
        url = f"{self.base_url}/breweries"
        params = {"by_dist": f"{latitude},{longitude}"}
        response = self.session.get(url, params=params)
        return response

    def get_breweries_by_ids(self, brewery_ids):
        url = f"{self.base_url}/breweries"
        params = {"by_ids": brewery_ids}
        response = self.session.get(url, params=params)
        return response


