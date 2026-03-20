# 🧠 LibreED Smart Async Pipeline Prototype

A high-performance prototype inspired by LibreED that demonstrates **async processing, smart deduplication, batching, persistent caching, and lightweight AI-based classification**.

---

## 🚀 Problem Statement

The current LibreED pipeline faces challenges such as:

- Repeated processing of duplicate questions  
- High latency due to sequential LLM calls  
- Lack of caching → inefficient computation  
- Limited optimization for local environments  

---

## 💡 Proposed Solution

This prototype introduces:

- ⚡ **Async Processing Pipeline** → parallel execution  
- 🔥 **Batch Processing** → avoids sequential LLM calls  
- 🧠 **Text-based Deduplication** → removes duplicate questions intelligently  
- 💾 **Persistent Caching** → avoids re-processing previously seen questions  
- 🤖 **Lightweight Classification Engine** → simulates topic classification  
- 🧾 **Explanation Generation** → LLM-style output  
- 📊 **Metrics Tracking** → performance + cache efficiency  
- 🌐 **Streamlit Dashboard** → visualize results  

---

## ✨ Features

- ⚡ Async processing using `asyncio`  
- 🔥 Batch processing (parallel execution of tasks)  
- 🧠 Text-based deduplication (not ID-based)  
- 💾 File-based persistent caching  
- 🤖 Simulated AI classification  
- 🧾 Auto-generated explanations  
- 📊 Performance metrics (cache + timing + efficiency)  
- 🌐 Interactive dashboard using Streamlit  

---

## ⚡ Async Batching Insight

Instead of waiting for each question sequentially, the system:

- Processes multiple questions in parallel  
- Groups them into batches  
- Reduces total latency significantly  

This simulates how real-world LLM pipelines should work for scalability.

---

## ⚙️ Tech Stack

- Python 3.12  
- asyncio  
- Streamlit  
- JSON-based storage  

---

## 📂 Project Structure

libred-smart-pipeline-prototype/
│
├── async_pipeline.py
├── cache.py
├── metrics.py
├── main.py
├── app.py
│
├── sample_data/
│ └── questions.json
│
├── outputs/
│ ├── results.json
│ ├── metrics.json
│ └── cache.json
│
└── README.md


---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install streamlit
2. Run pipeline
python main.py
3. Run again (to see caching effect)
python main.py
4. Launch dashboard
streamlit run app.py
📊 Example Output
First Run:

❌ Cache MISS

⏳ Processing time ~1s

Second Run:

⚡ Cache HIT

🚀 Processing time ~0s

📈 Performance Impact
Metric	Before	After
Processing Time	High	Low
Redundant Calls	Yes	No
Cache Hit Rate	0%	100%
🔥 Why This Matters

This prototype demonstrates:

How repeated LLM calls can be avoided using caching

How async + batching improves performance

How local pipelines can be optimized for scalability

🚀 Future Improvements

Integrate real LLM (Ollama / OpenAI)

Async batching for real model inference

Replace mock classifier with semantic/embedding-based classification

Use better data sources (GFG / official exam portals)

Generate explanations using real LLMs

Extend beyond GATE to multiple exams

Integrate directly into LibreED codebase

🎥 Demo

👉 https://youtu.be/eq8tBfASgIA?si=P4bIGpdKZO6DS9Mj

⭐ Key Highlight

This prototype reduces repeated computation using persistent caching + async batching, making the system significantly more efficient and scalable.

---

