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


# 🚀 PROCESS QUESTION
async def process_question(q, metrics):
    start = time.time()
    metrics.total_requests += 1

    cached = cache_get(q["id"])
    if cached:
        print(f"⚡ Cache HIT for {q['id']}")
        metrics.cache_hits += 1
        return cached

    print(f"❌ Cache MISS for {q['id']}")

    await asyncio.sleep(0.5)

    result = {
        "id": q["id"],
        "question": q["text"],
        "topic": classify_question(q["text"])
    }

    cache_set(q["id"], result)

    metrics.cache_miss += 1
    metrics.total_time += time.time() - start

    return result


# 🔥 MAIN PIPELINE
async def run_pipeline(metrics):

    with open("sample_data/questions.json") as f:
        questions = json.load(f)

    print(f"\n📥 Total Input Questions: {len(questions)}")

    questions = deduplicate_questions(questions)

    print(f"🧠 Unique Questions After Dedup: {len(questions)}\n")

    # ✅ FIXED ASYNC TASK CREATION
    tasks = []
    for q in questions:
        tasks.append(process_question(q, metrics))

    results = await asyncio.gather(*tasks)

    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Results saved to outputs/results.json")