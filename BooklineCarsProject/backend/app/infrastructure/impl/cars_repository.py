from app.utils.config import DATA_PATH

import json
import logging

async def read_json_cars_file():
    logging.debug("read_json_cars_file executting...")
    with open(DATA_PATH, 'r') as file:
        data = json.load(file)
    return data

async def write_json_cars_file(new_data):
    logging.debug("write_json_cars_file executting...")
    with open(DATA_PATH, 'r+') as f:
        data = json.load(f)
        data = new_data
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part