import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 7
data = pd.read_csv('train_prelucrat2.csv')

## Calcularea procentului copiilor aflati la bord
passengers = len(data)
children = len(data[data['Age'] < 18])
perc_child = round((children / passengers) * 100, 2)

## Calcularea ratei de supravietuire pentru copii si adulti
surv_rate = { "Copii" : round(data[data['Age'] < 18]['Survived'].mean() * 100, 2), "Adulti" : round(data[data['Age'] >= 18]['Survived'].mean() * 100, 2)}

## Afisare terminal:
print(f"Procentul copiilor aflați la bord: {perc_child}%")
print(f"Rata de supraviețuire pentru copii: {surv_rate['Copii']}%")
print(f"Rata de supraviețuire pentru adulti: {surv_rate['Adulti']}%")

## Grafic:
labels = ['Copii', 'Adulti']
surv_rate_list = [surv_rate['Copii'], surv_rate['Adulti']]

plt.figure(figsize=(10, 10))
plt.bar(labels, surv_rate_list, color=['skyblue', 'orange'])
plt.title('Rata de supraviețuire pentru copii si adulti')
plt.ylabel('Procent de supravietuire (%)')
plt.ylim(0, 100)

## Adaugarea valorilor procentuale deasupra barelor
for i, rate in enumerate(surv_rate_list): # Enumerate face obiectul iterabil
    plt.text(i, rate + 2, f'{round(rate, 2)}%', ha='center', va='bottom')

plt.savefig("./cerinta7/Da.png")
