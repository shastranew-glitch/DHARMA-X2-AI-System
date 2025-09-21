import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DHARMA Status", page_icon="🧠", layout="wide")

st.title("DHARMA Data Sync — Status")

summary_csv = "reports/dataset_summary.csv"
summary_json = "reports/dataset_summary.json"

if not os.path.exists(summary_csv) or not os.path.exists(summary_json):
    st.warning("No summary found yet. Run DHARMA Data Sync to generate artifacts.")
else:
    df = pd.read_csv(summary_csv)
    st.subheader("Input Files")
    st.dataframe(df, use_container_width=True)

    meta = pd.read_json(summary_json, typ="series")
    c1, c2, c3 = st.columns(3)
    c1.metric("Files", int(meta.get("file_count", 0)))
    c2.metric("Total Size (MB)", round(meta.get("total_size_bytes", 0)/1e6, 2))
    c3.metric("Generated (UTC)", str(meta.get("generated_utc", "")))

st.caption("Powered by DHARMA X2 • Streamlit Community Cloud")
