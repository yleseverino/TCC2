import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
dados = pd.read_csv("resultados.csv")

# ax = sns.boxplot(x = dados["51 m = 3"])

# ax = sns.boxplot(x = dados["51 m = 5"])

ax = sns.boxplot(x = dados["51 m = 10"])

plt.show()