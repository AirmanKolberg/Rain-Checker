import json


def json_to_dict(json_location):

    with open(json_location) as f:
        data = json.load(f)

    return data


def dict_to_json(dictionary, json_location):

    with open(json_location, 'w') as json_file:
        json.dump(dictionary, json_file)


if __name__ == '__main__':
    
    pass
