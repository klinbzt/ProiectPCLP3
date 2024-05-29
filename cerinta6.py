import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 6
data = pd.read_csv('train_prelucrat2.csv')

# Definirea categoriilor de vârstă și a valorii maxime
bins = list(range(0, 81, 20))
labels = ['0-20', '21-40', '41-60', '61-80']

# Adăugarea coloanei 'Age_Category' care indică categoria de vârstă
data['Age_Category'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Filtrarea datelor pentru a include doar bărbații
male_data = data[data['Sex'] == 'male']

survived_males_per_category = male_data[male_data['Survived'] == 1].groupby('Age_Category').size()
total_males_per_category = male_data.groupby('Age_Category').size()

# Calcularea procentului de supraviețuire al bărbaților pentru fiecare categorie de vârstă
survival_percentage = round((survived_males_per_category / total_males_per_category) * 100, 2)

## Afișare terminal
print(f"Procentul de supraviețuire al bărbaților pentru fiecare categorie de vârstă:\n{survival_percentage}")

# Generarea unui grafic pentru a evidenția aceste rezultate
survival_percentage.plot(kind='bar', color='skyblue')
plt.title('Procentul de supraviețuire al bărbaților în funcție de categorie de vârstă')
plt.xlabel('Categorie de vârstă')
plt.ylabel('Procent de supraviețuire')
plt.xticks(rotation=0)
plt.savefig("./cerinta6/IntervaleVarsteBarbatiSupr.png")