import random
import string

from .file_utils import read_lines_csv_file


def gen_users(user_count=5):
    for user_id in range(user_count):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        input_pattern = f'{random_string}_{user_id}'
        yield {
            "id": 0,
            "username": input_pattern,
            "firstName": input_pattern,
            "lastName": input_pattern,
            "email": input_pattern,
            "password": input_pattern,
            "phone": input_pattern,
            "userStatus": random.randint(0, 10)
        }


def get_list_of_users(size=5):
    return list(gen_users(size))


def get_list_of_users_from_csv_file(file_name, size=5):
    return read_lines_csv_file(file_name, size)


def get_param_list_error_users(file_name, size=5):
    result = []
    for line in read_lines_csv_file(file_name, size):
        error_msg = line.pop('errorMessage')
        result.append((line, error_msg))
    return result
