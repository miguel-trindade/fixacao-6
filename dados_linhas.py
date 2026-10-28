import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados (convertendo a coluna data)
df = pd.read_csv("dados_linhas.csv", parse_dates=["data"])
df = df.sort_values("data")

# uma linha para cada loja
fig, ax = plt.subplots(figsize=(8, 5))
for loja in sorted(df["loja"].unique()):
    d = df[df["loja"] == loja]
    ax.plot(d["data"], d["vendas"], marker="o", markersize=3, label=loja)

ax.set_title("Vendas ao longo do tempo")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.legend()
ax.grid(alpha=0.3)
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
