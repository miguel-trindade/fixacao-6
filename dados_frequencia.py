import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_frequencia.csv")

# conta quantas vezes cada tipo aparece
contagem = df["tipo_atendimento"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(contagem.index, contagem.values, edgecolor="black")

# escreve o valor em cima de cada barra
for i, v in enumerate(contagem.values):
    ax.text(i, v + 1, str(v), ha="center")

ax.set_title("Frequência por tipo de atendimento")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Quantidade")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
