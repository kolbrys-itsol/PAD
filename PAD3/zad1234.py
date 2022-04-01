import pandas as pd

# zad 1
print('===zad1===')
file = pd.read_csv('PAD_03_PD.csv', sep=';')
# print(file.head(20))
# print(file.describe())
print(file['Country'].value_counts())

# zad 2
print('===zad2===')
file['owned_goods'] = file['owns_car'] + file['owns_TV'] + file['owns_house'] + file['owns_Phone']
print(file.head(20))

# zad 3
print('===zad3===')
print(file.groupby('gender').agg({'owned_goods': 'mean'}).round(2))

# zad 4
print('===zad4===')
print(file.groupby('Country').agg({'owned_goods': 'mean', 'Age': 'min'}).round(2))
