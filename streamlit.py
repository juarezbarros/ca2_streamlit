import streamlit as st
import pandas as pd
import plotly.graph_objects as go

url = "df_sarima_graph1.csv"
df_sarima_graph1 = pd.read_csv(url)



df = df_sarima_graph1.copy()
df['Date'] = pd.to_datetime(df['Date'])


horizon = st.selectbox("...", ['Pred_1', 'Pred_3', 'Pred_7'])


plot_df = df[['Date', 'Close', horizon]].dropna()


fig = go.Figure()


fig.add_trace(go.Scatter(
    x=plot_df['Date'],
    y=plot_df['Close'],
    mode='lines+markers',
    name='Real Price'
))


fig.add_trace(go.Scatter(
    x=plot_df['Date'],
    y=plot_df[horizon],
    mode='lines+markers',
    name=f'Prediction {horizon}'
))

fig.update_layout(
    title=f'AAPL - Real Price vs Prediction {horizon}',
    xaxis_title='Date',
    yaxis_title='Price ($)',
    template='plotly_white'
)

st.plotly_chart(fig)
