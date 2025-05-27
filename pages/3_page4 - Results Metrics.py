import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Metrics per Models", layout="wide")
st.title("Results - Models")


df_metrics = pd.read_csv("df_metrics.csv")

tickers = df_metrics["Ticker"].unique()
selected_ticker = st.sidebar.selectbox("Selecione um Ticker", tickers)

df_tkr_metrics = df_metrics[df_metrics["Ticker"] == selected_ticker]


st.subheader(f"Metrics - {selected_ticker}")
st.dataframe(df_tkr_metrics.reset_index(drop=True))


st.subheader("Best Models +1 Day - based on R2 and RMSE")

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
fig, ax = plt.subplots(figsize=(6, 4))  
sns.barplot(data=df_best_per_ticker, x='Ticker', y='RMSE_+1', hue='Model', dodge=False, ax=ax)



ax.set_ylabel("RMSE (+1d)", fontsize=7)
ax.set_xlabel("Ticker", fontsize=7)


ax.legend(title="Model", fontsize=7, title_fontsize=7)

for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom',
                fontsize=7, color='black',
                xytext=(0, 4),
                textcoords='offset points')


ax.tick_params(axis='both', labelsize=8)

st.pyplot(fig)
