import pandas as pd

if __name__ == '__main__':
    print('============zad2a===========')
    dataframe_old = pd.read_csv('orders.csv')
    dataframe = pd.read_csv('customers.csv')
    print(dataframe.columns)

    print('============zad2b===========')
    print(f'Rozmiar Orders {dataframe_old.shape}')
    print(f'Rozmiar Customers {dataframe.shape}')

    print('============zad2c===========')
    dataframe.rename(columns={"customerID": "customer_id"}, inplace=True)
    print(dataframe.columns)

    print('============zad2d===========')
    # concat nie dostarcza możliwości łączenia po wartościach w kolumnach więc wybrałem merge
    dataframe_merged = pd.merge(dataframe_old, dataframe, on='customer_id')
    print(dataframe_merged)

    print('============zad3===========')
    dataframe_merged.drop('customer_id', axis=1, inplace=True)
    dataframe_merged.to_csv('solution.csv')
