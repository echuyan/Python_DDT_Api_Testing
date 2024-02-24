import pytest
from base_request import BaseRequest
import random
from collections import Counter

BASE_URL_PETSTORE = 'https://api.openbrewerydb.org/v1'

def test_get_all_breweries():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    breweries_list = base_request.get('breweries', "", expected_error=False)
    assert breweries_list

@pytest.fixture(scope="session")
def get_cities():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    breweries_list = base_request.get('breweries?per_page=200', "", expected_error=False)
    cities = [item["city"] for item in breweries_list]
    city_counts = Counter(cities)
    filtered_cities = {city for city, count in city_counts.items() if count > 2}
    return filtered_cities


@pytest.fixture(scope="module")
@pytest.mark.parametrize("perpage, expected", [(2, 2), (1, 1)])
def test_get_breweries_by_city_per_page(get_cities, perpage, expected):
    base_request = BaseRequest(BASE_URL_PETSTORE)
    city = random.choice(list(get_cities))
    result = base_request.get(f'breweries?by_city={city}&per_page={perpage}', "", expected_error=False)
    assert len(result)==expected


@pytest.mark.parametrize("type, expected", [("micro", "micro"), ("proprietor", "proprietor"), ("nano", "nano"), ("brewpub", "brewpub"), ("regional", "regional")])
def test_get_breweries_by_type(type,expected):
    base_request = BaseRequest(BASE_URL_PETSTORE)
    endpoint = f'breweries?by_type={type}&per_page=3'
    result = base_request.get(endpoint, "", expected_error=False)
    types1 = list({item["brewery_type"] for item in result})
    #types2 = [item["brewery_type"] for item in result]
    assert len(types1) == 1 and types1[0] == expected



@pytest.mark.parametrize("number, expected", [(3, 3), (52, 50)])
def test_get_random_brewery(number,expected):
    base_request = BaseRequest(BASE_URL_PETSTORE)
    endpoint = 'breweries/random'
    result = base_request.get(endpoint, "", expected_error=False)
    assert len(result)==1


def test_get_non_existent_city():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    endpoint = 'breweries?by_city=NON_EXIST'
    result = base_request.get(endpoint, "", expected_error=False)
    assert len(result) == 0


