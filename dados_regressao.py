import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_regressao.csv")

# regressao linear simples (y = m*x + b)
m, b = np.polyfit(df["renda_mensal"], df["gasto_mensal"], 1)
r2 = np.corrcoef(df["renda_mensal"], df["gasto_mensal"])[0, 1] ** 2

x = np.linspace(df["renda_mensal"].min(), df["renda_mensal"].max(), 100)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["renda_mensal"], df["gasto_mensal"], alpha=0.7, label="Dados")
ax.plot(x, m * x + b, color="red", label=f"y = {m:.3f}x + {b:.1f} (R² = {r2:.3f})")

ax.set_title("Renda mensal x Gasto mensal")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
