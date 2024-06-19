import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Carregar os dados
data = load_data('dados.csv')

# Título da Página
st.title('Análise de Segurança da Informação')

# Exibir o DataFrame
st.subheader('Dados de Ataques')
st.write(data)

# Gráfico de Barras: Número de Ataques por Ano e Tipo de Ataque
st.subheader('Número de Ataques por Ano e Tipo de Ataque')
year_attack_type = data.groupby(['Ano', 'Tipo de Ataque']).size().unstack()
st.bar_chart(year_attack_type)

# Seleção de País para Análise Cruzada
st.subheader('Análise por País')
pais = st.selectbox('Selecione um País', data['País'].unique())
data_pais = data[data['País'] == pais]

# Gráfico de Barras para o País Selecionado
st.subheader(f'Número de Ataques no {pais} por Ano e Tipo de Ataque')
year_attack_type_pais = data_pais.groupby(['Ano', 'Tipo de Ataque']).size().unstack()
st.bar_chart(year_attack_type_pais)
