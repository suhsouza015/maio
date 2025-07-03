
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="SunnieExcel", layout="wide")

st.markdown("""
# 📊 Analisador Avançado de Planilhas Excel
Envie sua planilha e aplique filtros avançados com gráficos dinâmicos.
""")

uploaded_file = st.sidebar.file_uploader("📁 Envie seu arquivo Excel (.xlsx)", type=["xlsx"])

def filtro_numerico(df, col):
    st.sidebar.markdown(f"**Filtro numérico para `{col}`**")
    op = st.sidebar.selectbox(f"Operador para {col}", ["≥", "≤", "=", "Entre"])
    if op == "Entre":
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        val_min, val_max = st.sidebar.slider(f"Intervalo para {col}", min_val, max_val, (min_val, max_val))
        return df[(df[col] >= val_min) & (df[col] <= val_max)]
    elif op == "≥":
        val = st.sidebar.number_input(f"Valor mínimo para {col}", value=float(df[col].min()))
        return df[df[col] >= val]
    elif op == "≤":
        val = st.sidebar.number_input(f"Valor máximo para {col}", value=float(df[col].max()))
        return df[df[col] <= val]
    else:  # '='
        val = st.sidebar.number_input(f"Valor exato para {col}", value=float(df[col].median()))
        return df[df[col] == val]

def filtro_categorico(df, col):
    st.sidebar.markdown(f"**Filtro categórico para `{col}`**")
    opcoes = df[col].dropna().unique().tolist()
    selecao = st.sidebar.multiselect(f"Selecionar valores para {col}", opcoes, default=opcoes)
    return df[df[col].isin(selecao)]

def filtro_data(df, col):
    st.sidebar.markdown(f"**Filtro de datas para `{col}`**")
    min_date = df[col].min()
    max_date = df[col].max()
    dt_range = st.sidebar.date_input(f"Selecione intervalo para {col}", [min_date, max_date])
    if len(dt_range) == 2:
        return df[(df[col] >= pd.to_datetime(dt_range[0])) & (df[col] <= pd.to_datetime(dt_range[1]))]
    return df

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        if df.empty:
            st.warning("⚠️ Arquivo vazio.")
        else:
            st.write(f"### Preview ({len(df)} registros)")
            st.dataframe(df.head())

            # Detecta tipos das colunas para filtro
            filtros_selecionados = st.sidebar.multiselect("Colunas para filtrar", df.columns.tolist())

            df_filtrado = df.copy()

            with st.sidebar.expander("Filtros avançados", expanded=True):
                for col in filtros_selecionados:
                    if pd.api.types.is_numeric_dtype(df[col]):
                        df_filtrado = filtro_numerico(df_filtrado, col)
                    elif pd.api.types.is_datetime64_any_dtype(df[col]):
                        df_filtrado = filtro_data(df_filtrado, col)
                    else:
                        df_filtrado = filtro_categorico(df_filtrado, col)

            st.markdown(f"### Dados filtrados: {len(df_filtrado)} registros")
            st.dataframe(df_filtrado)

            if len(df_filtrado) > 0:
                st.sidebar.markdown("---")
                st.sidebar.markdown("### Configuração do gráfico")
                col_grafico = st.sidebar.selectbox("Coluna para gráfico", df_filtrado.columns)

                tipo_grafico = st.sidebar.radio(
                    "Tipo de gráfico",
                    ["Automático", "Histograma", "Barras", "Pizza"]
                )

                if tipo_grafico == "Automático":
                    if pd.api.types.is_numeric_dtype(df_filtrado[col_grafico]):
                        tipo_grafico = "Histograma"
                    else:
                        tipo_grafico = "Barras"

                # Paleta legal e simples
                cores = px.colors.qualitative.Pastel

                if tipo_grafico == "Histograma":
                    fig = px.histogram(df_filtrado, x=col_grafico, title=f"Histograma de {col_grafico}",
                                       color_discrete_sequence=cores)
                elif tipo_grafico == "Barras":
                    vc = df_filtrado[col_grafico].value_counts()
                    fig = px.bar(vc, x=vc.index, y=vc.values,
                                 labels={'x': col_grafico, 'y': 'Contagem'},
                                 title=f"Contagem de {col_grafico}",
                                 color_discrete_sequence=cores)
                else:  # Pizza
                    vc = df_filtrado[col_grafico].value_counts()
                    fig = px.pie(names=vc.index, values=vc.values, title=f"Distribuição de {col_grafico}",
                                 color_discrete_sequence=cores)

                st.plotly_chart(fig, use_container_width=True)

            else:
                st.warning("⚠️ Nenhum dado após filtro.")

    except Exception as e:
        st.error(f"❌ Erro ao processar arquivo: {e}")

else:
    st.info("Envie um arquivo Excel para começar.")

