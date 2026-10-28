import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_barras.csv")

categorias = list(df["categoria"].unique())
regioes = list(df["regiao"].unique())

# grafico de barras agrupadas
fig, ax = plt.subplots(figsize=(8, 5))
largura = 0.2
x = np.arange(len(categorias))

for i, r in enumerate(regioes):
    valores = []
    for c in categorias:
        v = df[(df["categoria"] == c) & (df["regiao"] == r)]["vendas_medias"].iloc[0]
        valores.append(v)
    ax.bar(x + (i - 1.5) * largura, valores, largura, label=r)

ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.set_title("Vendas médias por categoria e região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
