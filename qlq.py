import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

uploaded_file = st.sidebar.file_uploader("📂 Envie sua planilha Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    df_maio = pd.read_excel(uploaded_file)

    aba1, aba2 = st.tabs(["📊 Análise de Preços", "🔍 Filtro por Produto"])

    with aba1:
        st.title("📊 Análise de Preços - Maio")

        mxpre = df_maio["Preço à vista"].max()
        mnpre = df_maio["Preço à vista"].min()
        valor_slider = st.sidebar.slider("Filtrar: Preço à vista até", mnpre, mxpre, mxpre)

        df_pre = df_maio[df_maio["Preço à vista"] <= valor_slider]

        st.markdown("### 📈 Tabela Filtrada")
        st.dataframe(df_pre, use_container_width=True)

        fig = px.bar(df_pre["Preço a prazo"].value_counts(), title="Preço a Prazo - Frequência")
        fig2 = px.histogram(df_pre["Preço à vista"], title="Distribuição de Preços à Vista")

        col1, col2 = st.columns(2)
        col1.plotly_chart(fig, use_container_width=True)
        col2.plotly_chart(fig2, use_container_width=True)

    with aba2:
        st.title("🔍 Filtro por Produto e Preço")

        produtos = df_maio["Produto"].unique()
        produto_selecionado = st.sidebar.selectbox("Escolha um Produto", produtos)

        df_filtrado = df_maio[df_maio["Produto"] == produto_selecionado]

        precos_disponiveis = df_filtrado["Preço à vista"].unique()
        preco_selecionado = st.sidebar.selectbox("Escolha um Preço à Vista", sorted(precos_disponiveis))

        resultado = df_filtrado[df_filtrado["Preço à vista"] == preco_selecionado]

        st.markdown("### 📄 Resultado do Filtro")
        st.dataframe(resultado, use_container_width=True)

