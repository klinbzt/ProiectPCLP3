import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 5
data = pd.read_csv('../date/train_prelucrat.csv')

## Intervale varste
bins = [0, 20, 40, 60, 80]
labels = ['0-20', '21-40', '41-60', '61-80']

## Adaugarea coloana 'Age_interval'
data['Age_interval'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

## Adaugare coloana in tabel
data.to_csv('../date/train_prelucrat2.csv', index=False)

data = pd.read_csv('../date/train_prelucrat2.csv')
data['Age_interval'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

## Numararea persoanelor în fiecare categorie de varsta
passengers_per_cat = data['Age_interval'].value_counts().sort_index()

## Afisare terminal:
print(f"Numărul de pasageri în fiecare categorie de varsta: {passengers_per_cat.to_string()}")

## Histograma pasageri in fiecare categorie de varsta
plt.figure(figsize=(10, 10))
passengers_per_cat.plot(kind='bar', color='skyblue')
plt.title('Numarul de pasageri in fiecare categorie de varsta')
plt.xlabel('Categoriile de varsta')
plt.ylabel('Numar pasageri')
plt.xticks(rotation=0)

## Adaugarea valorilor deasupra barelor

for i, count in enumerate(passengers_per_cat):
    plt.text(i, count + 2, str(count), ha='center', va='bottom')

plt.savefig("../date/cerinta5/IntervaleVarsteBarbatiSupr.png")