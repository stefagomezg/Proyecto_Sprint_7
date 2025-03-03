import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
#Filtrando los modelos de carros desde el año 2010
car_data_modern = car_data[car_data['model_year']>= 2010]
#Agrupando los datos por año
gp_by_year= car_data_modern.groupby('model_year')['model'].size().reset_index()

st.header('Analicemos modelos de carros modernos')

bar_button = st.button('Construir un diagrama de barras para los modelos de carros')

if bar_button: #Al hacer clic en el botón
    st.write('Creación de diagrama de barras para visualizar la cantidad de modelos de carros que se producen cada año')
    #Creación del diagrama
    fig1 = px.bar(gp_by_year, x= 'model_year', y='model', labels={'model_year': 'Año', 'model': 'Cantidad de carros'},color='model_year')
    #Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)
    
bar_button2 = st.button('Construir un diagrama de barras de las condiciones de cada tipo de carro')

#Agrupando los tipos de carros y las condiciones en las que se encuentran
gp_by_type = car_data_modern.groupby(['type','condition'])['model'].size().reset_index()

if bar_button2: #Al hacer clic en el botón
    st.write('Creación de diagrama de barras para visualizar las condiciones de cada tipo de carro')
    #Creación del diagrama
    fig2 = px.bar(gp_by_type, x= 'type', y='model', labels={'type': 'Tipo de carro', 'model': 'Cantidad de carros'},color='condition')
    #Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

build_dispersion_diagram = st.checkbox('Construir un diagrama de dispersión de precio y kilometraje')

if build_dispersion_diagram: #Al hacer clic en el checkbox
    st.write('Creación de diagrama de barras para ver la disperción de precio y kilometraje')
    #Creación del diagrama
    fig3 = px.scatter(car_data_modern, x="odometer", y="price")
    



    