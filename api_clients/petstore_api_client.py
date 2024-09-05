import requests


class PetstoreApiClient:

    def __init__(self, base_url="https://petstore.swagger.io/v2",
                 auth_token="special-key"):
        self.session = requests.Session()
        self.session.headers = {"Autorization": f"{auth_token}",
                        "Content-Type": "aplication/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_pets_by_status(self, query):
        response = self.session.get(url=f"{self.base_url}/pet/findByStatus",
                                    params=query,
                                    )
        return response


    def create_pet(self,data):
        response = self.session.post(url=f"{self.base_url}/pet",
                                      json=data,
                                      )
        return response


        # def create_user()




