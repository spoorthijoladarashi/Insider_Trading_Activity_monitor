import streamlit as st

st.set_page_config(
    page_title="Smart Money Analytics Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.metric-container{
    background-color:#1e293b;
    padding:15px;
    border-radius:12px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Smart Money Analytics Dashboard")

st.markdown("""
### Institutional Holdings & Insider Trading Intelligence

Analyze:

✅ SEC 13F Holdings

✅ Insider Transactions

✅ Conviction Scores

✅ Smart Money Signals

✅ AI Generated Insights
""")

st.info("Select dashboard pages from sidebar.")
