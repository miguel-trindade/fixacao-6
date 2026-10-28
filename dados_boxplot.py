import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leitura dos dados
df = pd.read_csv("dados_boxplot.csv")

deps = list(df["departamento"].unique())
dados = [df[df["departamento"] == d]["salario"] for d in deps]

# boxplot
fig, ax = plt.subplots(figsize=(8, 5))
ax.boxplot(dados)
ax.set_xticklabels(deps)
ax.set_title("Salário por departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
