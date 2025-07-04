import streamlit as st
import pandas as pd
import altair as alt
from io import BytesIO

st.set_page_config(page_title="SunniExcel", layout="wide")
st.title("🌞 SunniExcel — Sua Planilha Inteligente e Visual")

# Upload ou criação
st.sidebar.header("📥 Upload ou Criação")
arquivo = st.sidebar.file_uploader("Envie um .xlsx", type=["xlsx"])

if arquivo:
    df = pd.read_excel(arquivo)
    df = df.apply(lambda x: x.round(2) if pd.api.types.is_numeric_dtype(x) else x)
    st.session_state.df_editado = df.copy()
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=df.index, columns=df.columns)
elif "df_editado" not in st.session_state:
    st.sidebar.header("🧩 Criar nova planilha")
    linhas = st.sidebar.number_input("Linhas", 1, 100, 5)
    colunas = st.sidebar.number_input("Colunas", 1, 20, 3)
    nomes = [st.sidebar.text_input(f"Coluna {i+1}", f"Coluna {i+1}") for i in range(colunas)]
    df = pd.DataFrame([["" for _ in range(colunas)] for _ in range(linhas)], columns=nomes)
    st.session_state.df_editado = df.copy()
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=df.index, columns=df.columns)

df_editado = st.session_state.df_editado
celulas_modificadas = st.session_state.celulas_modificadas

# Editor de dados
st.subheader("📝 Editar dados")
df_editado = st.data_editor(df_editado, num_rows="dynamic", use_container_width=True)
st.session_state.df_editado = df_editado

# Colunas visíveis
st.subheader("👁️ Colunas visíveis")
colunas_visiveis = st.multiselect("Selecionar colunas para exibição", df_editado.columns.tolist(), default=df_editado.columns.tolist())

# Operações
st.subheader("🧮 Regras de Operação com Filtro Específico")
col_numericas = df_editado.select_dtypes(include="number").columns.tolist()
col_categoricas = df_editado.select_dtypes(include=["object", "category"]).columns.tolist()

num_ops = st.number_input("Número de operações", 0, 10, 0)
regras = []

for i in range(int(num_ops)):
    col = st.selectbox("Coluna Numérica", ["(nenhuma)"] + col_numericas, key=f"colop{i}")
    tipo = st.selectbox("Tipo", ["Soma", "Subtração", "Multiplicação", "Divisão", "Porcentagem"], key=f"tipoop{i}")
    val = st.number_input("Valor", format="%.2f", key=f"valop{i}")
    if col_categoricas:
        cat = st.selectbox("Coluna categórica (opcional)", ["(nenhuma)"] + col_categoricas, key=f"catop{i}")
        if cat != "(nenhuma)":
            valores = df_editado[cat].dropna().unique().tolist()
            filtro_vals = st.multiselect("Filtrar valores", valores, key=f"valcat{i}")
        else:
            cat, filtro_vals = None, []
    else:
        cat, filtro_vals = None, []
    regras.append({"col": col, "tipo": tipo, "val": val, "cat": cat, "filtros": filtro_vals})

# Aplicar regras
if st.button("⚡ Aplicar operações"):
    for r in regras:
        col, tipo, val, cat, filtros = r.values()
        try:
            filtro = df_editado[cat].isin(filtros) if cat and filtros else pd.Series([True] * len(df_editado))
            if col != "(nenhuma)":
                if tipo == "Soma":
                    df_editado.loc[filtro, col] += val
                elif tipo == "Subtração":
                    df_editado.loc[filtro, col] -= val
                elif tipo == "Multiplicação":
                    df_editado.loc[filtro, col] *= val
                elif tipo == "Divisão" and val != 0:
                    df_editado.loc[filtro, col] /= val
                elif tipo == "Porcentagem":
                    df_editado.loc[filtro, col] *= (1 + val / 100)

                celulas_modificadas.loc[df_editado.index[filtro], col] = True
        except Exception as e:
            st.warning(f"Erro em {col}: {e}")

    # Atualiza visualização
    st.session_state.df_editado = df_editado
    st.session_state.celulas_modificadas = celulas_modificadas
    st.success("✅ Regras aplicadas com sucesso!")

# Atualizar visualização
df_editado = st.session_state.df_editado
celulas_modificadas = st.session_state.celulas_modificadas
df_visivel = df_editado[colunas_visiveis]

# Regras visuais
st.subheader("🎯 Regras Visuais")
regras_visual = []
qtd_visuais = st.number_input("Regras visuais", 0, 5, 0)

