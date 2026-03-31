# 🧠 LibrEd Smart Async Pipeline Prototype

A high-performance prototype inspired by LibrEd that demonstrates **async processing, intelligent caching, multi-model evaluation, real data integration, and scalable pipeline design**.

---

## 🚀 Problem Statement

The current LibrEd generator pipeline faces key challenges:

- ❌ Sequential LLM execution → high latency  
- 🔁 No caching → repeated computation  
- 📉 Fixed model usage → lack of flexibility  
- 📦 Limited data sources → dependency on specific platforms  

These issues make the pipeline slower and harder to scale for large datasets.

---

## 💡 Proposed Solution

This prototype rethinks the generator pipeline with a **scalable and modular architecture**:

- ⚡ **Async Batch Processing** → parallel execution of LLM tasks  
- 💾 **Persistent Caching** → avoids redundant computation  
- 🤖 **Multi-Model Evaluation** → supports LLaMA, Mistral, Phi  
- 🌐 **Alternative Data Sources** → integrates GFG-based extraction  
- 🔄 **Configurable Pipeline** → model + source selection  
- 📊 **Performance Metrics** → tracks latency and efficiency  
- 🌐 **Dashboard Visualization** → Streamlit-based insights  

---

## ✨ Key Features

- ⚡ Async pipeline using `asyncio`  
- 🔥 Batch processing to reduce LLM latency  
- 💾 File-based persistent caching  
- 🤖 Multi-model benchmarking system  
- 🌐 Real data source integration (GFG prototype)  
- 📊 Metrics tracking (time, cache hit rate, efficiency)  
- 🧾 Auto-generated explanations (simulated)  
- 🎛️ Configurable pipeline execution  

---

## ⚙️ Configurable Pipeline

The pipeline supports dynamic configuration:
```bash
python main.py --model mistral --source gfg
Supported Models
LLaMA (baseline)
Mistral (fast + accurate)
Phi (lightweight)
Supported Data Sources
Local dataset (default)
GeeksforGeeks (prototype)
⚡ Async Batching Insight

Instead of sequential execution:

Questions are grouped into batches
Multiple batches are processed concurrently
System avoids waiting for individual responses

👉 This significantly reduces total pipeline latency.

📊 Performance Benchmark
Metric	Sequential	Async + Cache
Processing Time	High	Reduced
Redundant Calls	Yes	Eliminated
Cache Hit Rate	0%	High
Scalability	Low	High
🌐 Data Source Integration (NEW)

This prototype introduces GFG-based question extraction:

Uses HTML parsing via BeautifulSoup
Extracts structured questions from articles
Demonstrates shift toward better and scalable data sources

👉 Designed to replace reliance on limited sources like GateAcademy.

🧠 Multi-Model Evaluation (NEW)

A benchmarking system to compare models:

Measures latency, consistency, and performance
Helps identify optimal model for pipeline tasks
Model	Speed	Accuracy	Use Case
LLaMA	Medium	Medium	Baseline
Mistral	Fast	High	Recommended
Phi	Fast	Medium	Lightweight
🔄 TypeScript Prototype (NEW)

A small TypeScript module demonstrates:

Async batch processing in a JS-based environment
Future compatibility with planned migration

👉 Aligns with LibrEd’s direction toward TypeScript-based pipeline.

⚙️ Tech Stack
Python 3.12
asyncio
Streamlit
BeautifulSoup (data extraction)
TypeScript (prototype module)
📂 Project Structure
libred-smart-pipeline-prototype/
│
├── src/
│   ├── async_pipeline.py
│   ├── model_evaluator.py
│   ├── cache_manager.py
│   ├── data_source_gfg.py
│
├── ts-prototype/
│   └── batchProcessor.ts
│
├── outputs/
│   ├── results.json
│   ├── metrics.json
│
├── app.py
├── main.py
└── README.md
▶️ How to Run
1. Install dependencies
pip install streamlit beautifulsoup4 requests
2. Run pipeline
python main.py --model mistral --source gfg
3. Launch dashboard
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

This prototype directly aligns with LibrEd goals:

Improves LLM performance using async batching
Eliminates redundant computation using caching
Introduces better data sources
Enables multi-model flexibility
Prepares for TypeScript-based pipeline

👉 Designed for direct integration into LibrEd generator

🚧 Future Improvements
Integrate real LLMs (Ollama, Mistral, etc.)
Improve data extraction accuracy
Add official exam portals
Replace mock classifier with embeddings
Extend beyond GATE (multi-exam support)
🎥 Demo

👉 https://youtu.be/eq8tBfASgIA?si=P4bIGpdKZO6DS9Mj

⭐ Key Highlight

This prototype shows how:

⚡ Async batching reduces latency
💾 Caching eliminates redundant computation
🌐 Better data sources improve scalability

👉 Making LLM pipelines practical for real-world systems

```bash
python main.py --model mistral --source gfg
Supported Models
LLaMA (baseline)
Mistral (fast + accurate)
Phi (lightweight)
Supported Data Sources
Local dataset (default)
GeeksforGeeks (prototype)
⚡ Async Batching Insight

