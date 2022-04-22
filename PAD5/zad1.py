import pandas as pd

if __name__ == '__main__':

    print('============zad1===========')
    dataframe = pd.read_csv('orders.csv')
    print(dataframe.describe())
    print(dataframe.info())
    print(dataframe.head(5))

    print('============zad1a===========')
    dataframe['order_date'] = pd.to_datetime(dataframe['order_date'], format='%Y-%m-%d')
    print(dataframe.head(5))

    print('============zad1b===========')
    print(dataframe['tshirt_category'].value_counts())

    print('============zad1c===========')
    my_dict = {'White ': 'Wh ', 'Black ': 'Bl ', 'T-Shirt': 'Tshirt'}
    for (k, v) in my_dict.items():
        dataframe['tshirt_category'] = dataframe['tshirt_category'].apply(lambda f: f.replace(v, k))
    print(dataframe['tshirt_category'].value_counts())

    print('============zad1d===========')
    # zamiast size powinno być gender?
    # pd.set_option('display.max_columns', None)
    dataframe[['tshirt_colour', 'tshirt_type', 'tshirt_gender']] = dataframe['tshirt_category'].str.split(' ', expand=True)
    dataframe.drop(columns='tshirt_category', inplace=True)
    print(dataframe.head(20))

    print('============zad1e===========')
    mask = (dataframe['order_date'] >= '2014/12/31') & (dataframe['order_date'] <= '2016/08/02')
    print(dataframe.loc[mask])



