import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📂 Analisador Dinâmico de Planilhas Excel")

uploaded_file = st.file_uploader("Envie seu arquivo .xlsx", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.write("### Colunas encontradas:")
        st.write(df.columns.tolist())

        # Seleção dinâmica de colunas para filtrar
        col_filter = st.multiselect("Selecione colunas para filtrar", df.columns.tolist())

        df_filtrado = df.copy()

        # Para cada coluna selecionada, aplicar filtro conforme o tipo
        for col in col_filter:
            if pd.api.types.is_numeric_dtype(df[col]):
                min_val = float(df[col].min())
                max_val = float(df[col].max())
                faixa = st.slider(f"Filtrar valores da coluna '{col}'", min_val, max_val, (min_val, max_val))
                df_filtrado = df_filtrado[df_filtrado[col].between(faixa[0], faixa[1])]
            else:
                opcoes = df[col].dropna().unique().tolist()
                selecao = st.multiselect(f"Selecionar valores da coluna '{col}'", opcoes, default=opcoes)
                df_filtrado = df_filtrado[df_filtrado[col].isin(selecao)]

        st.write(f"### Dados filtrados: {len(df_filtrado)} registros")
        st.dataframe(df_filtrado)

        # Seleção para gráfico
        col_grafico = st.selectbox("Selecione coluna para gráfico", df_filtrado.columns)

        if pd.api.types.is_numeric_dtype(df_filtrado[col_grafico]):
            fig = px.histogram(df_filtrado, x=col_grafico, title=f"Histograma de {col_grafico}")
        else:
            fig = px.bar(df_filtrado[col_grafico].value_counts(), title=f"Frequência de {col_grafico}")

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
else:
    st.info("Envie um arquivo Excel para começar.")
