import requests

"""
Server must be running in order these tests to work.
"""

SERVER_ADDRESS = "http://localhost:8000/"


def test_food_post():
    for i in range(10):
        response = requests.post(SERVER_ADDRESS,
                                 json={"id": i,
                                       "name": f"name{i}",
                                       "serving_size": 10,
                                       "kcal_per_serving": 20,
                                       "protein_grams": 30.1,
                                       "fibre_grams": 40.2})
        print(response)
        assert response.status_code == 201
        assert f"name{i}" in response.text.lower()


def test_get_all_foods():
    response = requests.get(f"{SERVER_ADDRESS}")
    print(response)
    assert response.status_code == 200


def test_get_food_by_id():
    response = requests.get(f"{SERVER_ADDRESS}1")
    print(response)
    assert response.status_code == 200
