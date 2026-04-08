import json
import time

from cache import cache_get, cache_set, get_cache_metrics
from metrics import Metrics


# 🔹 Example dummy LLM function (replace with your actual logic)
def process_question(question):
    """
    Simulates processing (LLM call or classification).
    Replace this with your real pipeline logic.
    """
    return {
        "question": question,
        "topic": "Sample Topic"
    }


def run_pipeline(questions):
    results = []

    for q in questions:
        # Track total requests
        metrics.total_requests += 1

        # 🔹 Check cache first
        cached = cache_get(q)

        if cached:
            results.append(cached)
            continue

        # 🔹 Process if not cached
        output = process_question(q)

        # 🔹 Save to cache
        cache_set(q, output)

        results.append(output)

    return results


if __name__ == "__main__":
    start_time = time.time()

    # 🔹 Initialize metrics
    metrics = Metrics()

    # 🔹 Sample input (replace with your dataset/PDF input)
    questions = [
        "What is AI?",
        "Explain machine learning",
        "What is AI?",  # duplicate to test cache
    ]

    # 🔹 Run pipeline
    results = run_pipeline(questions)

    # 🔹 Save results
    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    # 🔹 Measure total time
    metrics.total_time = time.time() - start_time

    # 🔹 Get cache metrics
    cache_metrics = get_cache_metrics()
    metrics.update_cache_metrics(cache_metrics)

    # 🔹 Save + print metrics
    metrics.save()
    metrics.report()
