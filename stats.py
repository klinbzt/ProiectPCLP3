# Buzatu Calin-Cristian 313CB
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cerinta 1:
data = pd.read_csv('train.csv')

rows = int(data.shape[0])
cols = int(data.shape[1])
val_lipsa_total = rows * cols - data.count().sum()
dup_rows = data.duplicated().sum()

print(f"Informatii fisier train.csv:")
print(f"-> linii: {rows}\n-> coloane: {cols}\n-> nr. valori lipsa (totale): {val_lipsa_total}\n-> randuri duplicate: {dup_rows}")

## Determinare tipuri de obiecte + valori lipsa
for i in range(1, cols):
    types = data.columns[i]
    val_missing = data.iloc[:, i].isnull().sum()

    print(f"* tip: {types} (nr. valori lipsa: {val_missing})")

# Cerinta 2:
print(f"\nStatistici:")
data_uniq = data.drop_duplicates() ## Elimin liniile duplicate
true_rows = int(data_uniq.shape[0])

survived = data_uniq[data_uniq.columns[1]].sum() ## Poti sa faci si cu .mean(TODO)
prec_sur = survived / true_rows * 100
print(f"-> Procentaj supravietuitori: {round(prec_sur, 2)}%")

dead = true_rows - data_uniq[data_uniq.columns[1]].sum()
prec_dead = dead / true_rows * 100
print(f"-> Procentaj decedati: {round(prec_dead, 2)}%")

## Determinare procentaj pentru fiecare PClass
pstats = data_uniq['Pclass'].value_counts(normalize=True) * 100
pstats_str = pstats.sort_index().round(2).to_string()
print(f"-> Pocentaje pentru {pstats_str}")

## Calcularea procentului de barbati/femei
procent_gen = data_uniq['Sex'].value_counts(normalize=True) * 100

print(f"-> Procentaje {procent_gen.round(2).to_string()}")

## Grafice:

plt.figure(figsize=(10, 10))
plt.bar(['Supraviețuitori', 'Decedați'], [prec_sur, prec_dead], color=['green', 'red'])
plt.ylabel('Procentaj (%)')
plt.title('Procentajul supraviețuitorilor vs. decedaților')
plt.show()

## Procentaj pentru fiecare clasă de pasageri (Pclass)
plt.figure(figsize=(10, 10))
plt.bar(pstats.index.astype(str), pstats.values, color='blue')
plt.xlabel('Clasă de pasageri (Pclass)')
plt.ylabel('Procentaj (%)')
plt.title('Procentajul pentru fiecare clasă de pasageri')
plt.show()

## Procentaj pentru fiecare sex (male/female)
plt.figure(figsize=(10, 10))
plt.bar(procent_gen.index, procent_gen.values, color=['blue', 'pink'])
plt.xlabel('Sex')
plt.ylabel('Procentaj (%)')
plt.title('Procentajul pentru fiecare sex')
plt.show()