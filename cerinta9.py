import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 9:
data = pd.read_csv('train_prelucrat2.csv')

data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

map_title_to_gender = {}

for title in data['Title'].unique():
    mode_gender = data[data['Title'] == title]['Sex'].mode()

    if not mode_gender.empty:
        gender = mode_gender[0]
    else:
        gender = mode_gender[1]
    
    map_title_to_gender[title] = gender

print(map_title_to_gender)

title_counts = data['Title'].value_counts()

plt.figure(figsize=(10, 10))
title_counts.plot(kind='bar', color='skyblue')
plt.title('Numarul de persoane pentru fiecare titlu de nobilime')
plt.xlabel('Titlu de nobilime')
plt.ylabel('Numar de persoane')
plt.xticks(rotation=45, ha='right')

## Adaugarea valorilor deasupra barelor

for i, count in enumerate(title_counts):
    plt.text(i, count + 2, str(count), ha='center', va='bottom')

plt.savefig("cerinta9/MatchingTitles.png")