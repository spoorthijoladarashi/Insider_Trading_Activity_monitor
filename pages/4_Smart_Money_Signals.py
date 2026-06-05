import streamlit as st
import plotly.graph_objects as go

from utils.data_loader import load_data

_,signals=load_data()

st.title("Smart Money Signals")

score = signals["signal_score"].mean()

fig = go.Figure(
go.Indicator(
    mode="gauge+number",
    value=score,
    title={"text":"Smart Money Score"}
))

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    signals.sort_values(
        by="signal_score",
        ascending=False
    )
)
