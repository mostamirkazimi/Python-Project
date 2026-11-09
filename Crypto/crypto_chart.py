import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Crypto Chart", layout="wide")
st.title("📊 Crypto Chart")

tickchart = [
    "BTC-USD",
    "ETH-USD",
    "BNB-USD",
    "XRP-USD",
    "ADA-USD",
    "SOL-USD",
    "DOGE-USD",
    "DOT-USD",
    "MATIC-USD",
    "LTC-USD",
    "TSLA"
]

dropdown = st.selectbox(
    "Select a cryptocurrency or stock:",
    tickchart
)

start_date = st.date_input(
    "Select a start date:",
    pd.to_datetime("2022-01-01")
)

end_date = st.date_input(
    "Select an end date:",
    pd.to_datetime("2023-01-01")
)

if dropdown:
    df = yf.download(
        dropdown,
        start=start_date,
        end=end_date,
        interval="1d"
    )

    if not df.empty:

        # حذف MultiIndex در صورت وجود
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        st.subheader(f"Price Chart: {dropdown}")

        st.line_chart(df["Close"])

        st.write(df.tail())
    else:
        st.error("No data found.")
