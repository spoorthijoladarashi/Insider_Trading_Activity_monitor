import pandas as pd

def calculate_kpis(df):

    return {
        "companies":df["issuer_name"].nunique(),
        "records":len(df),
        "market_value":df["market_value"].sum(),
        "avg_conviction":round(
            df["conviction_score"].mean(),2
        )
    }

def top_companies(df):

    return (
        df.groupby("issuer_name")
        ["market_value"]
        .sum()
        .reset_index()
        .sort_values(
            by="market_value",
            ascending=False
        )
        .head(20)
    )
