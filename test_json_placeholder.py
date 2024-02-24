import pytest
from base_request import BaseRequest
import random
from collections import Counter
import json

BASE_URL_PETSTORE = 'https://jsonplaceholder.typicode.com'

def test_get_all_posts():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    result = base_request.get('posts', "", expected_error=False)
    assert result is not None


def test_post_post():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    body = {
    "title": "foo",
    "body": "bar",
    "userId": "1"
}
    result = base_request.post('posts',"",body,expected_error=True)
    assert result['id'] is not None



def get_resources():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    res_list = base_request.get('posts', "", expected_error=False)
    ids = [item["id"] for item in res_list]
    return ids



@pytest.mark.parametrize("id", get_resources(), scope="module")
def test_update_all_resources(id):
     base_request = BaseRequest(BASE_URL_PETSTORE)
     body = {
         "id":"101",
         "title": "foo",
         "body": "bar",
         "userId": "1"
     }

     result = base_request.put(f'posts/{id}', "", body, expected_error=False)
     assert result is not None

def get_two_random_resources():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    res_list = base_request.get('posts', "", expected_error=False)
    ids = [item["id"] for item in res_list]
    id1 = random.choice(ids)
    id2 = random.choice(ids)
    return [id1,id2]

@pytest.mark.parametrize("id", get_two_random_resources(), scope="module")
def test_delete_random_resource(id):
    base_request = BaseRequest(BASE_URL_PETSTORE)
    result = base_request.delete(f'posts/{id}', "")
    assert result is not None


def test_get_nested_resources():
    base_request = BaseRequest(BASE_URL_PETSTORE)
    endpoint = 'posts/1/comments'
    result = base_request.get(endpoint, "", expected_error=False)
    emails = [item["email"] for item in result]
    assert "Eliseo@gardner.biz" in emails
    #assert result is not None

