import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Carregar o dataframe
df = pd.read_csv("df_merged.csv")
df['Date'] = pd.to_datetime(df['Date'])  # Converter para datetime

# Filtrar datas a partir de 1º de dezembro de 2020
df_filtered = df[df['Date'] >= '2020-12-01']

# Título do app
st.title("Fechamento por Ticker (Dezembro 2020 em diante)")

# Criar o gráfico com Matplotlib
plt.figure(figsize=(14, 7))

for ticker in df_filtered['Ticker'].unique():
    ticker_df = df_filtered[df_filtered['Ticker'] == ticker]
    plt.plot(ticker_df['Date'], ticker_df['Close'], label=ticker)

plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Preço por Ticker')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Exibir no Streamlit
st.pyplot(plt)

