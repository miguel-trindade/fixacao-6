import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_distribuicao.csv")

# histograma das idades
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["idade"], bins=10, edgecolor="black")
ax.set_title("Distribuição da idade dos clientes")
ax.set_xlabel("Idade")
ax.set_ylabel("Frequência")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
