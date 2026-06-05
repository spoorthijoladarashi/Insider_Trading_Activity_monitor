import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

holdings,_=load_data()

st.title("Institutional Holdings")

top = (
    holdings.groupby("issuer_name")
    ["market_value"]
    .sum()
    .reset_index()
)

fig=px.treemap(
    top,
    path=["issuer_name"],
    values="market_value",
    title="Institutional Capital Allocation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2=px.scatter(
    holdings,
    x="shares_amount",
    y="market_value",
    color="conviction_score",
    size="conviction_score"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
