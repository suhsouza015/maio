import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analisador Dinâmico de Excel", layout="wide")

st.title("📂 Analisador Dinâmico de Planilhas Excel")

# Upload do arquivo
uploaded_file = st.sidebar.file_uploader("Envie seu arquivo .xlsx", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.sidebar.success("✅ Arquivo carregado com sucesso!")
        
        if df.empty:
            st.warning("⚠️ O arquivo está vazio.")
        else:
            st.write("### 📋 Preview dos dados")
            st.dataframe(df.head())

            # Seleção de colunas para filtro
            cols = df.columns.tolist()
            col_filter = st.sidebar.multiselect("Selecione colunas para filtrar", cols)

            df_filtrado = df.copy()

            # Aplica filtros dinâmicos conforme tipo da coluna
            for col in col_filter:
                if pd.api.types.is_numeric_dtype(df[col]):
                    min_val = float(df[col].min())
                    max_val = float(df[col].max())
                    faixa = st.sidebar.slider(f"Filtrar '{col}'", min_val, max_val, (min_val, max_val))
                    df_filtrado = df_filtrado[df_filtrado[col].between(faixa[0], faixa[1])]
                else:
                    opcoes = df[col].dropna().unique().tolist()
                    selecao = st.sidebar.multiselect(f"Selecionar valores de '{col}'", opcoes, default=opcoes)
                    df_filtrado = df_filtrado[df_filtrado[col].isin(selecao)]

            st.markdown(f"### 📊 Dados filtrados: {len(df_filtrado)} registros")
            st.dataframe(df_filtrado)

            # Opções para gráfico
            st.sidebar.markdown("---")
            st.sidebar.write("### Configuração do Gráfico")

            if len(df_filtrado) > 0:
                col_grafico = st.sidebar.selectbox("Coluna para gráfico", df_filtrado.columns)

                # Tipo do gráfico: histogram para numéricos, barra para categóricos
                tipo_grafico = st.sidebar.radio("Tipo de gráfico", options=["Automático", "Histograma", "Barras"])

                if tipo_grafico == "Automático":
                    if pd.api.types.is_numeric_dtype(df_filtrado[col_grafico]):
                        tipo_grafico = "Histograma"
                    else:
                        tipo_grafico = "Barras"

                if tipo_grafico == "Histograma":
                    fig = px.histogram(df_filtrado, x=col_grafico, title=f"Histograma de {col_grafico}")
                else:
                    # gráfico de barras com contagem de valores únicos
                    fig = px.bar(df_filtrado[col_grafico].value_counts().reset_index(),
                                 x='index', y=col_grafico,
                                 labels={'index': col_grafico, col_grafico: 'Contagem'},
                                 title=f"Contagem de {col_grafico}")

                st.plotly_chart(fig, use_container_width=True)

                # Botão para download dos dados filtrados
                csv = df_filtrado.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Baixar dados filtrados (CSV)",
                    data=csv,
                    file_name='dados_filtrados.csv',
                    mime='text/csv'
                )
            else:
                st.warning("⚠️ Não há dados para exibir após o filtro.")

    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")

else:
    st.info("📁 Envie um arquivo Excel para começar.")
