import json
import os
import logging

CACHE_FILE = "outputs/cache.json"

# Setup logger
logger = logging.getLogger(__name__)

# Metrics (global for prototype simplicity)
CACHE_HITS = 0
CACHE_MISSES = 0


def load_cache():
    """Load cache from file."""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            logger.warning("Cache file corrupted. Resetting cache.")
            return {}
    return {}


def save_cache(cache):
    """Persist cache to file."""
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


# Load once
CACHE = load_cache()


def cache_get(key):
    """Retrieve value from cache and track metrics."""
    global CACHE_HITS, CACHE_MISSES

    if key in CACHE:
        CACHE_HITS += 1
        logger.debug(f"Cache HIT for key: {key[:50]}")
        return CACHE[key]
    else:
        CACHE_MISSES += 1
        logger.debug(f"Cache MISS for key: {key[:50]}")
        return None


def cache_set(key, value):
    """Store value in cache."""
    CACHE[key] = value
    save_cache(CACHE)
    logger.debug(f"Cache SET for key: {key[:50]}")


def get_cache_metrics():
    """Return cache performance metrics."""
    total = CACHE_HITS + CACHE_MISSES
    hit_rate = (CACHE_HITS / total) * 100 if total else 0

    return {
        "cache_hits": CACHE_HITS,
        "cache_misses": CACHE_MISSES,
        "cache_hit_rate": round(hit_rate, 2),
    }
