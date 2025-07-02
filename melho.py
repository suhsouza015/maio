import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Análise de Preços",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Análise Interativa de Preços")

# Upload da planilha
uploaded_file = st.sidebar.file_uploader("📂 Envie sua planilha Excel (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        df_maio = pd.read_excel(uploaded_file)

        if "Preço à vista" not in df_maio.columns or "Preço a prazo" not in df_maio.columns or "Produto" not in df_maio.columns:
            st.error("❌ A planilha deve conter as colunas: 'Produto', 'Preço à vista' e 'Preço a prazo'.")
        else:
            # Tabs principais
            aba1, aba2 = st.tabs(["📊 Análise de Preços", "🔍 Filtro por Produto"])

            # -------------- ABA 1 ---------------
            with aba1:
                st.subheader("📈 Gráficos e Tabela Filtrada")

                mxpre = df_maio["Preço à vista"].max()
                mnpre = df_maio["Preço à vista"].min()

                valor_slider = st.sidebar.slider(
                    "🔽 Filtrar por preço à vista até:",
                    float(mnpre), float(mxpre), float(mxpre)
                )

                df_filtrado = df_maio[df_maio["Preço à vista"] <= valor_slider]

                st.markdown(f"**💡 Total de itens após filtro:** `{len(df_filtrado)}`")

                st.dataframe(df_filtrado, use_container_width=True)

                col1, col2 = st.columns(2)

                with col1:
                    fig1 = px.bar(
                        df_filtrado["Preço a prazo"].value_counts().sort_index(),
                        title="📊 Frequência dos Preços a Prazo",
                        labels={'x': 'Preço a Prazo', 'y': 'Frequência'}
                    )
                    st.plotly_chart(fig1, use_container_width=True)

                with col2:
                    fig2 = px.histogram(
                        df_filtrado,
                        x="Preço à vista",
                        nbins=20,
                        title="📉 Distribuição de Preços à Vista"
                    )
                    st.plotly_chart(fig2, use_container_width=True)

            # -------------- ABA 2 ---------------
            with aba2:
                st.subheader("🔍 Filtro por Produto e Preço")

                produtos = df_maio["Produto"].dropna().unique()
                produto_escolhido = st.sidebar.selectbox("🛒 Escolha um Produto", sorted(produtos))

                df_produto = df_maio[df_maio["Produto"] == produto_escolhido]

                precos = df_produto["Preço à vista"].dropna().unique()
                preco_escolhido = st.sidebar.selectbox("💰 Escolha um Preço à Vista", sorted(precos))

                resultado = df_produto[df_produto["Preço à vista"] == preco_escolhido]

                st.markdown(f"**🔎 Resultado:** `{len(resultado)}` registro(s) encontrado(s)")
                st.dataframe(resultado, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")

else:
    st.info("📁 Envie um arquivo .xlsx na barra lateral para começar.")
