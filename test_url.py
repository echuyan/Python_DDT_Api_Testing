import pytest
import requests


pytest.fixture(scope="module")
def test_url(url, status_code):
    result = requests.get(url)
    print(result.status_code)
