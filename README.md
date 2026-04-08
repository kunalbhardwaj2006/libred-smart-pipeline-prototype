# 🧠 LibreED Smart Async Pipeline Prototype

A high-performance prototype inspired by LibreED that demonstrates **async processing, smart deduplication, batching, persistent caching, and performance-aware pipeline design**.

---

## 🚀 Problem Statement

The current LibreED pipeline faces key bottlenecks:

- ⏳ High latency due to **sequential LLM calls**
- 🔁 Repeated processing of duplicate questions
- ❌ No caching → redundant computation
- 🐢 Poor scalability for large datasets

---

## 💡 Proposed Solution

This prototype introduces a **scalable pipeline architecture** with:

- ⚡ Async Processing → parallel execution
- 🔥 Batch Processing → avoids sequential blocking
- 🧠 Smart Deduplication → prevents duplicate processing
- 💾 Persistent Caching → avoids repeated LLM calls
- 📊 Metrics Tracking → measures system performance
- 🌐 Streamlit Dashboard → visualizes results

---

## 🧪 Key Enhancements (Mentor-Aligned)

This PoC directly addresses core system challenges:

### ✅ 1. Reduce LLM Dependency
- Simulated classification + explanation pipeline
- Designed to plug into real LLM later

### ✅ 2. Improve Pipeline Speed
- Async batching eliminates sequential bottlenecks
- Parallel execution reduces latency

### ✅ 3. Caching for Efficiency
- File-based persistent cache (`cache.json`)
- Prevents recomputation across runs

### ✅ 4. Observability (NEW 🔥)
- Cache hit/miss tracking
- Cache hit rate calculation
- Total execution time tracking

---

## ⚡ Async Batching Insight

Instead of:
Q1 → wait → Q2 → wait → Q3

We do:

(Q1, Q2, Q3) → processed in parallel


✔ Reduces total runtime  
✔ Improves throughput  
✔ Matches real-world LLM pipelines  

---

## 💾 Caching System (NEW 🔥)

- Stores processed results in `outputs/cache.json`
- Uses question ID as key
- Tracks:

  - Cache Hits  
  - Cache Misses  
  - Cache Hit Rate (%)  

### 📊 Example:

| Run | Cache Hit Rate | Time |
|-----|--------------|------|
| First Run | 0% | High |
| Second Run | ~100% | Near Instant |

---

## 📊 Metrics Tracking (NEW 🔥)

Metrics are saved in:

✔ Reduces total runtime  
✔ Improves throughput  
✔ Matches real-world LLM pipelines  

---

## 💾 Caching System (NEW 🔥)

- Stores processed results in `outputs/cache.json`
- Uses question ID as key
- Tracks:

  - Cache Hits  
  - Cache Misses  
  - Cache Hit Rate (%)  

### 📊 Example:

| Run | Cache Hit Rate | Time |
|-----|--------------|------|
| First Run | 0% | High |
| Second Run | ~100% | Near Instant |

---

## 📊 Metrics Tracking (NEW 🔥)

Metrics are saved in:
outputs/metrics.json


Includes:

- Total Requests
- Cache Hits
- Cache Misses
- Cache Hit Rate (%)
- Total Execution Time

---

## 🌐 Dashboard (Streamlit)

Interactive dashboard shows:

- Questions + classification
- Cache performance
- System efficiency insights

---

## ⚙️ Tech Stack

- Python 3.12  
- asyncio  
- Streamlit  
- JSON storage  

---

## 📂 Project Structure
libred-smart-pipeline-prototype/
│
├── async_pipeline.py # async batching logic
├── cache.py # caching + hit/miss tracking
├── metrics.py # performance metrics
├── main.py # pipeline runner
├── app.py # Streamlit dashboard
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
3. Run again (observe caching 🚀)
python main.py
4. Launch dashboard
streamlit run app.py
📊 Example Output
First Run:
❌ Cache MISS
⏳ Higher processing time
Second Run:
⚡ Cache HIT
🚀 Near-zero processing time
🔥 Performance Impact
Metric	Before	After
Processing Time	High	Low
Redundant Calls	Yes	No
Cache Usage	❌	✅
Scalability	Low	High
🎯 Why This Matters

This prototype shows:

How LLM cost & latency can be reduced
How async + batching improves scalability
How caching dramatically improves performance
How to build production-ready pipelines
🚀 Future Improvements
🔗 Integrate real LLM (Ollama / OpenAI)
⚡ Async batching for real model inference
🧠 Semantic/embedding-based classification
📚 Better data sources (official PYQs)
🧾 Real explanation generation via LLM
📊 Advanced metrics (latency per batch)
🔄 Integration into LibreED pipeline
🎥 Demo

👉 https://youtu.be/eq8tBfASgIA?si=P4bIGpdKZO6DS9Mj

⭐ Key Highlight

This prototype demonstrates how async processing + caching + metrics tracking can transform a slow sequential pipeline into a fast, scalable, and efficient system 
