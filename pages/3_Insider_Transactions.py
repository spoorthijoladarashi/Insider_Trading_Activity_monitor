import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df,_ = load_data()

st.title("Insider Transactions")

if "transaction_code" in df.columns:

    fig=px.histogram(
        df,
        x="transaction_code",
        title="Buy/Sell Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
