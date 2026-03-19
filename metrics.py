class Metrics:
    def __init__(self):
        self.cache_hits = 0
        self.cache_miss = 0
        self.total_time = 0
        self.total_requests = 0

    def report(self):
        print("\n📊 FINAL METRICS REPORT")
        print("=" * 40)
        print(f"Total Requests: {self.total_requests}")
        print(f"Cache Hits: {self.cache_hits}")
        print(f"Cache Miss: {self.cache_miss}")

        hit_rate = (self.cache_hits / self.total_requests) * 100 if self.total_requests else 0
        print(f"Cache Hit Rate: {hit_rate:.2f}%")

        print(f"Total Processing Time: {self.total_time:.2f}s")
        print("=" * 40)