import asyncio
import time
import json
import os
from cache import cache_get, cache_set


# 🔥 SMART TEXT-BASED DEDUP
def deduplicate_questions(questions):
    seen = set()
    unique = []

    for idx, q in enumerate(questions):
        key = q["text"].strip().lower()
        if key not in seen:
            seen.add(key)
            q["id"] = f"q{idx+1}"
            unique.append(q)

    return unique


# 🧠 SUBJECT-AWARE CLASSIFIER
def classify_question(text, subject=None):
    if subject:
        mapping = {
            "OS": "Operating Systems",
            "DBMS": "Database Management Systems",
            "CN": "Computer Networks",
            "DSA": "Data Structures & Algorithms",
            "AI": "Artificial Intelligence"
        }
        return mapping.get(subject, "General Computer Science")

    return "General Computer Science"


# 🤖 REAL + FALLBACK LLM
def generate_explanation(question, topic):
    api_key = os.getenv("OPENAI_API_KEY")

    # 🔥 REAL LLM (if available)
    if api_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful computer science tutor."},
                    {"role": "user", "content": f"Explain briefly: {question}"}
                ],
                max_tokens=100
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"[LLM ERROR FALLBACK] {str(e)}"

    # ⚡ FALLBACK (Kaggle safe)
    return f"""
[LLM FALLBACK MODE]

Topic: {topic}

Explanation:
This question relates to {topic}. It tests conceptual understanding and is commonly asked in technical exams.

This fallback is used when API key is not available.
"""


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

    topic = classify_question(q["text"], q.get("subject"))

    result = {
        "id": q["id"],
        "question": q["text"],
        "topic": topic,
        "explanation": generate_explanation(q["text"], topic),
        "source": "multi-source",
        "exam": "generic",
        "model_used": "hybrid-llm"
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

    batch_size = 3
    batches = [questions[i:i + batch_size] for i in range(0, len(questions), batch_size)]

    results = []

    for batch in batches:
        batch_start = time.time()

        batch_tasks = [process_question(q, metrics) for q in batch]
        batch_results = await asyncio.gather(*batch_tasks)

        print(f"⚡ Batch processed in {time.time() - batch_start:.2f}s")

        results.extend(batch_results)

    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Results saved to outputs/results.json")