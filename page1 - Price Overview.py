import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


df = pd.read_csv("df_merged.csv")
df['Date'] = pd.to_datetime(df['Date'])  # Converter para datetime
df_filtered = df[df['Date'] >= '2020-01-01']

st.title("Close Price - Stocks 2020")
plt.figure(figsize=(14, 7))

for ticker in df_filtered['Ticker'].unique():
    ticker_df = df_filtered[df_filtered['Ticker'] == ticker]
    plt.plot(ticker_df['Date'], ticker_df['Close'], label=ticker)

plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Preço por Ticker')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Exibir no Streamlit
st.pyplot(plt)

