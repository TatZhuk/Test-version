import requests


def test_get_response_status_code():
    response = requests.get('https://api.github.com/repos/TatZhuk/Test-version')
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["full_name"] == "TatZhuk/Test-version"
