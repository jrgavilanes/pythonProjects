import requests

"""
Server must be running in order these tests to work.
"""

SERVER_ADDRESS = "http://localhost:8000/"


def test_food_post():
    response = requests.post(SERVER_ADDRESS,
                             json={"id": 1,
                                   "name": "name1",
                                   "serving_size": 10,
                                   "kcal_per_serving": 20,
                                   "protein_grams": 30.1,
                                   "fibre_grams": 40.2})
    print()
    assert response.status_code == 201
    assert "name1" in response.text.lower()
