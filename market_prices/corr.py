import pandas as pd
import numpy as np
from os import getcwd, listdir
import matplotlib.pyplot as plt

df = pd.read_csv('prices.csv')

piv = df.pivot(columns='Pair', values='close').fillna(0)
corr = piv.corr()
for col in corr.columns:
    corr[col] = ((corr[col]*1_000_000) % 1_00) / 1_00
    corr[col].replace({0.0:1.0}, inplace = True)
    for x, y in enumerate(corr[col]):
        if y != 1.0:
            corr[col].iloc[x] *= (-1)

plt.matshow(corr)
plt.show()
print(corr)

corr.to_csv('price_correlations.csv')