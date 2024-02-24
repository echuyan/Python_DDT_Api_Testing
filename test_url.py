import pytest
import requests


pytest.fixture(scope="module")
def test_url(url, status_code):
    result = requests.get(url)
    assert result.status_code == status_code
