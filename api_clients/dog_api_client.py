import requests

class DogApiClient:

    def __init__(self, base_url="https://dog.ceo"):
        self.session = requests.Session()
        self.base_url = base_url

    def single_random_image(self):
        response = self.session.get(url=f"{self.base_url}/api/breeds/image/random"
                                    )
        return response

    def multiple_random_image(self, quantity):
        response = self.session.get(url=f"{self.base_url}/api/breeds/image/random/{quantity}"
                                      )
        return response

    def dogs_by_breed(self, breed):
        response = self.session.get(url=f"{self.base_url}/api/breed/{breed}/images"
                                    )
        return response
