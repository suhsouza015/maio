import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Tabs na tela principal
aba1, aba2 = st.tabs(["📊 Análise de Preços", "🔍 Filtro por Produto"])

# ---------------------------
# ABA 1 – Gráficos e slider
# ---------------------------
with aba1:
    st.title("📊 Análise de Preços - Maio")
    
    df_maio = pd.read_excel("C:\\Users\\thiago\\Downloads\\pro.xlsx")

    # Slider para preço à vista
    mxpre = df_maio["Preço à vista"].max()
    mnpre = df_maio["Preço à vista"].min()
    valor_slider = st.sidebar.slider("Filtrar: Preço à vista até", mnpre, mxpre, mxpre)

    df_pre = df_maio[df_maio["Preço à vista"] <= valor_slider]

    st.markdown("### 📈 Tabela Filtrada")
    st.dataframe(df_pre, use_container_width=True)

    # Gráficos
    fig = px.bar(df_pre["Preço a prazo"].value_counts(), title="Preço a Prazo - Frequência")
    fig2 = px.histogram(df_pre["Preço à vista"], title="Distribuição de Preços à Vista")

    col1, col2 = st.columns(2)
    col1.plotly_chart(fig, use_container_width=True)
    col2.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# ABA 2 – Filtro por Produto e Preço
# ---------------------------
with aba2:
    st.title("🔍 Filtro por Produto e Preço")

    df_maio = pd.read_excel("C:\\Users\\thiago\\Downloads\\pro.xlsx")

    # Lista de produtos únicos
    produtos = df_maio["Produto"].unique()
    produto_selecionado = st.sidebar.selectbox("Escolha um Produto", produtos)

    # Filtra DataFrame por produto
    df_filtrado = df_maio[df_maio["Produto"] == produto_selecionado]

    # Lista de preços à vista disponíveis para o produto selecionado
    precos_disponiveis = df_filtrado["Preço à vista"].unique()
    preco_selecionado = st.sidebar.selectbox("Escolha um Preço à Vista", sorted(precos_disponiveis))

    # Filtra por preço à vista
    resultado = df_filtrado[df_filtrado["Preço à vista"] == preco_selecionado]

    st.markdown("### 📄 Resultado do Filtro")
    st.dataframe(resultado, use_container_width=True)
