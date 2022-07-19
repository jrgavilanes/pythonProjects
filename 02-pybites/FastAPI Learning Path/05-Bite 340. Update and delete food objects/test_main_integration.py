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


def test_update_food():
    response = requests.put(f"{SERVER_ADDRESS}1",
                            json={"id": 1,
                                  "name": f"updated_name1",
                                  "serving_size": 90,
                                  "kcal_per_serving": 80,
                                  "protein_grams": 70.1,
                                  "fibre_grams": 60.2})

    assert response.status_code == 200
    assert "updated_name1" in response.text.lower()

    response = requests.put(f"{SERVER_ADDRESS}100",
                            json={"id": 100,
                                  "name": f"updated_name1",
                                  "serving_size": 90,
                                  "kcal_per_serving": 80,
                                  "protein_grams": 70.1,
                                  "fibre_grams": 60.2})
    assert response.status_code == 404


def test_delete_food():
    response = requests.delete(f"{SERVER_ADDRESS}1")
    assert response.status_code == 200

    response = requests.delete(f"{SERVER_ADDRESS}100")
    assert response.status_code == 404
