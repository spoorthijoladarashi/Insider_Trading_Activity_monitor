import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# --------------------------------------------------
# Executive Dashboard Charts
# --------------------------------------------------

def top_companies_bar(df):

    top = (
        df.groupby("issuer_name")["market_value"]
        .sum()
        .reset_index()
        .sort_values(
            by="market_value",
            ascending=False
        )
        .head(20)
    )

    fig = px.bar(
        top,
        x="issuer_name",
        y="market_value",
        title="Top 20 Companies by Market Value",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="Company",
        yaxis_title="Market Value",
        height=600
    )

    return fig


# --------------------------------------------------
# Filing Trend
# --------------------------------------------------

def filing_trend_chart(df):

    if "filing_date" not in df.columns:
        return None

    trend = (
        df.groupby("filing_date")
        .size()
        .reset_index(name="count")
    )

    fig = px.line(
        trend,
        x="filing_date",
        y="count",
        title="Filing Activity Over Time",
        markers=True
    )

    return fig


# --------------------------------------------------
# Treemap
# --------------------------------------------------

def holdings_treemap(df):

    holdings = (
        df.groupby("issuer_name")["market_value"]
        .sum()
        .reset_index()
    )

    fig = px.treemap(
        holdings,
        path=["issuer_name"],
        values="market_value",
        title="Institutional Holdings Treemap"
    )

    return fig


# --------------------------------------------------
# Conviction Scatter Plot
# --------------------------------------------------

def conviction_scatter(df):

    required = [
        "shares_amount",
        "market_value",
        "conviction_score"
    ]

    if not all(col in df.columns for col in required):
        return None

    fig = px.scatter(
        df,
        x="shares_amount",
        y="market_value",
        color="conviction_score",
        size="conviction_score",
        hover_data=["issuer_name"],
        title="Conviction vs Market Value"
    )

    return fig


# --------------------------------------------------
# Market Value Distribution
# --------------------------------------------------

def market_value_distribution(df):

    fig = px.histogram(
        df,
        x="market_value",
        nbins=50,
        title="Market Value Distribution"
    )

    return fig


# --------------------------------------------------
# Market Value Box Plot
# --------------------------------------------------

def market_value_box(df):

    fig = px.box(
        df,
        y="market_value",
        title="Market Value Spread"
    )

    return fig


# --------------------------------------------------
# Correlation Heatmap
# --------------------------------------------------

def correlation_heatmap(df):

    numeric = df.select_dtypes(
        include=["number"]
    )

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Matrix"
    )

    return fig


# --------------------------------------------------
# Insider Buy Sell Chart
# --------------------------------------------------

def insider_transaction_chart(df):

    if "transaction_code" not in df.columns:
        return None

    fig = px.histogram(
        df,
        x="transaction_code",
        title="Insider Transaction Types"
    )

    return fig


# --------------------------------------------------
# Insider Timeline
# --------------------------------------------------

def insider_timeline(df):

    if "transaction_date" not in df.columns:
        return None

    timeline = (
        df.groupby("transaction_date")
        .size()
        .reset_index(name="count")
    )

    fig = px.line(
        timeline,
        x="transaction_date",
        y="count",
        title="Insider Trading Timeline",
        markers=True
    )

    return fig


# --------------------------------------------------
# Ownership Pie Chart
# --------------------------------------------------

def ownership_pie(df):

    if "ownership_form" not in df.columns:
        return None

    fig = px.pie(
        df,
        names="ownership_form",
        title="Ownership Distribution"
    )

    return fig


# --------------------------------------------------
# Smart Money Gauge
# --------------------------------------------------

def signal_gauge(score):

    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text":
                "Smart Money Score"
            },
            gauge={
                "axis":{
                    "range":[0,100]
                },
                "bar":{
                    "color":"green"
                }
            }
        )
    )

    fig.update_layout(
        height=400
    )

    return fig


# --------------------------------------------------
# Signal Ranking Chart
# --------------------------------------------------

def signal_ranking(df):

    top = (
        df.sort_values(
            by="signal_score",
            ascending=False
        )
        .head(20)
    )

    fig = px.bar(
        top,
        x="ticker",
        y="signal_score",
        title="Top Smart Money Signals"
    )

    return fig


# --------------------------------------------------
# Sector Allocation
# --------------------------------------------------

def sector_allocation(df):

    if "sector" not in df.columns:
        return None

    sector = (
        df.groupby("sector")["market_value"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        sector,
        names="sector",
        values="market_value",
        title="Sector Allocation"
    )

    return fig


# --------------------------------------------------
# Institution Concentration
# --------------------------------------------------

def institution_concentration(df):

    if "institution_name" not in df.columns:
        return None

    concentration = (
        df.groupby("institution_name")
        ["market_value"]
        .sum()
        .reset_index()
        .sort_values(
            by="market_value",
            ascending=False
        )
        .head(15)
    )

    fig = px.bar(
        concentration,
        x="institution_name",
        y="market_value",
        title="Top Institutions"
    )

    return fig


# --------------------------------------------------
# Conviction Distribution
# --------------------------------------------------

def conviction_distribution(df):

    if "conviction_score" not in df.columns:
        return None

    fig = px.histogram(
        df,
        x="conviction_score",
        nbins=25,
        title="Conviction Score Distribution"
    )

    return fig


# --------------------------------------------------
# Smart Money Dashboard Summary
# --------------------------------------------------

def dashboard_summary_pie(
    holdings_count,
    insider_count
):

    fig = px.pie(
        names=[
            "Institutional Holdings",
            "Insider Transactions"
        ],
        values=[
            holdings_count,
            insider_count
        ],
        title="Data Composition"
    )

    return fig
