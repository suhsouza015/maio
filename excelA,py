import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import io

st.set_page_config(page_title="📈 Analisador Avançado Excel", layout="wide")

st.title("📊 Analisador Avançado de Planilhas Excel")
st.markdown("Envie sua planilha, aplique filtros, visualize gráficos e veja estatísticas sem sair do lugar.")

uploaded_file = st.sidebar.file_uploader("📁 Envie seu arquivo Excel (.xlsx)", type=["xlsx"])

def filtro_numerico(df, col):
    op = st.sidebar.selectbox(f"🔢 Operador para `{col}`", ["≥", "≤", "=", "Entre"], key=col+"_num")
    if op == "Entre":
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        v_min, v_max = st.sidebar.slider("Intervalo", min_val=min_val, max_val=max_val, value=(min_val, max_val), key=col+"_range")
        return df[(df[col] >= v_min) & (df[col] <= v_max)]
    val = st.sidebar.number_input("Valor", value=float(df[col].median()), key=col+"_input")
    if op == "≥":
        return df[df[col] >= val]
    elif op == "≤":
        return df[df[col] <= val]
    return df[df[col] == val]

def filtro_categorico(df, col):
    opcoes = df[col].dropna().unique().tolist()
    selecao = st.sidebar.multiselect(f"🔠 Selecionar para `{col}`", opcoes, default=opcoes, key=col+"_cat")
    return df[df[col].isin(selecao)]

def filtro_data(df, col):
    min_dt, max_dt = df[col].min(), df[col].max()
    intervalo = st.sidebar.date_input(f"📅 Intervalo para `{col}`", [min_dt, max_dt], key=col+"_date")
    if len(intervalo) == 2:
        return df[(df[col] >= pd.to_datetime(intervalo[0])) & (df[col] <= pd.to_datetime(intervalo[1]))]
    return df

if uploaded_file:
    try:
        xls = pd.ExcelFile(uploaded_file)
        abas = xls.sheet_names
        aba_selecionada = st.sidebar.selectbox("📄 Aba da planilha", abas)
        df = pd.read_excel(xls, sheet_name=aba_selecionada)

        if df.empty:
            st.warning("⚠️ A aba está vazia.")
            st.stop()

        # Salva estado da aba selecionada
        if "aba" not in st.session_state:
            st.session_state["aba"] = aba_selecionada
        else:
            st.session_state["aba"] = aba_selecionada

        st.subheader("📝 Editar Planilha")
        edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

        buffer_editado = io.BytesIO()
        edited_df.to_excel(buffer_editado, index=False, engine='openpyxl')
        buffer_editado.seek(0)

        st.download_button("📥 Baixar planilha editada", data=buffer_editado, file_name="planilha_editada.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        st.markdown("### 👀 Pré-visualização dos dados")
        st.dataframe(df.head(1000 if len(df) > 10000 else len(df)))

        colunas_filtraveis = st.sidebar.multiselect("🔎 Colunas para filtrar", df.columns.tolist(), key="filtros")
        df_filtrado = df.copy()

        if colunas_filtraveis:
            st.sidebar.markdown("🧪 **Filtros ativos**")
            for col in colunas_filtraveis:
                if pd.api.types.is_numeric_dtype(df[col]):
                    df_filtrado = filtro_numerico(df_filtrado, col)
                elif pd.api.types.is_datetime64_any_dtype(df[col]):
                    df_filtrado = filtro_data(df_filtrado, col)
                else:
                    df_filtrado = filtro_categorico(df_filtrado, col)

        st.markdown(f"### 🎯 Dados filtrados: {len(df_filtrado)} registros")
        st.dataframe(df_filtrado)

        # Exportar dados filtrados
        buffer_filtros = io.BytesIO()
        df_filtrado.to_excel(buffer_filtros, index=False, engine='openpyxl')
        buffer_filtros.seek(0)
        st.download_button("💾 Baixar dados filtrados", data=buffer_filtros, file_name="dados_filtrados.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        # Estatísticas
        st.markdown("### 📐 Resumo Estatístico")
        estat = df_filtrado.select_dtypes(include=[np.number])
        if not estat.empty:
            st.dataframe(estat.describe().T.style.format(precision=2), use_container_width=True)
        else:
            st.info("Nenhuma coluna numérica disponível para estatísticas.")

        # Gráficos em abas
        st.markdown("### 📊 Visualização Gráfica")
        colunas_graficas = st.multiselect("Selecionar colunas para gráficos", df_filtrado.columns.tolist(), key="graficos")
        tipo_grafico = st.radio("Tipo de gráfico", ["Automático", "Histograma", "Barras", "Pizza"], key="tipo_grafico")

        if colunas_graficas:
            abas = st.tabs(colunas_graficas)
            for i, col in enumerate(colunas_graficas):
                with abas[i]:
                    tipo = tipo_grafico
                    if tipo == "Automático":
                        tipo = "Histograma" if pd.api.types.is_numeric_dtype(df_filtrado[col]) else "Barras"
                    cores = px.colors.qualitative.Set3

                    if tipo == "Histograma":
                        fig = px.histogram(df_filtrado, x=col, color_discrete_sequence=cores)
                    elif tipo == "Barras":
                        contagem = df_filtrado[col].value_counts()
                        fig = px.bar(x=contagem.index, y=contagem.values, labels={'x': col, 'y': 'Contagem'}, color_discrete_sequence=cores)
                    else:
                        contagem = df_filtrado[col].value_counts()
                        fig = px.pie(names=contagem.index, values=contagem.values, color_discrete_sequence=cores)

                    fig.update_layout(title=f"{tipo} de {col}", height=500)
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Selecione colunas para visualizar gráficos.")
    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")
else:
    st.info("📎 Envie uma planilha Excel para começar.")
