import json


def get_data_from_json(path):

    with open(path, 'r') as file:
        json_data = json.load(file)

    return json_data
