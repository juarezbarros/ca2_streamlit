import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

url = "df_sarima_graph1.csv"
df_sarima_graph1 = pd.read_csv(url)


df = df_sarima_graph1.copy()

# Preprocessamento
df[['Pred_1', 'Pred_3', 'Pred_7']] = df[['Pred_1', 'Pred_3', 'Pred_7']].replace(0, np.nan)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by=['Ticker', 'Date'])

# Sidebar: seleção do ticker
tickers = df['Ticker'].unique()
selected_ticker = st.sidebar.selectbox("Selecione o Ticker", tickers)

# Filtrar dados para o ticker selecionado
df_tkr = df[df['Ticker'] == selected_ticker]

# Criar gráfico interativo com plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=df_tkr['Date'], y=df_tkr['Close'], 
                         mode='lines+markers', name='Close', line=dict(color='black')))
fig.add_trace(go.Scatter(x=df_tkr['Date'], y=df_tkr['Pred_1'], 
                         mode='lines', name='Pred_1', line=dict(dash='dot')))
fig.add_trace(go.Scatter(x=df_tkr['Date'], y=df_tkr['Pred_3'], 
                         mode='lines', name='Pred_3', line=dict(dash='dot')))
fig.add_trace(go.Scatter(x=df_tkr['Date'], y=df_tkr['Pred_7'], 
                         mode='lines', name='Pred_7', line=dict(dash='dot')))

fig.update_layout(
    title=f"Preço Real vs Previsões - {selected_ticker}",
    xaxis_title="Data",
    yaxis_title="Preço ($)",
    template="plotly_white",
    xaxis=dict(tickangle=45),
    legend=dict(x=0, y=1)
)

st.plotly_chart(fig)

