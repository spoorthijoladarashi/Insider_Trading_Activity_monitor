import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.analytics import *

holdings, signals = load_data()

kpi = calculate_kpis(holdings)

st.title("Executive Dashboard")

c1,c2,c3,c4=st.columns(4)

c1.metric(
    "Companies",
    f"{kpi['companies']:,}"
)

c2.metric(
    "Records",
    f"{kpi['records']:,}"
)

c3.metric(
    "Market Value",
    f"${kpi['market_value']:,.0f}"
)

c4.metric(
    "Avg Conviction",
    kpi['avg_conviction']
)

top=top_companies(holdings)

fig=px.bar(
    top,
    x="issuer_name",
    y="market_value",
    title="Top Holdings"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
