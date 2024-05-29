import pandas as pd
import matplotlib.pyplot as plt

## Cerinta 3:
data = pd.read_csv('train.csv')
data_uniq = data_uniq = data.drop_duplicates()

## Histograma 'Survived'
plt.figure(figsize=(10, 10))
data_uniq['Survived'].plot(kind='hist', bins=[-0.5, 0.5, 1.5], rwidth=0.8, title='Histogram (Survived)')
plt.xlabel('Survived')
plt.ylabel('Frequency')
plt.xticks([0, 1])
plt.grid(True)
plt.show()


## Histograma 'Pclass'
plt.figure(figsize=(10, 10))
data_uniq['Pclass'].plot(kind='hist', bins=[0.5, 1.5, 2.5, 3.5], rwidth=0.8, title='Histogram (Pclass)')
plt.xlabel('Pclass')
plt.ylabel('Frequency')
plt.xticks([1, 2, 3])
plt.grid(True)
plt.show()

## Histograma 'Age'
plt.figure(figsize=(30, 30))
data_uniq['Age'].plot(kind='hist', bins = list(range(1, 81)), rwidth = 0.6,  title='Histogram (Age)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.xticks(list(range(1, 81)))
plt.grid(True)
plt.show()

## Histogramă 'SibSp'
plt.figure(figsize=(10, 6))
data_uniq['SibSp'].plot(kind='hist', bins=30, title='Histogram (SibSp)')
plt.xlabel('SibSp')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# ## Histograma 'Parch'
# plt.figure(figsize=(10, 6))
# data_uniq['Parch'].plot(kind='hist', bins=30, title='Histogram of Parch')
# plt.xlabel('Parch')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()

# ## Histogramă 'Fare'
# plt.figure(figsize=(10, 6))
# data_uniq['Fare'].plot(kind='hist', bins=30, title='Histogram of Fare')
# plt.xlabel('Fare')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()