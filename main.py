import os
import json
import logging


def create_file_if_not_exists(cache_file):
    dir_path = os.path.dirname(cache_file)  # get directory path from filepath

    try:
        os.makedirs(dir_path)  # try creating directory path if not exists
    except FileExistsError:
        pass
        
    try:
        with open(cache_file, "x"):  # try creating file at the directory path if not exists
            pass
    except FileExistsError:
        pass


def load_from_cache(cache_file):
    # retrieve data for 'assistant_id' and 'thread_id' from cache if exists

    try:
        with open(cache_file, "r") as cache:
            data = json.load(cache)  # '.load()' is for file/object  # '.loads()' is for string
        return data
    except (FileNotFoundError, ValueError):
        return None
    

def save_to_cache(cache_file, default_assistant_id, default_thread_id):
    # if data for 'assistant_id' and 'thread_id' not exists, create new and save to cache

    create_file_if_not_exists(cache_file)

    data = {
        "assistant_id": default_assistant_id,
        "thread_id": default_thread_id
    }
    
    with open (cache_file, "w") as cache:
        json.dump(data, cache)  # '.dump()' is for file/object  # '.dumps()' is for string


log_file = "./log/log.log"
create_file_if_not_exists(log_file)

logging.basicConfig(level=logging.INFO, filename=log_file, filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

default_assistant_id = "ABC"
default_thread_id = "XYZ"
cache_file = "./cache/cache.json"

data = load_from_cache(cache_file)

try:
    assistant_id = data["assistant_id"]
    logging.info("Successfully retrieved data from cache")
except (TypeError, KeyError):
    assistant_id = None
    logging.error("Cache file not found or corrupted. Creating new one...")

try:
    thread_id = data["thread_id"]
    logging.info("Successfully retrieved data from cache")
except (TypeError, KeyError):
    thread_id = None
    logging.error("Cache file not found or corrupted. Creating new one...")

if not assistant_id or not thread_id:
    save_to_cache(cache_file, default_assistant_id, default_thread_id)

print(assistant_id)
print(thread_id)
