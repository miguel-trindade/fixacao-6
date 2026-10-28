import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_heatmap.csv")

# ordem correta dos dias da semana
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
tabela = tabela.reindex(dias)

# heatmap
fig, ax = plt.subplots(figsize=(8, 5))
im = ax.imshow(tabela.values, cmap="YlOrRd", aspect="auto")
ax.set_xticks(range(len(tabela.columns)))
ax.set_xticklabels(tabela.columns)
ax.set_yticks(range(len(tabela.index)))
ax.set_yticklabels(tabela.index)

# valores dentro das celulas
for i in range(tabela.shape[0]):
    for j in range(tabela.shape[1]):
        ax.text(j, i, int(tabela.values[i, j]), ha="center", va="center", fontsize=9)

fig.colorbar(im, label="Movimento de clientes")
ax.set_title("Movimento de clientes por dia e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")

plt.tight_layout()
plt.show()
