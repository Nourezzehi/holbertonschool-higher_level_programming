#!/usr/bin/python3
"""object in text file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, "w") as filename:
        filename.write(json.dumps(my_obj))
