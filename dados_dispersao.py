import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_dispersao.csv")

# grafico de dispersao separando por sexo
fig, ax = plt.subplots(figsize=(8, 5))
for sexo, marcador in zip(df["sexo"].unique(), ["o", "x"]):
    d = df[df["sexo"] == sexo]
    ax.scatter(d["altura_cm"], d["peso_kg"], marker=marcador, label=sexo, alpha=0.8)

ax.set_title("Altura x Peso")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
