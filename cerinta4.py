import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 4
data = pd.read_csv('train_prelucrat.csv')

## Calculare numar valori lipsa + numar total
vals_mis = data.isnull().sum()
cols_mis = vals_mis[vals_mis > 0]
rows = len(data)
dead = data[data['Survived'] == 0]
surv = data[data['Survived'] == 1]
total_dead = len(dead)
total_surv = len(surv)

dead_mis = dead.isnull().sum()
surv_mis = surv.isnull().sum()

## Data frame-uri:

missing_info = pd.DataFrame({
    'Numar valori lipsa': cols_mis,
    'Procentaj valori lipsa (%)': round((cols_mis / rows) * 100, 2)
})

Tsurv_mis = pd.DataFrame({
    'Decedati (0)': dead_mis,
    'Supravietuitori (1)': surv_mis
})

Tsurv_mis_percentage = pd.DataFrame({
    'Decedati (0)': round((dead_mis / total_dead) * 100, 2),
    'Supravietuitori (1)': round((surv_mis / total_surv) * 100, 2)
})

## Afisare terminal:
print(f"Coloanele cu valori lipsa:\n{cols_mis.to_string()}")
print(f"\nNumarul si procentul valorilor lipsa:\n{missing_info}")
print(f"\nNumarul valorilor lipss pentru fiecare dintre cele doua clase (coloana Survived):\n{Tsurv_mis}")
print(f"\nProcentul valorilor lipsă pentru fiecare dintre cele două clase (coloana Survived):\n{Tsurv_mis_percentage}")

## Generare histograme pentru a vizualizarea rezultatelor
plt.figure(figsize=(12, 10))

## Subplot pentru numar valori lipsa
plt.subplot(2, 2, 1)
missing_info['Numar valori lipsa'].plot(kind='bar', color='skyblue')
plt.title('Numarul valorilor lipsa')
plt.ylabel('Numar valori lipsă')

## Adaugarea valorilor deasupra barelor
for i, count in enumerate(missing_info['Numar valori lipsa']):
    plt.text(i, count + 2, f'{count}', ha='center', va='bottom')

## Subplot pentru procentaj valorilor lipsa
plt.subplot(2, 2, 2)
missing_info['Procentaj valori lipsa (%)'].plot(kind='bar', color='orange')
plt.title('Procentaj valorilor lipsa (%)')
plt.ylabel('Procentaj valori lipsa (%)')

## Adaugarea valorilor deasupra barelor
for i, count in enumerate(missing_info['Procentaj valori lipsa (%)']):
    plt.text(i, count + 2, f'{count}', ha='center', va='bottom')

## Subplot pentru numărul valorilor lipsă în funcție de clasa Survived
plt.subplot(2, 2, 3)
Tsurv_mis.plot(kind='bar', color=['skyblue', 'orange'], ax=plt.gca())
plt.title('Numarul valorilor lipsa pentru clasa Survived')
plt.ylabel('Numar valori lipsă')
plt.legend(['Decedati (0)', 'Supravietuitori (1)'])

## Subplot pentru pprocentaj valorilor lipsă în funcție de clasa Survived
plt.subplot(2, 2, 4)
Tsurv_mis_percentage.plot(kind='bar', color=['skyblue', 'orange'], ax=plt.gca())
plt.title('Procentul valorilor lipsa pentru clasa Survived')
plt.ylabel('Procentaj valori lipsa (%)')
plt.legend(['Decedati (0)', 'Supravietuitori (1)'])

plt.tight_layout()
plt.savefig("./cerinta4/ColoaneLipsa")
