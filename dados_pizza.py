import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_pizza.csv")

# grafico de pizza
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%", startangle=90)
ax.set_title("Faturamento por canal de venda")

plt.tight_layout()
plt.show()
