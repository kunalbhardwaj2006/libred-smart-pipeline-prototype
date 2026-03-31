import asyncio
import json
import time

from async_pipeline import run_pipeline
from metrics import Metrics
from model_evaluator import evaluate_models


# ==============================
# 💾 SAVE METRICS FOR DASHBOARD
# ==============================
def save_metrics(metrics):
    data = {
        "total_requests": metrics.total_requests,
        "cache_hits": metrics.cache_hits,
        "cache_miss": metrics.cache_miss,
        "total_time": metrics.total_time,
        "cache_hit_rate": (
            (metrics.cache_hits / metrics.total_requests) * 100
            if metrics.total_requests > 0 else 0
        ),
    }

    with open("outputs/metrics.json", "w") as f:
        json.dump(data, f, indent=2)


# ==============================
# 🤖 SAVE MODEL EVALUATION
# ==============================
def save_model_results(results):
    with open("outputs/model_comparison.json", "w") as f:
        json.dump(results, f, indent=2)


# ==============================
# 🚀 MAIN PIPELINE RUNNER
# ==============================
async def main():
    print("\n🚀 Starting Smart Async Pipeline...\n")

    start_time = time.time()

    metrics = Metrics()

    # 🔥 Run async pipeline
    await run_pipeline(metrics)

    # 📊 Print metrics
    metrics.report()

    # 💾 Save metrics
    save_metrics(metrics)

    # ==========================
    # 🤖 Run Model Evaluation
    # ==========================
    print("\n🧠 Running Multi-Model Evaluation...\n")

    model_results = evaluate_models()

    save_model_results(model_results)

    print("✅ Model evaluation completed")

    # ==========================
    # ⏱️ Total execution time
    # ==========================
    total_time = time.time() - start_time
    print(f"\n⏱️ Total Execution Time: {round(total_time, 2)} seconds\n")

    print("🎯 Pipeline execution completed successfully!\n")


# ==============================
# ▶️ ENTRY POINT
# ==============================
if __name__ == "__main__":
    asyncio.run(main())
