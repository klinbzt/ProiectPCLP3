import pandas as pd
import matplotlib.pyplot as plt

# Cerinta 3:
data = pd.read_csv('train.csv')
data_uniq = data_uniq = data.drop_duplicates()
data_selected = data_uniq.select_dtypes(include=['int64', 'float64'])

for name in data_selected.columns:
    plt.figure(figsize=(10, 10))
    plt.hist(data_uniq[name].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histograma pentru "{name}"')
    # plt.xlabel('Valoare')
    # plt.ylabel('Număr de exemple')
    plt.grid(True)
    plt.show()
