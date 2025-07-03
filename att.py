import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import scipy.stats as stats
from sklearn.decomposition import PCA
import io

def aplicar_filtros(df, colunas):
    for col in colunas:
        if pd.api.types.is_numeric_dtype(df[col]):
            op = st.sidebar.selectbox(f"🔢 Operador para `{col}`", ["≥", "≤", "=", "Entre"], key=col)
            if op == "Entre":
                v_min, v_max = st.sidebar.slider(f"Intervalo para `{col}`", float(df[col].min()), float(df[col].max()), key=col+"_range")
                df = df[(df[col] >= v_min) & (df[col] <= v_max)]
            else:
                val = st.sidebar.number_input("Valor", float(df[col].median()), key=col+"_input")
                df = df[df[col] >= val] if op == "≥" else df[df[col] <= val] if op == "≤" else df[df[col] == val]
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            intervalo = st.sidebar.date_input(f"📅 Intervalo para `{col}`", [df[col].min(), df[col].max()], key=col+"_date")
            if len(intervalo) == 2:
                df = df[(df[col] >= pd.to_datetime(intervalo[0])) & (df[col] <= pd.to_datetime(intervalo[1]))]
        else:
            opcoes = df[col].dropna().unique().tolist()
            selecao = st.sidebar.multiselect(f"🔠 Selecionar para `{col}`", opcoes, default=opcoes, key=col+"_cat")
            df = df[df[col].isin(selecao)]
    return df

def detectar_outliers_iqr(df):
    outliers = pd.DataFrame()
    for col in df.select_dtypes(include=[np.number]).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        filtro = (df[col] < (q1 - 1.5 * iqr)) | (df[col] > (q3 + 1.5 * iqr))
        outliers = pd.concat([outliers, df[filtro]])
    return outliers.drop_duplicates()

def plot_dispersao(df, col_x, col_y):
    fig = px.scatter(df, x=col_x, y=col_y, trendline="ols", title=f"Dispersão: {col_x} vs {col_y}")
    st.plotly_chart(fig, use_container_width=True)

st.set_page_config(page_title="🔬 Analisador Avançado", layout="wide")
st.title("🔍 Analisador Avançado de Dados")
st.markdown("Carregue dados, explore, visualize, compare e interprete com ferramentas analíticas interativas.")

uploaded_file = st.sidebar.file_uploader("📁 Envie seu Excel ou CSV", type=["xlsx", "csv"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".xlsx"):
            xls = pd.ExcelFile(uploaded_file)
            abas = xls.sheet_names
            aba = st.sidebar.selectbox("🗂️ Aba", abas)
            df = pd.read_excel(xls, sheet_name=aba)
        else:
            df = pd.read_csv(uploaded_file)

        st.subheader("📝 Pré-visualização")
        st.dataframe(df.head(1000))

        colunas_filtraveis = st.sidebar.multiselect("🔎 Filtros", df.columns.tolist())
        df_filtrado = aplicar_filtros(df.copy(), colunas_filtraveis)
        st.markdown(f"### 🎯 {len(df_filtrado)} registros filtrados")
        st.dataframe(df_filtrado)

        # Estatísticas
        st.subheader("📐 Estatísticas Descritivas")
        st.dataframe(df_filtrado.describe().T.style.format(precision=2))

        # Gráficos
        st.subheader("📊 Visualizações")
        col_graf = st.multiselect("📌 Colunas para gráfico", df_filtrado.columns.tolist())
        tipo_graf = st.radio("Tipo", ["Histograma", "Barras", "Pizza"])
        for col in col_graf:
            if tipo_graf == "Histograma":
                st.plotly_chart(px.histogram(df_filtrado, x=col), use_container_width=True)
            elif tipo_graf == "Barras":
                contagem = df_filtrado[col].value_counts()
                st.plotly_chart(px.bar(x=contagem.index, y=contagem.values, labels={"x":col, "y":"Contagem"}), use_container_width=True)
            elif tipo_graf == "Pizza":
                contagem = df_filtrado[col].value_counts()
                st.plotly_chart(px.pie(names=contagem.index, values=contagem.values), use_container_width=True)

        # Correlação
        st.subheader("🔗 Correlação")
        numericas = df_filtrado.select_dtypes(include=[np.number])
        metodo = st.radio("Método", ["pearson", "spearman", "kendall"])
        correl = numericas.corr(method=metodo)
        st.dataframe(correl.style.background_gradient(cmap="RdBu_r").format(precision=2))

        # Outliers
        st.subheader("🚨 Outliers")
        outliers = detectar_outliers_iqr(df_filtrado)
        if not outliers.empty:
            st.dataframe(outliers)
        else:
            st.info("Nenhum outlier detectado.")

        # Dispersão
        st.subheader("📈 Dispersão + Regressão")
        col1 = st.selectbox("X", numericas.columns)
        col2 = st.selectbox("Y", numericas.columns, index=1)
        plot_dispersao(df_filtrado, col1, col2)

        # Teste estatístico
        st.subheader("🧪 Teste t de diferença entre grupos")
        cat_col = st.selectbox("Variável categórica", df_filtrado.select_dtypes(include="object").columns)
        num_col = st.selectbox("Variável numérica", numericas.columns)
        grupos = df_filtrado[cat_col].dropna().unique()
        if len(grupos) >= 2:
            grupo1 = df_filtrado[df_filtrado[cat_col] == grupos[0]][num_col]
            grupo2 = df_filtrado[df_filtrado[cat_col] == grupos[1]][num_col]
            stat, p = stats.ttest_ind(grupo1, grupo2)
            st.markdown(f"**Resultado**: t = {stat:.3f}, p = {p:.3f}")

        # PCA
        st.subheader("🧬 PCA - Redução Dimensional")
        if len(numericas.columns) >= 2:
            pca = PCA(n_components=2)
            componentes = pca.fit_transform(numericas)
            pca_df = pd.DataFrame(componentes, columns=["PC1", "PC2"])
            st.plotly_chart(px.scatter(pca_df, x="PC1", y="PC2", title="PCA (2 Componentes)"), use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao processar: {e}")
else:
    st.info("📎 Envie um arquivo Excel ou CSV para começar.")
