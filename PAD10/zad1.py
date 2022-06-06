import streamlit as st
import pandas as pd
import time
import plotly.express as plot

content = st.sidebar.selectbox('Zawartość', ['Ankieta', 'Staty'])

if content == 'Ankieta':
    name = st.text_input('Podaj swoje imię: ')
    last_name = st.text_input('Podaj swoje nazwisko: ')

    if st.button('Ok'):
        st.success('Formularz poprawny')
        print(name, last_name)

else:
    file = st.file_uploader('Wprowadź dane', type=['csv'])
    if file is not None:
        with st.spinner('Poczekaj...'):
            time.sleep(1)
        dataframe = pd.read_csv(file, sep=',')

        graph = st.selectbox('Wybierz rodzaj wykresu', ['Wybierz', 'Kolumnowy', 'Scatter'])

        columns = dataframe.columns.to_list()
        if graph == 'Kolumnowy':
            x = st.selectbox('X', columns)
            y = st.selectbox('Y', columns)
            fig = plot.bar(dataframe, x=x, y=y)
            st.plotly_chart(fig)
        elif graph == 'Scatter':
            x = st.selectbox('X', columns)
            y = st.selectbox('Y', columns)
            fig = plot.scatter(dataframe, x=x, y=y)
            st.plotly_chart(fig)
