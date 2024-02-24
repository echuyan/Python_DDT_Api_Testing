import pytest
from base_request import BaseRequest


BASE_URL_PETSTORE = 'https://dog.ceo/api'
NON_EXISTENT_BREED = 'nonexistentbreed'

def test_get_all_breeds():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    breeds_list = base_request.get('breeds/list/all', "", expected_error=False)
    assert breeds_list is not None


def test_get_random_image():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    image_json = base_request.get('breeds/image/random', "", expected_error=False)
    assert image_json['status'] == "success"


@pytest.mark.parametrize("number, expected", [(3, 3), (52, 50)])
def test_get_many_random_images(number,expected):
    base_request = BaseRequest(BASE_URL_PETSTORE)
    endpoint = f'breeds/image/random/{number}'
    image_json = base_request.get(endpoint, "", expected_error=False)
    assert len(image_json['message']) == expected


@pytest.mark.parametrize("breed, expected", [('hound', 7), ('germanshepherd', 0)])
def test_get_sub_breeds(breed,expected):
    base_request = BaseRequest(BASE_URL_PETSTORE)
    endpoint = f'breed/{breed}/list'
    image_json = base_request.get(endpoint, "", expected_error=False)
    assert len(image_json['message']) == expected

def test_get_non_existent_breed():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    endpoint = f'breed/{NON_EXISTENT_BREED}/images/random'
    image_json = base_request.get(endpoint, "", expected_error=True)
    assert (image_json['message']) == 'Breed not found (master breed does not exist)'
