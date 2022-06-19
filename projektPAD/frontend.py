import streamlit as st
import pandas as pd
import time
import ast
import plotly.express as plot

content = st.sidebar.selectbox('Menu', ['Strona główna', 'Statystyki'])

if content == 'Strona główna':
    st.title('Strona główna')
    st.header('Witaj! Statystyki są dostępne po lewej.')
else:
    file = st.file_uploader('Wprowadź plik data.csv utworzony przez web scraper', type=['csv'])
    if file is not None:
        with st.spinner('Wczytuję plik...'):
            time.sleep(1)
        dataframe = pd.read_csv(file, sep=',')

        graph = st.selectbox('Wybierz rodzaj wykresu',
                             ['Wybierz', 'Szczegółowość tagów a popularność', 'Treści dla dorosłych', 'Scatter'])

        columns = dataframe.columns.to_list()
        if graph == 'Szczegółowość tagów a popularność':
            st.header('Szczegółowość tagów a popularność')
            st.subheader(
                'Zobaczmy czy istnieje związek między popularnością tytułu, a szczegółowością jego opisu/tagów. '
                'Maksymalna liczba ogólnych tagów to 30.')
            dataframe['Count'] = dataframe.Tags.transform(ast.literal_eval).str.len()
            fig = plot.line(dataframe, facet_row_spacing=0.05, x='Popularity', y='Count')
            # fig.update_yaxes(autorange="reversed")
            st.plotly_chart(fig)
            st.markdown('Widzimy, że im mniejsza popularność, tym większa szansa, że pozycja ma mniej szczegółowy opis.')
        elif graph == 'Treści dla dorosłych':
            mask_nsc = dataframe.Tags.apply(lambda x: 'No Sexual Content' in x)
            df2 = dataframe[mask_nsc]
            underage_count = df2.Id.count()
            adult_count = dataframe.Id.count() - underage_count
            df3 = pd.DataFrame.from_dict(
                {'Type': ['Adult', 'No adult content'], 'Quantity': [adult_count, underage_count]})
            fig = plot.bar(df3, x='Type', y='Quantity')
            st.header('Treści dla dorosłych')
            st.subheader(
                'Większość gier typu visual novel (zwłaszcza japońskich) zawiera treści dla dorosłych. '
                'Sprawdźmy jak to wygląda w przypadku 1500 najpopularniejszych gier na VNDB:')
            st.plotly_chart(fig)
