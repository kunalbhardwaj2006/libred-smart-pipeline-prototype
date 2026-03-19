import json
import os

CACHE_FILE = "outputs/cache.json"


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


# Load once
CACHE = load_cache()


def cache_get(key):
    return CACHE.get(key)


def cache_set(key, value):
    CACHE[key] = value
    save_cache(CACHE)