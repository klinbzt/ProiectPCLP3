import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 6
data = pd.read_csv('train_prelucrat2.csv')

## Definirea categoriilor (intervale) de varsta 
bins = list(range(0, 81, 20))
labels = ['0-20', '21-40', '41-60', '61-80']

male_data = data[data['Sex'] == 'male'] # Includere doar barbati

survived_males_per_category = male_data[male_data['Survived'] == 1].groupby('Age_interval').size()
total_males_per_category = male_data.groupby('Age_interval').size()

survival_percentage = round((survived_males_per_category / total_males_per_category) * 100, 2)

## Afișare terminal
print(f"Procentul de supraviețuire al barbatilor pentru fiecare categorie de varsta:\n{survival_percentage.to_string()}")

## Histograma pentru procentul de supravietuire al barbatilor in functie de categorie de varsta
survival_percentage.plot(kind='bar', color='skyblue')
plt.title('Procentul de supravietuire al barbatilor in functie de categorie de varsta')
plt.xlabel('Categorie de varsta')
plt.ylabel('Procent de supravietuire')
plt.xticks(rotation=0)
plt.savefig("./cerinta6/IntervaleVarsteBarbatiSupr.png")