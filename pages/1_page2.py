
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurações iniciais da página
st.set_page_config(page_title="Predictions SARIMA e LSTM", layout="wide")
st.title("Predictions SARIMA e LSTM - December/20")

# Carregar os dados
df = pd.read_csv("df_merged.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Corrigir zeros como NaN
df[['Sarima_Pred_1', 'Sarima_Pred_3', 'Sarima_Pred_7']] = \
    df[['Sarima_Pred_1', 'Sarima_Pred_3', 'Sarima_Pred_7']].replace(0, np.nan)

# Filtrar apenas dezembro de 2020
df = df[(df['Date'].dt.month == 12) & (df['Date'].dt.year == 2020)]
df = df.sort_values(by=['Ticker', 'Date'])

# Seleção de ticker no sidebar
tickers = df['Ticker'].unique()
selected_ticker = st.sidebar.selectbox("Selecione um Ticker", tickers)

# Filtrar dados do ticker
df_tkr = df[df['Ticker'] == selected_ticker]

# Gráfico SARIMA
st.subheader(f"SARIMA Predictions - {selected_ticker}")
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(df_tkr['Date'], df_tkr['Close'], label='Real Price', color='black', linewidth=2)
ax1.plot(df_tkr['Date'], df_tkr['Sarima_Pred_1'], label='SARIMA +1d', linestyle='--')
ax1.plot(df_tkr['Date'], df_tkr['Sarima_Pred_3'], label='SARIMA +3d', linestyle='--')
ax1.plot(df_tkr['Date'], df_tkr['Sarima_Pred_7'], label='SARIMA +7d', linestyle='--')
ax1.set_title("Real Price vs SARIMA Predictions")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price")
ax1.legend()
ax1.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Gráfico LSTM
st.subheader(f"LSTM Predictions - {selected_ticker}")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(df_tkr['Date'], df_tkr['Close'], label='Preço Real', color='black', linewidth=2)
ax2.plot(df_tkr['Date'], df_tkr['LSTM_Pred_1'], label='LSTM +1d', linestyle='--')
ax2.plot(df_tkr['Date'], df_tkr['LSTM_Pred_3'], label='LSTM +3d', linestyle='--')
ax2.plot(df_tkr['Date'], df_tkr['LSTM_Pred_7'], label='LSTM +7d', linestyle='--')
ax2.set_title("Real Price vs LSTM Predictions")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price")
ax2.legend()
ax2.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig2)

