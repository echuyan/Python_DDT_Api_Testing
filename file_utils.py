import os
import csv


def get_full_file_path(path_ending):
    base_path = os.path.dirname(__file__)
    full_file_path = os.path.join(base_path, path_ending)
    return full_file_path


def read_csv_file(path_ending):
    full_file_path = get_full_file_path(path_ending)
    with open(full_file_path, "r") as csv_file:
        rows = csv.DictReader(csv_file)
        for row in rows:
            yield row


def read_lines_csv_file(path_ending, lime_counts=5):
    result = []
    for line in read_csv_file(path_ending):
        result.append(line)
        if len(result) == lime_counts:
            return result
    raise ValueError(f'File {path_ending} has less than {lime_counts} lines')