import json
from pathlib import Path


class Metrics:
    def __init__(self):
        self.total_time = 0
        self.total_requests = 0
        self.cache_hits = 0
        self.cache_misses = 0

    def update_cache_metrics(self, cache_metrics):
        self.cache_hits = cache_metrics["cache_hits"]
        self.cache_misses = cache_metrics["cache_misses"]

    def to_dict(self):
        hit_rate = (
            (self.cache_hits / (self.cache_hits + self.cache_misses)) * 100
            if (self.cache_hits + self.cache_misses) > 0
            else 0
        )

        return {
            "total_requests": self.total_requests,
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "cache_hit_rate": round(hit_rate, 2),
            "total_time": round(self.total_time, 2),
        }

    def save(self):
        path = Path("outputs/metrics.json")
        path.parent.mkdir(exist_ok=True)

        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    def report(self):
        print("\n📊 FINAL METRICS REPORT")
        print("=" * 40)
        print(json.dumps(self.to_dict(), indent=2))
        print("=" * 40)
