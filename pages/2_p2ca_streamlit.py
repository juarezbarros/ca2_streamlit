import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Indicators", layout="wide")

url = "df_merged.csv"  # ou caminho correto no GitHub
df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Date'].dt.month == 12]  # Filtrar apenas Dezembro

tickers = df['Ticker'].unique()
selected_ticker = st.sidebar.selectbox("Select a Ticker", tickers)

df_tkr = df[df['Ticker'] == selected_ticker]

st.title(f"Technical Indicators - {selected_ticker} (December Only)")

# Plot 1 - Volume
fig1 = px.line(df_tkr, x='Date', y='Volume', title='Daily Volume')
st.plotly_chart(fig1, use_container_width=True)

# Plot 2 - SMA_10
fig2 = px.line(df_tkr, x='Date', y='SMA_10', title='SMA 10')
st.plotly_chart(fig2, use_container_width=True)

# Plot 3 - RSI
fig3 = px.line(df_tkr, x='Date', y='RSI', title='RSI')
st.plotly_chart(fig3, use_container_width=True)

# Plot 4 - Volatility_10
fig4 = px.line(df_tkr, x='Date', y='Volatility_10', title='10-Day Volatility')
st.plotly_chart(fig4, use_container_width=True)