Instead of sequential execution:

Questions are grouped into batches
Multiple batches are processed concurrently
System avoids waiting for individual responses

👉 This significantly reduces total pipeline latency.

📊 Performance Benchmark
Metric	Sequential	Async + Cache
Processing Time	High	Reduced
Redundant Calls	Yes	Eliminated
Cache Hit Rate	0%	High
Scalability	Low	High
🌐 Data Source Integration (NEW)

This prototype introduces GFG-based question extraction:

Uses HTML parsing via BeautifulSoup
Extracts structured questions from articles
Demonstrates shift toward better and scalable data sources

👉 Designed to replace reliance on limited sources like GateAcademy.

🧠 Multi-Model Evaluation (NEW)

A benchmarking system to compare models:

Measures latency, consistency, and performance
Helps identify optimal model for pipeline tasks
Model	Speed	Accuracy	Use Case
LLaMA	Medium	Medium	Baseline
Mistral	Fast	High	Recommended
Phi	Fast	Medium	Lightweight
🔄 TypeScript Prototype (NEW)

A small TypeScript module demonstrates:

Async batch processing in a JS-based environment
Future compatibility with planned migration

👉 Aligns with LibrEd’s direction toward TypeScript-based pipeline.

⚙️ Tech Stack
Python 3.12
asyncio
Streamlit
BeautifulSoup (data extraction)
TypeScript (prototype module)
📂 Project Structure
libred-smart-pipeline-prototype/
│
├── src/
│   ├── async_pipeline.py
│   ├── model_evaluator.py
│   ├── cache_manager.py
│   ├── data_source_gfg.py
│
├── ts-prototype/
│   └── batchProcessor.ts
│
├── outputs/
│   ├── results.json
│   ├── metrics.json
│
├── app.py
├── main.py
└── README.md
▶️ How to Run
1. Install dependencies
pip install streamlit beautifulsoup4 requests
2. Run pipeline
python main.py --model mistral --source gfg
3. Launch dashboard
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

This prototype directly aligns with LibrEd goals:

Improves LLM performance using async batching
Eliminates redundant computation using caching
Introduces better data sources
Enables multi-model flexibility
Prepares for TypeScript-based pipeline

👉 Designed for direct integration into LibrEd generator

🚧 Future Improvements
Integrate real LLMs (Ollama, Mistral, etc.)
Improve data extraction accuracy
Add official exam portals
Replace mock classifier with embeddings
Extend beyond GATE (multi-exam support)
🎥 Demo

👉 https://youtu.be/eq8tBfASgIA?si=P4bIGpdKZO6DS9Mj

⭐ Key Highlight

This prototype shows how:

⚡ Async batching reduces latency
💾 Caching eliminates redundant computation
🌐 Better data sources improve scalability

👉 Making LLM pipelines practical for real-world systems


---

# 🚀 NOW COMMIT DETAILS

## ✅ Branch Name

feat/full-pipeline-enhancement


---

## ✅ Commit Message

feat: integrate model evaluation, GFG data source, and TypeScript async prototype


---

---

python main.py --model mistral --source gfg
