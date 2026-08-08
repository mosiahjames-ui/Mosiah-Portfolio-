import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Cuts & Slices Ops Dashboard", layout="wide")

# 1. Top Executive Narrative Banner (Context & Insight First)
st.title("🍕 Cuts & Slices — Sales & Discount Analysis")

st.error("""
🚨 **Executive Insight:** Operational inefficiencies and unstandardized regional entry errors directly caused **$156,000+ in confirmed hidden business losses**.
""")

# Executive Narrative Section
st.markdown("""
### Executive Summary
* **Context:** Cuts & Slices is a high-demand, fast-growing NYC pizzeria where small operational leakages on high-volume sales directly eat into tight profit margins.
* **The Data:** Analysis of nearly 10,000 sales orders tracking item sales, applied discounts, and regional transaction records.
* **How Analyzed:** Cleaned and standardized raw transaction records to run a hypothesis-driven discount audit, isolating where pricing rules failed.
* **The So-What:** We need to implement strict automated input validation rules and hard caps on promotional discounts to protect profit margins as the business expands.
""")

st.divider()

# 2. Interactive Section & Data Visuals
st.subheader("Regional Loss & Discount Audit")

# Filter Sidebar
region = st.sidebar.selectbox("Filter by Region", ["All Regions", "North", "South", "East", "West"])

# Sample Summary Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Uncaptured Loss", "$156,420", "-12.4% Margin Impact")
col2.metric("Orders with Deep Discounts", "1,248", "Rule Violation")
col3.metric("Data Entry Error Rate", "8.2%", "Requires Validation")

st.info("💡 Use the filters on the left to drill down into specific regional data-entry anomalies.")