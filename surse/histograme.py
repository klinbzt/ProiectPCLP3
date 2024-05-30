import pandas as pd
import matplotlib.pyplot as plt

## Cerinta 3:
data = pd.read_csv('../date/train_prelucrat.csv')
data_uniq = data_uniq = data.drop_duplicates()

## Histograma 'Survived'
plt.figure(figsize=(10, 10))
data_uniq['Survived'].plot(kind='hist', bins=[-0.5, 0.5, 1.5], rwidth=0.8, title='Histogram (Survived)')
plt.xlabel('Survived')
plt.ylabel('Frecventa')
plt.xticks([0, 1])
plt.grid(True)
plt.savefig("../date/cerinta3/Survived.png")

## Histograma 'Pclass'
plt.figure(figsize=(10, 10))
data_uniq['Pclass'].plot(kind='hist', bins=[0.5, 1.5, 2.5, 3.5], rwidth=0.8, title='Histogram (Pclass)')
plt.xlabel('Pclass')
plt.ylabel('Frecventa')
plt.xticks([1, 2, 3])
plt.grid(True)
plt.savefig("../date/cerinta3/PClass.png")

## Histograma 'Age'
plt.figure(figsize=(30, 30))
data_uniq['Age'].plot(kind='hist', bins = list(range(1, 81)), rwidth = 0.6,  title='Histogram (Age)')
plt.xlabel('Age')
plt.ylabel('Frecventa')
plt.xticks(list(range(1, 81)))
plt.grid(True)
plt.savefig("../date/cerinta3/Age.png")

## Histograma 'SibSp'
plt.figure(figsize=(10, 10))
data_uniq['SibSp'].plot(kind='hist', bins=30, title='Histogram (SibSp)')
plt.xlabel('SibSp')
plt.ylabel('Frecventa')
plt.grid(True)
plt.savefig("../date/cerinta3/SibSp.png")

## Histograma 'Parch'
plt.figure(figsize=(10, 10))
data_uniq['Parch'].plot(kind='hist', bins=30, title='Histogram (Parch)')
plt.xlabel('Parch')
plt.ylabel('Frecventa')
plt.grid(True)
plt.savefig("../date/cerinta3/Parch.png")
plt.close()

## Histograma 'Fare'
plt.figure(figsize=(10, 10))
data_uniq['Fare'].plot(kind='hist', bins=30, title='Histogram (Fare)')
plt.xlabel('Fare')
plt.ylabel('Frecventa')
plt.grid(True)
plt.savefig("../date/cerinta3/Fare.png")
