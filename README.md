# 🧠 LibreED Smart Async Pipeline Prototype

A high-performance prototype inspired by LibreED that demonstrates **async processing, smart deduplication, persistent caching, and lightweight AI-based classification**.

---

## 🚀 Problem Statement

The current LibreED pipeline faces challenges such as:

- Repeated processing of duplicate questions
- High latency due to repeated LLM calls
- Lack of caching → inefficient computation
- Limited performance optimization for local environments

---

## 💡 Proposed Solution

This prototype introduces:

- ⚡ **Async Processing Pipeline** → parallel execution  
- 🧠 **Text-based Deduplication** → removes duplicate questions intelligently  
- 💾 **Persistent Caching** → avoids re-processing previously seen questions  
- 🤖 **Lightweight Classification Engine** → simulates topic classification  
- 📊 **Metrics Tracking** → performance + cache efficiency  
- 🌐 **Streamlit Dashboard** → visualize results and performance  

---

## ✨ Features

- Async question processing using `asyncio`
- Text-based deduplication (not just ID-based)
- File-based caching (`cache.json`)
- Real-time performance metrics
- Clean UI dashboard using Streamlit

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

### 2. Run pipeline
python main.py

### 3. Run again (to see caching effect)
python main.py

### 4. Launch dashboard
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

This prototype demonstrates how:

Repeated LLM calls can be avoided using caching

Performance can be significantly improved on local machines

Data pipelines can be optimized for scalability

🚀 Future Improvements

Integrate real LLM (Ollama / OpenAI)

Advanced topic classification

Async batching for LLM calls

Support multiple exam streams

Improve frontend with React

🎥 Demo
https://youtu.be/eq8tBfASgIA?si=P4bIGpdKZO6DS9Mj

⭐ Key Highlight

This prototype reduces repeated computation using persistent caching, improving efficiency and making the system more scalable and cost-effective.


---

