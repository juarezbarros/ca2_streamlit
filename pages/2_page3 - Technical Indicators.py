import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Indicators", layout="wide")

url = "df_merged.csv" 
df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['Date'])
df = df[(df['Date'] >= '2020-12-01')]


tickers = df['Ticker'].unique()
selected_ticker = st.sidebar.selectbox("Select a Ticker", tickers)

df_tkr = df[df['Ticker'] == selected_ticker]

st.title(f"Technical Indicators - {selected_ticker} (December Only)")

# Plot 1 - Volume
fig1 = px.line(df_tkr, x='Date', y='Volume', title='Daily Volume - The total number of shares traded for a stock on a given day.')
st.plotly_chart(fig1, use_container_width=True)

# Plot 2 - SMA_10
fig2 = px.line(df_tkr, x='Date', y='SMA_10', title='Simple Moving Average 10 - The average closing price of a stock over the last 10 trading days.')
st.plotly_chart(fig2, use_container_width=True)

# Plot 3 - RSI
fig3 = px.line(df_tkr, x='Date', y='RSI', title='RSI - A momentum indicator that measures the speed and change of price movements.')
st.plotly_chart(fig3, use_container_width=True)

# Plot 4 - Volatility_10
fig4 = px.line(df_tkr, x='Date', y='Volatility_10', title='10-Day Volatility - A measure of how much the stock’s price fluctuated over the last 10 days.')
st.plotly_chart(fig4, use_container_width=True)
