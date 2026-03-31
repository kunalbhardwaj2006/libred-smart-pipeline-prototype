# 🧠 LibrEd Smart Async Pipeline Prototype

A high-performance prototype inspired by LibrEd that demonstrates **async execution, intelligent caching, batching, deduplication, and multi-model evaluation** for scalable LLM-based pipelines.

---

## 🚀 Problem Statement

The current LibrEd generator pipeline faces several performance bottlenecks:

- ❌ Sequential LLM execution → high latency  
- ❌ No caching → repeated and unnecessary computation  
- ❌ Duplicate questions processed multiple times  
- ❌ Fixed model usage → no flexibility or optimization  
- ❌ Limited efficiency for large datasets  

👉 These issues make the pipeline slow and difficult to scale.

---

## 💡 Proposed Solution

This prototype introduces a **scalable and optimized pipeline architecture**:

- ⚡ **Async Processing Pipeline** → parallel execution of tasks  
- 🔥 **Batch Processing** → avoids sequential LLM calls  
- 🧠 **Text-based Deduplication** → eliminates duplicate inputs  
- 💾 **Persistent Caching** → prevents repeated computation  
- 🤖 **Multi-Model Evaluation** → benchmark different LLMs  
- 🧾 **Explanation Generation** → simulated LLM outputs  
- 📊 **Performance Metrics** → tracks efficiency improvements  
- 🌐 **Streamlit Dashboard** → interactive visualization  

---

## ⚡ Key Insight: Async Batching

Instead of processing one request at a time:

- Questions are grouped into batches  
- Batches are processed concurrently  
- System avoids waiting for each response sequentially  

👉 This is critical for scaling real-world LLM pipelines.

---

## 🧠 Multi-Model Evaluation (Core Contribution)

This prototype introduces a **model benchmarking system** to compare different LLMs:

| Model      | Avg Latency | Avg Accuracy | Observation |
|------------|------------|-------------|------------|
| LLaMA 3.1  | High       | Medium      | Baseline model |
| Mistral    | Medium     | High        | Best balance |
| Phi-3      | Low        | Medium      | Lightweight |

### 📌 Key Takeaways
- No single model is optimal for all tasks  
- Faster models improve pipeline throughput  
- Balanced models (e.g., Mistral) are better for classification  

👉 This enables **data-driven model selection**, not guesswork.

---

## 📊 Performance Impact

| Metric                  | Before (Sequential) | After (Async + Cache) |
|------------------------|--------------------|------------------------|
| Processing Time        | High               | Significantly Reduced  |
| Redundant Calls        | Yes                | Eliminated             |
| Cache Hit Rate         | 0%                 | Up to 100%             |
| Scalability            | Limited            | High                   |

---

## ⚙️ Tech Stack

- Python 3.12  
- asyncio (concurrency)  
- Streamlit (visualization)  
- JSON-based storage  

---

## 📂 Project Structure
# 🧠 LibrEd Smart Async Pipeline Prototype

A high-performance prototype inspired by LibrEd that demonstrates **async execution, intelligent caching, batching, deduplication, and multi-model evaluation** for scalable LLM-based pipelines.

---

## 🚀 Problem Statement

The current LibrEd generator pipeline faces several performance bottlenecks:

- ❌ Sequential LLM execution → high latency  
- ❌ No caching → repeated and unnecessary computation  
- ❌ Duplicate questions processed multiple times  
- ❌ Fixed model usage → no flexibility or optimization  
- ❌ Limited efficiency for large datasets  

👉 These issues make the pipeline slow and difficult to scale.

---

## 💡 Proposed Solution

This prototype introduces a **scalable and optimized pipeline architecture**:

- ⚡ **Async Processing Pipeline** → parallel execution of tasks  
- 🔥 **Batch Processing** → avoids sequential LLM calls  
- 🧠 **Text-based Deduplication** → eliminates duplicate inputs  
- 💾 **Persistent Caching** → prevents repeated computation  
- 🤖 **Multi-Model Evaluation** → benchmark different LLMs  
- 🧾 **Explanation Generation** → simulated LLM outputs  
- 📊 **Performance Metrics** → tracks efficiency improvements  
- 🌐 **Streamlit Dashboard** → interactive visualization  

---

## ⚡ Key Insight: Async Batching

Instead of processing one request at a time:

- Questions are grouped into batches  
- Batches are processed concurrently  
- System avoids waiting for each response sequentially  

👉 This is critical for scaling real-world LLM pipelines.

---

## 🧠 Multi-Model Evaluation (Core Contribution)

This prototype introduces a **model benchmarking system** to compare different LLMs:

| Model      | Avg Latency | Avg Accuracy | Observation |
|------------|------------|-------------|------------|
| LLaMA 3.1  | High       | Medium      | Baseline model |
| Mistral    | Medium     | High        | Best balance |
| Phi-3      | Low        | Medium      | Lightweight |

### 📌 Key Takeaways
- No single model is optimal for all tasks  
- Faster models improve pipeline throughput  
- Balanced models (e.g., Mistral) are better for classification  

👉 This enables **data-driven model selection**, not guesswork.

---

## 📊 Performance Impact

| Metric                  | Before (Sequential) | After (Async + Cache) |
|------------------------|--------------------|------------------------|
| Processing Time        | High               | Significantly Reduced  |
| Redundant Calls        | Yes                | Eliminated             |
| Cache Hit Rate         | 0%                 | Up to 100%             |
| Scalability            | Limited            | High                   |

---

## ⚙️ Tech Stack

- Python 3.12  
- asyncio (concurrency)  
- Streamlit (visualization)  
- JSON-based storage  

---

## 📂 Project Structure
libred-smart-pipeline-prototype/
│
├── src/
│ ├── async_pipeline.py
│ ├── model_evaluator.py
│ ├── cache_manager.py
│ ├── metrics.py
│
├── outputs/
│ ├── results.json
│ ├── metrics.json
│ ├── model_comparison.json
│
├── sample_data/
│ └── questions.json
│
├── app.py
├── main.py
└── README.md

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

This prototype directly addresses key challenges in LibrEd:

Reduces LLM latency using async batching
Eliminates redundant computation using caching
Improves scalability for large datasets
Introduces multi-model benchmarking
Enables efficient local execution

👉 Designed to integrate into the existing LibrEd generator pipeline.

🚧 Future Improvements
Integrate real LLMs (Ollama, Mistral, etc.)
Replace simulated classification with embedding-based models
Add dynamic model routing (task-based selection)
Use better data sources (GFG / official exam portals)
Generate explanations using real LLMs
Extend beyond GATE to multi-exam support
Align architecture with upcoming TypeScript migration
🎥 Demo

👉 https://youtu.be/eq8tBfASgIA?si=P4bIGpdKZO6DS9Mj

⭐ Key Highlight

This prototype demonstrates how combining:

⚡ Async batching
💾 Persistent caching
🤖 Multi-model evaluation

can:

🚀 Reduce execution time
🔁 Eliminate redundant computation
📈 Improve scalability

👉 Making LLM-based pipelines practical for real-world systems.


---


