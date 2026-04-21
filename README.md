# 🧠 LibreED Smart Async Pipeline Prototype

A production-oriented prototype inspired by **LibreED** that demonstrates a **scalable async execution system, intelligent caching, and optimized LLM pipeline design**.

This project is built as a **Proof of Concept (PoC)** for improving the LibreED generator pipeline for **GSoC 2026**.

---

## 🔬 Kaggle Validation (Mentor-Ready Proof)

This prototype has been validated on a Kaggle notebook using multi-subject datasets.

### ✅ What was tested:
- Full async pipeline execution
- Cache behavior (MISS → HIT)
- Multi-subject support (OS, DBMS, CN, DSA, AI)
- LLM fallback handling
- Execution time tracking

### 📊 Key Results:
- First run → Cache MISS + full processing
- Second run → Cache HIT (near-instant)
- Async batching significantly reduced latency
- Logs + execution time recorded

👉 Kaggle Notebook: https://www.kaggle.com/code/kbkunalbhardwaj/notebook0ca800adc7  
👉 Demo Video: https://youtu.be/JBgsLNsxZEM

---

## 🚀 Problem Statement

While working with the LibreED pipeline, the following real-world bottlenecks were observed:

- ❌ Sequential LLM execution → high latency  
- ❌ Repeated LLM calls → redundant computation  
- ❌ No caching → wasted resources  
- ❌ Poor scalability for large datasets  
- ❌ Tight coupling of pipeline stages  

These issues make the system inefficient for **real-world educational workloads**.

---

## 💡 Proposed Solution

This prototype introduces a **system-level execution redesign**:

### ⚡ Core Improvements

- **Async Batch Processing** → parallel execution using `asyncio`  
- **Persistent Caching** → eliminates repeated LLM calls  
- **Smart Deduplication** → avoids duplicate processing  
- **Decoupled Pipeline Stages** → better scalability  
- **Metrics Tracking** → performance visibility  
- **Extensible LLM Interface (Mock → Real-ready)**  

---

## 🧠 Key Idea

Instead of optimizing individual steps, this project transforms the pipeline into a:

> **Resource-aware, scalable execution system**

Where:
- Tasks run in parallel  
- Results are reused  
- Computation is minimized  

---

## ⚙️ Tech Stack

- Python 3.12  
- asyncio (parallel execution)  
- JSON (lightweight storage)  
- Streamlit (visualization)  

---

## ⚡ Async Execution Insight

Traditional pipeline:
Task1 → Task2 → Task3 → Task4


Optimized pipeline:

(Task1, Task2, Task3, Task4) → Parallel Execution


✔ Reduces idle waiting time  
✔ Maximizes CPU/API usage  
✔ Improves throughput  

---

## 💾 Caching Strategy

- Hash-based cache key: `hash(question_text)`  
- Read-before-write approach  
- Persistent storage (`cache.json`)  

### Result:

| Run | Behavior |
|-----|--------|
| First Run | ❌ Cache MISS |
| Second Run | ⚡ Cache HIT |

---

## 📊 Performance Impact

| Metric | Before | After |
|------|-------|------|
| Execution Time | High | Low |
| LLM Calls | Repeated | Eliminated |
| Cache Hit Rate | 0% | ~100% |
| Scalability | Poor | High |

---

## 🧪 Kaggle Validation (Important)

This prototype was **validated on a Kaggle Notebook** to simulate real-world execution:

✔ Full pipeline execution  
✔ Cache MISS → HIT behavior  
✔ Execution logs + timing  
✔ Multi-subject scalability test  

👉 Notebook:  
https://www.kaggle.com/code/kbkunalbhardwaj/notebook0ca800adc7

---

## 📂 Project Structure


libred-smart-pipeline-prototype/
│
├── async_pipeline.py # Async execution engine
├── cache.py # Persistent caching system
├── metrics.py # Performance tracking
├── main.py # Pipeline entry point
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
2. Run pipeline (first run)
python main.py
3. Run again (observe caching)
python main.py
4. Launch dashboard
streamlit run app.py
📊 Sample Output
First Run:
❌ Cache MISS
⏳ Processing time ~1s
Second Run:
⚡ Cache HIT
🚀 Processing time ~0s
🎥 Demo

👉 https://youtu.be/JBgsLNsxZEM

✔ Shows:

Pipeline execution
Cache behavior
LibreED UI integration
AI-generated explanations
🔗 Alignment with LibreED

This prototype directly aligns with LibreED goals:

Improves generator pipeline performance
Reduces LLM latency bottleneck
Removes dependency on external explanation sources
Supports future TypeScript migration
🚀 Future Improvements
Integrate real LLMs (OpenAI / Ollama)
Async batching for real inference
Multi-model selection system
Better data sources (GFG / official portals)
Full integration into LibreED generator
TypeScript async pipeline prototype
⭐ Key Highlight

This project is not just a prototype — it is a validated execution strategy for building scalable LLM pipelines.

📌 Why This Matters

This approach can be applied to:

Educational platforms
Document processing systems
AI content generation pipelines

Making it a reusable architecture beyond LibreED.

👨‍💻 Author

Kunal Bhardwaj
GSoC 2026 Contributor (AOSSIE - LibreED)

GitHub: https://github.com/kunalbhardwaj2006


---