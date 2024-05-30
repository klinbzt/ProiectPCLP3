import pandas as pd

# Cerinta 8:
data = pd.read_csv('../date/train_prelucrat2.csv')

cols_nums = data.select_dtypes(include=['number']).columns
cols_categories = data.select_dtypes(exclude=['number']).columns

## Trebuie exclusa coloana 'Survived' si cea de 'PassengerId'
for col in cols_nums:
    if col != 'Survived' and col != 'PassengerId':
        ## Calcularea mediei in functie de coloana 'Survived'
        mean_values_survived = data[data['Survived'] == 1][col].mean()
        mean_values_not_survived = data[data['Survived'] == 0][col].mean()

        mean_values_survived = mean_values_survived.astype(data[col].dtype)
        mean_values_not_survived = mean_values_not_survived.astype(data[col].dtype)

        ## Completam valorile respective
        if col == 'Age': ## Trebuie sa verificam, ca pentru numere intregi precum 'Age' media se ia drept intreg
            for index, row in data.iterrows():
                if row['Survived'] == 1 and pd.isnull(row[col]):
                    data.loc[index, col] = round(mean_values_survived)

            for index, row in data.iterrows():
                if row['Survived'] == 0 and pd.isnull(row[col]):
                    data.loc[index, col] = round(mean_values_not_survived)
        else:
            for index, row in data.iterrows():
                if row['Survived'] == 1 and pd.isnull(row[col]):
                    data.loc[index, col] = mean_values_survived

            for index, row in data.iterrows():
                if row['Survived'] == 0 and pd.isnull(row[col]):
                    data.loc[index, col] = mean_values_not_survived

## Completarea valorilor lipsă pentru celulele ce contin valori lipsa
for col in cols_categories:
    ## Calculare valorii cu frecventa cea mai mare pentru coloanele respective in functie de coloana 'Survived'
    mode_surv = None     
    mode_dead = None
    
    if not data[data['Survived'] == 1][col].mode().empty:
        mode_surv = data[data['Survived'] == 1][col].mode()[0]

    if not data[data['Survived'] == 0][col].mode().empty:
        mode_dead = data[data['Survived'] == 0][col].mode()[0]

    if mode_dead != None and mode_surv != None:
        for index, row in data.iterrows():
            if row['Survived'] == 1 and pd.isnull(row[col]):
                data.loc[index, col] = mode_surv

        for index, row in data.iterrows():
            if row['Survived'] == 0 and pd.isnull(row[col]):
                data.loc[index, col] = mode_dead
                

## Salvarea datelor modificate in train_prelucrat3.csv
data.to_csv('../date/train_prelucrat3.csv', index=False)