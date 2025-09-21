import streamlit as st
import pandas as pd

st.set_page_config(page_title="DHARMA Parameters", page_icon="🧭")

st.title("Balanced Parameters")

st.subheader("Universal Targets (bands)")
st.write("""
- Beta: 0.5097 within ±0.0036
- Entropy: 5.1778 within ±0.0494
""")

st.subheader("Cycle Position Hotspots")
positions = [32, 41, 55, 39, 10, 74, 60, 36, 72, 67]
st.write(", ".join(map(str, positions)))

st.subheader("Signature Expert Combos")
data = [
    ["D1_EnsembleStacking + E16_Chaos_Theory + E1_FrequencyAnalysis"],
    ["B1_RandomForest_v2 + E21_CRT_Reconstructor + G19_Catastrophic_Forgetting"],
    ["A1_ARIMA_v2 + E16_Chaos_Theory + E30_MarkovChain_Residuals"],
    ["E16_Chaos_Theory + E1_FrequencyAnalysis + E30_MarkovChain_Residuals"],
]
df = pd.DataFrame(data, columns=["Combination"])
st.dataframe(df, use_container_width=True)

st.caption("These bands and combos are consistent across 54–56/56 periods.")
