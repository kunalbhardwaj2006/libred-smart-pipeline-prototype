import asyncio
import json
from async_pipeline import run_pipeline
from metrics import Metrics


# 💾 SAVE METRICS FOR FRONTEND
def save_metrics(metrics):
    data = {
        "total_requests": metrics.total_requests,
        "cache_hits": metrics.cache_hits,
        "cache_miss": metrics.cache_miss,
        "total_time": metrics.total_time,
        "cache_hit_rate": (
            metrics.cache_hits / metrics.total_requests * 100
            if metrics.total_requests > 0 else 0
        )
    }

    with open("outputs/metrics.json", "w") as f:
        json.dump(data, f, indent=2)


# 🚀 MAIN PIPELINE RUNNER
async def main():
    print("🚀 Starting Smart Async Pipeline...\n")

    metrics = Metrics()

    await run_pipeline(metrics)

    metrics.report()

    # ✅ Save metrics for Streamlit dashboard
    save_metrics(metrics)


# ▶️ ENTRY POINT
if __name__ == "__main__":
    asyncio.run(main())