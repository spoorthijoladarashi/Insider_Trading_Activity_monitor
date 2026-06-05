import streamlit as st

from utils.data_loader import load_data

df,_=load_data()

st.title("AI Insights")

avg=df["conviction_score"].mean()

if avg>75:

    st.success("""
    Strong institutional
    conviction detected.
    """)

elif avg>50:

    st.warning("""
    Moderate confidence
    among institutions.
    """)

else:

    st.error("""
    Weak institutional
    sentiment.
    """)

top = (
    df.groupby("issuer_name")
    ["market_value"]
    .sum()
    .idxmax()
)

st.info(
    f"Highest institutional allocation: {top}"
)
