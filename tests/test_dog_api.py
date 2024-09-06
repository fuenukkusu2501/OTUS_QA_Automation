import pytest


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