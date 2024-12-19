from app.utils.config import DATA_PATH

import json

async def read_json_cars_file():
    with open(DATA_PATH, 'r') as file:
        data = json.load(file)
    return data

async def write_json_cars_file():
    return None