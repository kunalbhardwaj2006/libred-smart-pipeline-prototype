import asyncio
import time
import json
from cache import cache_get, cache_set


# 🔥 SMART TEXT-BASED DEDUP
def deduplicate_questions(questions):
    seen = set()
    unique = []

    for idx, q in enumerate(questions):
        key = q["text"].strip().lower()
        if key not in seen:
            seen.add(key)

            # assign new ID
            q["id"] = f"q{idx+1}"
            unique.append(q)

    return unique


# 🧠 SIMPLE CLASSIFIER
def classify_question(text):
    text = text.lower()

    if "os" in text:
        return "Operating Systems"
    elif "dbms" in text:
        return "Database Management Systems"
    elif "network" in text:
        return "Computer Networks"
    elif "algorithm" in text:
        return "Algorithms"
    else:
        return "General Computer Science"


# 🤖 EXPLANATION GENERATOR
def generate_explanation(question, topic):
    return f"This question is classified under {topic} because it involves concepts related to {topic}."


# 🚀 PROCESS QUESTION (ASYNC)
async def process_question(q, metrics):
    start = time.time()
    metrics.total_requests += 1

    # ⚡ CACHE CHECK
    cached = cache_get(q["id"])
    if cached:
        print(f"⚡ Cache HIT for {q['id']}")
        metrics.cache_hits += 1
        return cached

    print(f"❌ Cache MISS for {q['id']}")

    # ⏳ Simulate delay (LLM)
    await asyncio.sleep(0.5)

    topic = classify_question(q["text"])

    result = {
    "id": q["id"],
    "question": q["text"],
    "topic": topic,
    "explanation": generate_explanation(q["text"], topic),
    "source": "multi-source",   # ✅ FIXED
    "exam": "generic",          # ✅ FIXED
    "model_used": "mock-llama"
    }

    # 💾 SAVE CACHE
    cache_set(q["id"], result)

    metrics.cache_miss += 1
    metrics.total_time += time.time() - start

    return result


# 🔥 MAIN PIPELINE (ASYNC)
async def run_pipeline(metrics):

    # 📂 LOAD QUESTIONS
    with open("sample_data/questions.json") as f:
        questions = json.load(f)

    print(f"\n📥 Total Input Questions: {len(questions)}")

    # 🔥 DEDUP
    questions = deduplicate_questions(questions)

    print(f"🧠 Unique Questions After Dedup: {len(questions)}\n")

    # 🔥 BATCHING
    batch_size = 2
    batches = [questions[i:i + batch_size] for i in range(0, len(questions), batch_size)]

    results = []

    # ✅ EVERYTHING BELOW IS INSIDE FUNCTION (IMPORTANT)
    for batch in batches:
        batch_start = time.time()

        batch_tasks = [process_question(q, metrics) for q in batch]
        batch_results = await asyncio.gather(*batch_tasks)

        batch_time = time.time() - batch_start
        print(f"⚡ Batch processed in {batch_time:.2f}s")

        results.extend(batch_results)

    # 💾 SAVE OUTPUT
    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Results saved to outputs/results.json")