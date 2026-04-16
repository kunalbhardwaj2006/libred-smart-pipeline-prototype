import os
import asyncio
import requests

# Optional OpenAI
try:
    from openai import OpenAI
except:
    OpenAI = None

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# -----------------------------
# 🔥 OPENAI
# -----------------------------
async def generate_openai(prompt):
    if not OPENAI_API_KEY or OpenAI is None:
        raise Exception("OpenAI not available")

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful CS tutor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


# -----------------------------
# 🔥 OLLAMA
# -----------------------------
async def generate_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        return response.json()["response"]

    except Exception:
        raise Exception("Ollama failed")


# -----------------------------
# 🧠 AUTO FALLBACK (KEY FEATURE)
# -----------------------------
async def generate_explanation_llm(question, topic):
    prompt = f"""
Explain the following question clearly:

Question: {question}
Topic: {topic}

Give a simple and structured explanation.
"""

    # 1️⃣ Try OpenAI
    try:
        result = await generate_openai(prompt)
        return f"[OPENAI] {result}"
    except Exception:
        print("⚠️ OpenAI failed, trying Ollama...")

    # 2️⃣ Try Ollama
    try:
        result = await generate_ollama(prompt)
        return f"[OLLAMA] {result}"
    except Exception:
        print("⚠️ Ollama failed, using mock...")

    # 3️⃣ Fallback MOCK
    return f"[MOCK] Explanation for {topic}: {question}"


# -----------------------------
# ⚡ BATCH PROCESSING
# -----------------------------
async def generate_batch_explanations(questions_with_topics):
    tasks = [
        generate_explanation_llm(q["text"], q["topic"])
        for q in questions_with_topics
    ]

    return await asyncio.gather(*tasks) 