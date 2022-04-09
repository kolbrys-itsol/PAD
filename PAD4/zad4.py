import numpy as np
import pandas as pd

if __name__ == '__main__':
    # zad 4
    dataframe = pd.read_csv('Zadanie_4.csv', sep=';')
    df = dataframe.groupby('DoctorID').agg({'DateTime': ['min', 'max']})
    df.to_csv('Zadanie_4_Solution.csv')
    print(df)

