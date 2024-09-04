import pytest





@pytest.mark.parametrize(["status, code"],
                         [("available, 200"), ("pending", 200), ("sold", 404)],
                        )
def test_get_pet_by_status(api_client, status):
    query = {"status": "available"}
    response = api_client.get_pets_by_status(query)
    json_response = response.json()
    assert response.status_code == code
    assert response.json()
