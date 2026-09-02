import json
from typing import TextIO


def json_export(kwargs: dict) -> None:
    return json.dump(kwargs, open('json_file.json', 'w'))

def json_import(file: TextIO) -> dict:
    return json.load(file)