for i in range(int(qtd_visuais)):
    colv = st.selectbox("Coluna Numérica", col_numericas, key=f"colv{i}")
    op = st.selectbox("Operador", [">", "<", ">=", "<=", "==", "!="], key=f"opv{i}")
    valv = st.number_input("Valor", key=f"valv{i}")
    cor = st.radio("Cor de destaque", ["Verde", "Vermelha"], key=f"corv{i}")
    regras_visual.append({"col": colv, "op": op, "val": valv, "cor": cor})

def aplicar_estilos(row):
    estilos = []
    for col in df_visivel.columns:
        estilo = ""
        if col in celulas_modificadas.columns and celulas_modificadas.at[row.name, col]:
            estilo = "background-color: mediumorchid; color: white;"
        else:
            for r in regras_visual:
                try:
                    if col == r["col"]:
                        v = row[col]
                        if eval(f"v {r['op']} {r['val']}"):
                            estilo = "background-color: lightgreen" if r["cor"] == "Verde" else "background-color: salmon"
                except:
                    pass
        estilos.append(estilo)
    return estilos

# Visualização final
st.subheader("📋 Visualização Final")
if regras_visual or celulas_modificadas.any().any():
    df_final = df_visivel.style.format(precision=2).apply(aplicar_estilos, axis=1)
else:
    df_final = df_visivel.style.format(precision=2)
st.dataframe(df_final, use_container_width=True)

# Gráfico de Linha (existente)
if len(col_numericas) >= 2:
    st.subheader("📊 Gráfico de Linha Interativo")
    x = st.selectbox("Eixo X", col_numericas, key="xgraf")
    y = st.selectbox("Eixo Y", col_numericas, key="ygraf")
    grafico = alt.Chart(df_editado).mark_line(point=True).encode(
        x=x, y=y, tooltip=list(df_editado.columns)
    ).properties(width=700, height=400)
    st.altair_chart(grafico, use_container_width=True)

## 🥧 Gráfico de Pizza com Filtros

if col_categoricas: # Só mostra a opção de gráfico de pizza se houver colunas categóricas
    st.subheader("🥧 Gráfico de Pizza")

    # Seleção da coluna categórica para as fatias
    col_categoria_pizza = st.selectbox(
        "Selecione a coluna para as fatias do gráfico de pizza",
        ["(nenhuma)"] + col_categoricas,
        key="col_pizza_cat"
    )

    if col_categoria_pizza != "(nenhuma)":
        # Seleção opcional da coluna numérica para o valor das fatias
        col_valor_pizza = st.selectbox(
            "Selecione a coluna numérica para o valor das fatias (opcional)",
            ["(nenhuma)"] + col_numericas,
            key="col_pizza_val"
        )

        # Filtro para os valores da coluna categórica
        valores_filtro_pizza = df_editado[col_categoria_pizza].dropna().unique().tolist()
        filtro_pizza_selecionados = st.multiselect(
            f"Filtrar valores para '{col_categoria_pizza}'",
            valores_filtro_pizza,
            default=valores_filtro_pizza,
            key="filtro_pizza_vals"
        )

        # Aplicar filtro ao DataFrame
        df_pizza = df_editado[df_editado[col_categoria_pizza].isin(filtro_pizza_selecionados)]

        if not df_pizza.empty:
            if col_valor_pizza != "(nenhuma)":
                # Agrupando e somando para o gráfico de pizza
                df_agrupado_pizza = df_pizza.groupby(col_categoria_pizza)[col_valor_pizza].sum().reset_index()
                # Criando o gráfico de pizza com base na soma
                chart_pizza = alt.Chart(df_agrupado_pizza).mark_arc().encode(
                    theta=alt.Theta(field=col_valor_pizza, type="quantitative"),
                    color=alt.Color(field=col_categoria_pizza, type="nominal", title="Categoria"),
                    tooltip=[col_categoria_pizza, alt.Tooltip(col_valor_pizza, format=".2f")] # Formata tooltip
                ).properties(
                    title=f"Distribuição de {col_valor_pizza} por {col_categoria_pizza}"
                )
            else:
                # Contando ocorrências se nenhuma coluna de valor for selecionada
                df_agrupado_pizza = df_pizza[col_categoria_pizza].value_counts().reset_index()
                df_agrupado_pizza.columns = [col_categoria_pizza, "Contagem"]
                # Criando o gráfico de pizza com base na contagem
                chart_pizza = alt.Chart(df_agrupado_pizza).mark_arc().encode(
                    theta=alt.Theta(field="Contagem", type="quantitative"),
                    color=alt.Color(field=col_categoria_pizza, type="nominal", title="Categoria"),
                    tooltip=[col_categoria_pizza, "Contagem"]
                ).properties(
                    title=f"Contagem de ocorrências por {col_categoria_pizza}"
                )
            st.altair_chart(chart_pizza, use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir com os filtros selecionados.")
    else:
        st.info("Selecione uma coluna categórica para gerar o gráfico de pizza.")
