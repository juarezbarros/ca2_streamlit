import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st



# Suponha que o df_merged já foi carregado:
df_merged = pd.read_csv("df_merged.csv")
# Ou se já estiver no ambiente: apenas df_merged

# Converter coluna Date para datetime (se ainda não estiver)
df_merged['Date'] = pd.to_datetime(df_merged['Date'])

# Filtrar datas a partir de 2020-12-01 (dezembro de 2020 em diante)
df_filtered = df_merged[df_merged['Date'] >= '2020-12-01']

# Gráfico de preços de fechamento por ticker
plt.figure(figsize=(14, 7))

for ticker in df_filtered['Ticker'].unique():
    ticker_df = df_filtered[df_filtered['Ticker'] == ticker]
    plt.plot(ticker_df['Date'], ticker_df['Close'], label=ticker)

plt.title('Close Price per Ticker (From December 2020)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
