import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cerinta 10
data = pd.read_csv('train_prelucrat.csv')

is_alone_list = []

for index, row in data.iterrows():
    if row['SibSp'] + row['Parch'] == 0:
        is_alone_list.append(True)
    else:
        is_alone_list.append(False)

## Folosim dataframe-ul
data['IsAlone'] = is_alone_list

## Histograma pentru pasageri
plt.figure(figsize=(8, 6))
ax = sns.histplot(data=data, x='Survived', hue='IsAlone', multiple='stack', bins=2,  palette=['skyblue', 'orange'])
plt.title('Sansele de supravietuire pentru persoanele singure')
plt.xlabel('Supravietuire')
plt.ylabel('Numar de pasageri')
plt.xticks([0.25, 0.75], [0, 1])
plt.legend(['Impreuna cu cineva', 'Singuri'])

## Adaugare procentaj in fiecare dreptunghi
for rect in ax.containers:
    ax.bar_label(rect, fmt='%d', label_type='edge')

plt.savefig("./cerinta10/InfluentareSiguratate.png")

## Selectie de volum n = 100
data_subset = data.head(100)

## Crearea unui catplot pentru a investiga relația dintre tarif, clasă și supraviețuire
plt.figure(figsize=(10, 10))
sns.catplot(data=data_subset, x='Pclass', y='Fare', hue='Survived', col='Survived', kind='swarm', palette=['skyblue', 'orange'])
plt.subplots_adjust(top=0.8)
plt.suptitle('Relatia dintre tarif, clasa si supravietuire pentru primele 100 de inregistrari', fontsize=16)

plt.savefig("./cerinta10/RelatieVariabileAl.png")