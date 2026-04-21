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


# 🤖 ASYNC LLM (OpenAI → Ollama → Mock)
async def generate_explanation_async(question, topic):

    # ✅ 1. Try OpenAI
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        try:
            from openai import AsyncOpenAI
            client = AsyncOpenAI(api_key=api_key)

            response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful CS tutor."},
                    {"role": "user", "content": f"Explain briefly: {question}"}
                ],
                max_tokens=120
            )

            return response.choices[0].message.content

        except Exception as e:
            print("⚠️ OpenAI failed:", e)

    # ✅ 2. Try Ollama (local)
    try:
        import aiohttp

        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": f"Explain: {question}",
                    "stream": False
                }
            ) as res:
                data = await res.json()
                return f"[OLLAMA] {data.get('response', '')}"

    except Exception as e:
        print("⚠️ Ollama failed:", e)

    # ✅ 3. Final fallback (Kaggle safe)
    return f"""
[MOCK FALLBACK]

Topic: {topic}

Explanation:
This question relates to {topic}. It tests fundamental concepts commonly asked in exams.
"""


# 🚀 PROCESS QUESTION (FULLY ASYNC)
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

    topic = classify_question(q["text"], q.get("subject"))

    # 🔥 ASYNC LLM CALL
    explanation = await generate_explanation_async(q["text"], topic)

    result = {
        "id": q["id"],
        "question": q["text"],
        "topic": topic,
        "explanation": explanation,
        "source": "multi-source",
        "exam": "generic",
        "model_used": "openai/ollama/mock-auto"
    }

    # 💾 CACHE SAVE
    cache_set(q["id"], result)

    metrics.cache_miss += 1
    metrics.total_time += time.time() - start

    return result


# 🔥 MAIN PIPELINE
async def run_pipeline(metrics):

    with open("sample_data/questions.json") as f:
        questions = json.load(f)

    print(f"\n📥 Total Input Questions: {len(questions)}")

    # 🔥 DEDUP
    questions = deduplicate_questions(questions)
    print(f"🧠 Unique Questions After Dedup: {len(questions)}\n")

    # 🔥 BATCHING
    batch_size = 4
    batches = [questions[i:i + batch_size] for i in range(0, len(questions), batch_size)]

    results = []

    for batch in batches:
        batch_start = time.time()

        tasks = [process_question(q, metrics) for q in batch]
        batch_results = await asyncio.gather(*tasks)

        print(f"⚡ Batch processed in {time.time() - batch_start:.2f}s")

        results.extend(batch_results)

    # 💾 SAVE OUTPUT
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Results saved to outputs/results.json")