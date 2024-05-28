# Buzatu Calin-Cristian 313CB
import pandas as pd
import numpy as np

# Cerinta 1:
data = pd.read_csv('train.csv')

rows = int(data.shape[0])
cols = int(data.shape[1])
val_lipsa_total = rows * cols - data.count().sum()
dup_rows = data.duplicated().sum()

print(f"Informatii fisier train.csv:")
print(f"-> linii: {rows}\n-> coloane: {cols}\n-> nr. valori lipsa (totale): {val_lipsa_total}\n-> randuri duplicate: {dup_rows}")

# Determinare tipuri de obiecte + valori lipsa
for i in range(1, cols):
    types = data.columns[i]
    val_missing = data.iloc[:, i].isnull().sum()

    print(f"* tip: {types} (nr. valori lipsa: {val_missing})")

# Cerinta 2:

survived = data[data.columns[1]].sum()
print(survived)