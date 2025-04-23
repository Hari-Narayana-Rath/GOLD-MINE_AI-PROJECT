import streamlit as st
import pandas as pd
import numpy as np
import json
from goldmine_logic import max_gold_with_path

st.set_page_config(page_title="Gold Mine Game", layout="wide")
st.title("🏆 Gold Mine Game Visualized")
st.markdown("See how your AI miner navigates the gold mine and collects maximum gold!")

input_method = st.radio("Input Method:", ["Upload JSON", "Enter manually"])

gold = []

if input_method == "Upload JSON":
    file = st.file_uploader("Upload a JSON file with 2D list", type=["json"])
    if file:
        gold = json.load(file)
        st.success("✅ Matrix loaded successfully!")

else:
    text = st.text_area("Enter a 2D matrix (use commas):", "1,3,1,5\n2,2,4,1\n5,0,2,3\n0,6,1,2")
    try:
        gold = [list(map(int, row.split(','))) for row in text.strip().split('\n')]
        st.success("✅ Matrix parsed successfully!")
    except:
        st.error("Please check the format.")

if gold:
    st.subheader("💎 Gold Mine Grid:")
    st.dataframe(pd.DataFrame(gold))

    if st.button("💰 Calculate and Visualize"):
        max_gold, dp_table, final_path = max_gold_with_path(gold)


        # Show DP table
        st.subheader("📊 DP Table (Calculated Max Gold from Each Cell):")
        st.dataframe(pd.DataFrame(dp_table))

        # Show path on gold mine
        st.subheader("🚶‍♂️ Optimal Path Visualization:")
        path_mask = np.full((len(gold), len(gold[0])), "", dtype=object)
        for r, c in final_path:
            path_mask[r][c] = "🟩"  # Green square for path

        path_vis = pd.DataFrame([[f"{path_mask[r][c]} {gold[r][c]}" if path_mask[r][c] else str(gold[r][c]) 
                                  for c in range(len(gold[0]))] for r in range(len(gold))])

        st.dataframe(path_vis)

        # List the moves
        st.subheader("🧭 Step-by-step Moves:")
        for idx, (r, c) in enumerate(final_path):
            st.write(f"Step {idx+1}: Move to cell ({r}, {c}) → {gold[r][c]} gold")

        st.success(f"🎯 Maximum gold collected: **{max_gold} tons**")

# ─── Footer ────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:1px solid #ccc"/>

<div style='text-align: center; color: grey; font-size: 14px;'>
    Made by:<br/>
    <b>Hari Narayana Rath</b> – <code>AP22110010601</code> <br/>
    <b>Pranav S Krishnan</b> – <code>AP22110010653</code><br/>
    <b>Christo</b> – <code>AP22110010399</code><br/>
    <b>Sri Ram</b> – <code>AP22110010509</code><br/>
    <b>Y J Linus</b> – <code>AP22110010619</code><br/>
</div>
""", unsafe_allow_html=True)
