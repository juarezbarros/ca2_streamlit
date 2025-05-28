
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Predictions SARIMA e LSTM", layout="wide")
st.title("Predictions SARIMAX, SARIMAX HYPEROPT, LSTM and LSTM HYPEROPT DEC/20")

df = pd.read_csv("df_merged.csv")
df['Date'] = pd.to_datetime(df['Date'])

df[['Sarima_Pred_1', 'Sarima_Pred_3', 'Sarima_Pred_7']] = \
    df[['Sarima_Pred_1', 'Sarima_Pred_3', 'Sarima_Pred_7']].replace(0, np.nan)

df = df[(df['Date'].dt.month == 12) & (df['Date'].dt.year == 2020)]
df = df.sort_values(by=['Ticker', 'Date'])

tickers = df['Ticker'].unique()
selected_ticker = st.sidebar.selectbox("Selecione um Ticker", tickers)

df_tkr = df[df['Ticker'] == selected_ticker]


col1, col2 = st.columns(2)


with col1:
    st.subheader(f"SARIMAX - {selected_ticker}")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(df_tkr['Date'], df_tkr['Close'], label='Real Price', color='black', linewidth=2)
    ax1.plot(df_tkr['Date'], df_tkr['Sarima_Pred_1'], label='SARIMA +1d', linestyle='--')
    ax1.plot(df_tkr['Date'], df_tkr['Sarima_Pred_3'], label='SARIMA +3d', linestyle='--')
    ax1.plot(df_tkr['Date'], df_tkr['Sarima_Pred_7'], label='SARIMA +7d', linestyle='--')
    ax1.set_title("Real vs SARIMA")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price")
    ax1.legend()
    ax1.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig1)


with col2:
    st.subheader(f"SARIMAX HYPEROPT - {selected_ticker}")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.plot(df_tkr['Date'], df_tkr['Close'], label='Real Price', color='black', linewidth=2)
    ax2.plot(df_tkr['Date'], df_tkr['SarimaH_Pred_1'], label='SARIMA_H +1d', linestyle='--')
    ax2.plot(df_tkr['Date'], df_tkr['SarimaH_Pred_3'], label='SARIMA_H +3d', linestyle='--')
    ax2.plot(df_tkr['Date'], df_tkr['SarimaH_Pred_7'], label='SARIMA_H +7d', linestyle='--')
    ax2.set_title("Real vs SARIMA HYPEROPT")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Price")
    ax2.legend()
    ax2.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig2)


col3, col4 = st.columns(2)


with col3:
    st.subheader(f"LSTM - {selected_ticker}")
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.plot(df_tkr['Date'], df_tkr['Close'], label='Real Price', color='black', linewidth=2)
    ax3.plot(df_tkr['Date'], df_tkr['LSTM_Pred_1'], label='LSTM +1d', linestyle='--')
    ax3.plot(df_tkr['Date'], df_tkr['LSTM_Pred_3'], label='LSTM +3d', linestyle='--')
    ax3.plot(df_tkr['Date'], df_tkr['LSTM_Pred_7'], label='LSTM +7d', linestyle='--')
    ax3.set_title("Real vs LSTM")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Price")
    ax3.legend()
    ax3.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig3)


with col4:
    st.subheader(f"LSTM HYPEROPT - {selected_ticker}")
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    ax4.plot(df_tkr['Date'], df_tkr['Close'], label='Real Price', color='black', linewidth=2)
    ax4.plot(df_tkr['Date'], df_tkr['LSTMH_Pred_1'], label='LSTM_H +1d', linestyle='--')
    ax4.plot(df_tkr['Date'], df_tkr['LSTMH_Pred_3'], label='LSTM_H +3d', linestyle='--')
    ax4.plot(df_tkr['Date'], df_tkr['LSTMH_Pred_7'], label='LSTM_H +7d', linestyle='--')
    ax4.set_title("Real vs LSTM HYPEROPT")
    ax4.set_xlabel("Date")
    ax4.set_ylabel("Price")
    ax4.legend()
    ax4.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig4)


