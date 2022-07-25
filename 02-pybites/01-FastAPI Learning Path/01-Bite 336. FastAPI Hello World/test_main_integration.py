import requests

"""
Server must be running in order these tests to work.
"""

SERVER_ADDRESS = "http://localhost:8000/"


def test_main_integration():
    response = requests.get(SERVER_ADDRESS)
    print()
    assert response.status_code == 200
    assert "fastapi" in response.text.lower()
