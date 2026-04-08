import asyncio
import time
import json

from async_pipeline import run_pipeline
from cache import get_cache_metrics
from metrics import Metrics


if __name__ == "__main__":
    start_time = time.time()

    metrics = Metrics()

    # 🔥 Run async pipeline
    asyncio.run(run_pipeline(metrics))

    # ⏱️ total time
    metrics.total_time = time.time() - start_time

    # 📊 cache metrics
    cache_metrics = get_cache_metrics()
    metrics.update_cache_metrics(cache_metrics)

    # 💾 save + print
    metrics.save()
    metrics.report()
