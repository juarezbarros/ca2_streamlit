import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Metrics per Models", layout="wide")
st.title("Avaliação de Modelos SARIMA e LSTM")


df_metrics = pd.read_csv("df_metrics.csv")

tickers = df_metrics["Ticker"].unique()
selected_ticker = st.sidebar.selectbox("Selecione um Ticker", tickers)

df_tkr_metrics = df_metrics[df_metrics["Ticker"] == selected_ticker]


st.subheader(f"Métricas dos Modelos - {selected_ticker}")
st.dataframe(df_tkr_metrics.reset_index(drop=True))


st.subheader("Best Model per Ticker +1 Day")

best_models = []
for ticker in df_metrics["Ticker"].unique():
    df_ticker = df_metrics[df_metrics["Ticker"] == ticker]
    df_valid = df_ticker[df_ticker["R2_+1"] > 0]
    if not df_valid.empty:
        best = df_valid.sort_values("RMSE_+1").iloc[0]
    else:
        best = df_ticker.sort_values("RMSE_+1").iloc[0]
    best_models.append(best)

df_best_per_ticker = pd.DataFrame(best_models)


sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_best_per_ticker, x='Ticker', y='RMSE_+1', hue='Model', dodge=False, ax=ax)

ax.set_title("Best Model per Ticker +1 Day", fontsize=14)
ax.set_ylabel("RMSE (+1 Day)")
ax.set_xlabel("Ticker")
ax.legend(title="Model")


for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom',
                fontsize=10, color='black',
                xytext=(0, 5),
                textcoords='offset points')

st.pyplot(fig)
