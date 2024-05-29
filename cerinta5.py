import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 5
data = pd.read_csv('train_prelucrat.csv')

# Definirea categoriilor de vârstă și a valorii maxime
bins = [0, 20, 40, 60, 80]
labels = ['0-20', '21-40', '41-60', '61-80']

# Adăugarea coloanei 'Age_Category' care indică categoria de vârstă
data['Age_Category'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Adaugare coloana in tabel
data.to_csv('train_prelucrat2.csv', index=False)












data = pd.read_csv('train_prelucrat2.csv')

data['Age_Category'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Numărarea persoanelor în fiecare categorie de vârstă
passengers_per_category = data['Age_Category'].value_counts().sort_index()

# Afișarea rezultatelor
print("Numărul de pasageri în fiecare categorie de vârstă:")
print(passengers_per_category)

# Generarea unui grafic pentru a evidenția aceste rezultate
passengers_per_category.plot(kind='bar', color='skyblue')
plt.title('Numărul de pasageri în fiecare categorie de vârstă')
plt.xlabel('Categorie de vârstă')
plt.ylabel('Număr de pasageri')
plt.xticks(rotation=0)
plt.show()