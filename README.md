# 🧠 LibrEd Smart Async Pipeline Prototype

A high-performance prototype inspired by LibrEd that demonstrates **async processing, intelligent deduplication, batching, persistent caching, and scalable AI-based classification pipelines**.

---

## 🚀 Problem Statement

The current LibrEd generator pipeline faces key challenges:

- ❌ Repeated processing of duplicate questions  
- ⏳ High latency due to sequential LLM calls  
- 🔁 No caching → redundant computation  
- 🐢 Limited optimization for local execution environments  

These issues slow down the pipeline and limit scalability for large datasets.

---

## 💡 Proposed Solution

This prototype introduces a **scalable and optimized pipeline design**:

- ⚡ **Async Processing Pipeline** → parallel execution  
- 🔥 **Batch Processing** → avoids sequential LLM calls  
- 🧠 **Text-based Deduplication** → detects duplicates intelligently  
- 💾 **Persistent Caching** → skips already processed inputs  
- 🤖 **Lightweight Classification Engine** → simulates LLM classification  
- 🧾 **Explanation Generation** → LLM-style outputs  
- 📊 **Performance Metrics** → tracks efficiency  
- 🌐 **Streamlit Dashboard** → visualizes pipeline behavior  

---

## ⚡ Key Insight: Async Batching

Instead of processing one question at a time:

- Questions are grouped into batches  
- Multiple batches are processed in parallel  
- System avoids waiting for each response sequentially  

👉 This is critical for scaling real-world LLM pipelines.

---

## 📊 Performance Benchmark

| Metric           | Sequential Pipeline | Async + Cache Pipeline |
|------------------|--------------------|------------------------|
| Processing Time  | High               | Significantly Reduced  |
| Redundant Calls  | Yes                | Eliminated             |
| Cache Hit Rate   | 0%                 | Up to 100%             |
| Scalability      | Limited            | High                   |

### 🚀 Observations
- Async batching significantly reduces latency  
- Caching eliminates repeated computation  
- Pipeline improves further on repeated runs  

---

## 🧠 Model Evaluation (Planned + Simulated)

| Model       | Accuracy | Speed | Suitability |
|------------|---------|------|------------|
| LLaMA 3.1  | Medium  | Slow | Baseline   |
| Mistral    | High    | Fast | Recommended |
| Phi-3      | Medium  | Fast | Lightweight |

👉 This will be extended to real benchmarking using local LLMs (Ollama).

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
├── src/
│   ├── async_pipeline.py
│   ├── model_evaluator.py
│   ├── cache_manager.py
│   ├── data_source.py
│
├── results/
│   ├── benchmarks.json
│   ├── model_comparison.json
│
├── demo/
│   ├── sample_output.json
│
├── README.md


---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install streamlit
2. Run pipeline
python main.py
3. Run again (to observe caching impact)
python main.py
4. Launch dashboard
streamlit run app.py
📊 Sample Execution
Processing 50 questions...
Batch size: 5
Async workers: 5

[✔] Batch 1 completed in 2.1s
[✔] Batch 2 completed in 1.8s
[✔] Cached responses reused: 12

Total execution time: ~34s
🔗 Relevance to LibrEd

This prototype directly aligns with LibrEd’s improvement goals:

Reduces LLM latency using async batching
Eliminates redundant computation via caching
Improves scalability for large datasets
Enables efficient local execution
Supports multi-model evaluation

👉 Designed for direct integration into the LibrEd generator pipeline.

🚧 Future Improvements
Integrate real LLMs (Ollama, Mistral, etc.)
Async batching for real model inference
Replace mock classifier with embedding-based classification
Use better data sources (GFG / official portals)
Generate explanations using LLMs instead of external sources
Extend beyond GATE (multi-exam support)
Integrate fully into LibrEd pipeline
🎥 Demo

👉 https://youtu.be/eq8tBfASgIA?si=P4bIGpdKZO6DS9Mj

⭐ Key Highlight

This prototype shows how:

⚡ Async batching reduces execution time
🔁 Caching removes redundant computation
📈 System becomes scalable and efficient

👉 Making LLM-based pipelines practical for real-world usage.
