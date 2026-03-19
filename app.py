import streamlit as st
import json

st.title("🧠 LibreED Smart Pipeline Prototype")

# Load results
try:
    with open("outputs/results.json") as f:
        results = json.load(f)
except:
    results = []

# Load metrics FIRST (important fix)
try:
    with open("outputs/metrics.json") as f:
        metrics = json.load(f)
except:
    metrics = None


# 📊 RESULTS
st.header("📊 Results")

for r in results:
    st.markdown(f"""
    **Q:** {r['question']}  
    👉 **Topic:** {r['topic']}
    """)


# ⚡ METRICS
st.header("⚡ Metrics")

if metrics:
    st.json(metrics)

    # 📈 PERFORMANCE INSIGHT
    st.subheader("📈 Performance Insight")

    if metrics["cache_hit_rate"] > 50:
        st.success("🚀 System is optimized with caching!")
    else:
        st.warning("⚠️ Low cache usage – optimization possible.")
else:
    st.write("Run pipeline first to see metrics.")