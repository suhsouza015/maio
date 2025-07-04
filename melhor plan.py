import streamlit as st
import pandas as pd
import altair as alt
from io import BytesIO

st.set_page_config(page_title="SunniExcel", layout="wide")
st.title("🌞 SunniExcel — Sua Planilha Inteligente e Visual")

# --- 1. Inicialização do Estado da Sessão ---
if "df_editado" not in st.session_state:
    st.session_state.df_editado = pd.DataFrame([["" for _ in range(3)] for _ in range(5)], columns=["Coluna 1", "Coluna 2", "Coluna 3"])
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=st.session_state.df_editado.index, columns=st.session_state.df_editado.columns)
if "selecao_grafico" not in st.session_state:
    st.session_state.selecao_grafico = {}

# --- 2. Upload ou Criação de Planilha ---
st.sidebar.header("📥 Upload ou Criação")
arquivo = st.sidebar.file_uploader("Envie um .xlsx", type=["xlsx"])

if arquivo is not None:
    if "nome_arquivo_upload" not in st.session_state or st.session_state.nome_arquivo_upload != arquivo.name:
        try:
            df = pd.read_excel(arquivo)
            df = df.apply(lambda x: x.round(2) if pd.api.types.is_numeric_dtype(x) else x)
            st.session_state.df_editado = df.copy()
            st.session_state.celulas_modificadas = pd.DataFrame(False, index=df.index, columns=df.columns)
            st.session_state.selecao_grafico = {}
            st.session_state.nome_arquivo_upload = arquivo.name
            st.success(f"Arquivo '{arquivo.name}' carregado com sucesso!")
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}. Certifique-se de que é um arquivo Excel válido.")
            st.session_state.df_editado = pd.DataFrame([["" for _ in range(3)] for _ in range(5)], columns=["Coluna 1", "Coluna 2", "Coluna 3"])
            st.session_state.celulas_modificadas = pd.DataFrame(False, index=st.session_state.df_editado.index, columns=st.session_state.df_editado.columns)
            st.session_state.selecao_grafico = {}
            if "nome_arquivo_upload" in st.session_state:
                del st.session_state.nome_arquivo_upload
            st.rerun()

if "df_editado" not in st.session_state or st.sidebar.button("Criar nova planilha", key="create_new_df_btn"):
    st.sidebar.header("🧩 Criar nova planilha")
    linhas = st.sidebar.number_input("Linhas", 1, 100, 5, key="new_rows")
    colunas = st.sidebar.number_input("Colunas", 1, 20, 3, key="new_cols")
    nomes = [st.sidebar.text_input(f"Coluna {i+1}", f"Coluna {i+1}", key=f"new_col_name_{i}") for i in range(colunas)]
    df = pd.DataFrame([["" for _ in range(colunas)] for _ in range(linhas)], columns=nomes)
    st.session_state.df_editado = df.copy()
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=df.index, columns=df.columns)
    st.session_state.selecao_grafico = {}
    if "nome_arquivo_upload" in st.session_state:
        del st.session_state.nome_arquivo_upload
    st.rerun()

df_editado = st.session_state.df_editado
celulas_modificadas = st.session_state.celulas_modificadas

# --- 3. Editor de Dados ---
st.subheader("📝 Editar Dados")
df_editado = st.data_editor(df_editado, num_rows="dynamic", use_container_width=True, key="main_data_editor")
st.session_state.df_editado = df_editado

# --- 4. Seleção de Colunas Visíveis ---
st.subheader("👁️ Colunas Visíveis")
colunas_visiveis = st.multiselect("Selecionar colunas para exibição", df_editado.columns.tolist(), default=df_editado.columns.tolist())

# --- 5. Regras de Operação com Filtro Específico ---
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

if st.button("⚡ Aplicar operações"):
    for r in regras:
        col, tipo, val, cat, filtros = r.values()
        try:
            filtro = df_editado[cat].isin(filtros) if cat and filtros else pd.Series([True] * len(df_editado), index=df_editado.index)
            
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
            st.warning(f"Erro ao aplicar regra em {col}: {e}")

    st.session_state.df_editado = df_editado
    st.session_state.celulas_modificadas = celulas_modificadas
    st.success("✅ Regras aplicadas com sucesso!")
    st.rerun()

# --- 6. Regras Visuais (Condicionais) ---
st.subheader("🎯 Regras Visuais")
regras_visual = []
qtd_visuais = st.number_input("Número de regras visuais", 0, 5, 0)

for i in range(int(qtd_visuais)):
    colv = st.selectbox("Coluna Numérica", col_numericas, key=f"colv{i}")
    op = st.selectbox("Operador", [">", "<", ">=", "<=", "==", "!="], key=f"opv{i}")
    valv = st.number_input("Valor", key=f"valv{i}")
    cor = st.radio("Cor de destaque", ["Verde", "Vermelha"], key=f"corv{i}")
    regras_visual.append({"col": colv, "op": op, "val": valv, "cor": cor})

# --- 7. Lógica de Filtragem e Destaque da Visualização Final ---
df_para_visualizacao_final = df_editado.copy()

selected_category_from_url = st.query_params.get("selected_category", None)
selected_category_col_from_url = st.query_params.get("selected_category_col", None)

if selected_category_from_url and selected_category_col_from_url:
    st.session_state.selecao_grafico = {selected_category_col_from_url: selected_category_from_url}
    
    if selected_category_col_from_url in df_para_visualizacao_final.columns:
        df_para_visualizacao_final = df_para_visualizacao_final[
            df_para_visualizacao_final[selected_category_col_from_url].astype(str) == selected_category_from_url
        ]
else:
    if st.session_state.selecao_grafico:
        st.session_state.selecao_grafico = {}


df_visivel = df_para_visualizacao_final[colunas_visiveis]


def aplicar_estilos(row):
    estilos = []
    
    selecao_ativa = st.session_state.selecao_grafico and len(st.session_state.selecao_grafico) > 0
    campo_selecionado_grafico = list(st.session_state.selecao_grafico.keys())[0] if selecao_ativa else None
    valor_selecionado_grafico = st.session_state.selecao_grafico[campo_selecionado_grafico] if selecao_ativa else None

    for col in df_visivel.columns:
        estilo = ""
        if col in celulas_modificadas.columns and celulas_modificadas.at[row.name, col]:
            estilo = "background-color: mediumorchid; color: white;"
        else:
            for r in regras_visual:
                try:
                    if col == r["col"]:
                        v = row[col]
                        if pd.notna(v) and eval(f"v {r['op']} {r['val']}"):
                            estilo = "background-color: lightgreen;" if r["cor"] == "Verde" else "background-color: salmon;"
                except:
                    pass

        if selecao_ativa and campo_selecionado_grafico in row.index and str(row[campo_selecionado_grafico]) == valor_selecionado_grafico:
            estilo += "background-color: lightblue;" 

        estilos.append(estilo)
    return estilos

# --- 8. Visualização Final da Tabela ---
st.subheader("📋 Visualização Final")
if regras_visual or celulas_modificadas.any().any() or st.session_state.selecao_grafico:
    df_final_styled = df_visivel.style.format(precision=2).apply(aplicar_estilos, axis=1)
else:
    df_final_styled = df_visivel.style.format(precision=2)
st.dataframe(df_final_styled, use_container_width=True)

# Botão para limpar a seleção do gráfico
if st.session_state.selecao_grafico:
    if st.button("Limpar Filtro do Gráfico"):
        if "selected_category" in st.query_params:
            del st.query_params["selected_category"]
        if "selected_category_col" in st.query_params:
            del st.query_params["selected_category_col"]
        st.session_state.selecao_grafico = {}
        st.rerun()

# --- 9. Gráfico de Linha (apenas visualização) ---
if len(col_numericas) >= 2:
    st.subheader("📊 Gráfico de Linha")
    x = st.selectbox("Eixo X", col_numericas, key="xgraf")
    y = st.selectbox("Eixo Y", col_numericas, key="ygraf")
    grafico = alt.Chart(df_editado).mark_line(point=True).encode(
        x=x, y=y, tooltip=list(df_editado.columns)
    ).properties(width=700, height=400)
    st.altair_chart(grafico, use_container_width=True)


## 📊 Gráficos por Categoria (Apenas Visualização)


if col_categoricas:
    st.subheader("📊 Gráficos por Categoria (Apenas Visualização)")

    col_categoria_grafico = st.selectbox(
        "Selecione a coluna para categorizar o gráfico",
        ["(nenhuma)"] + col_categoricas,
        key="col_graf_cat"
    )

    if col_categoria_grafico != "(nenhuma)":
        col_valores_numericos_multi = st.multiselect(
            "Selecione as colunas numéricas para o valor (opcional)",
            col_numericas,
            key="col_graf_val_multi"
        )

        keyword_filter_graf = st.text_input(
            "Filtrar por palavra-chave (opcional, em qualquer coluna)",
            key="keyword_graf_filter"
        )

        df_filtrado_por_keyword_graf = df_editado.copy()
        if keyword_filter_graf:
            df_str_graf = df_editado.astype(str)
            mask_keyword_graf = df_str_graf.apply(lambda row: row.astype(str).str.contains(keyword_filter_graf, case=False, na=False).any(), axis=1)
            df_filtrado_por_keyword_graf = df_editado[mask_keyword_graf]
            if df_filtrado_por_keyword_graf.empty:
                st.warning(f"Nenhum dado encontrado com a palavra-chave '{keyword_filter_graf}'.")
                st.stop()

        valores_filtro_graf = df_filtrado_por_keyword_graf[col_categoria_grafico].dropna().unique().tolist()
        filtro_graf_selecionados = st.multiselect(
            f"Filtrar valores para '{col_categoria_grafico}'",
            valores_filtro_graf,
            default=valores_filtro_graf,
            key="filtro_graf_vals"
        )

        df_final_graf = df_filtrado_por_keyword_graf[df_filtrado_por_keyword_graf[col_categoria_grafico].isin(filtro_graf_selecionados)]

        if not df_final_graf.empty:
            tipo_grafico = st.radio("Escolha o tipo de gráfico", ["Pizza", "Barras Agrupadas"], key="tipo_visual_graf")

            selection_visual = alt.selection_point(fields=[col_categoria_grafico], on="click", empty="none")

            if tipo_grafico == "Pizza":
                if len(col_valores_numericos_multi) <= 1:
                    valor_campo = col_valores_numericos_multi[0] if col_valores_numericos_multi else "Contagem"
                    
                    if not col_valores_numericos_multi:
                        df_agrupado_pizza = df_final_graf[col_categoria_grafico].value_counts().reset_index()
                        df_agrupado_pizza.columns = [col_categoria_grafico, "Contagem"]
                    else:
                        df_agrupado_pizza = df_final_graf.groupby(col_categoria_grafico)[valor_campo].sum().reset_index()
                    
                    chart_pizza = alt.Chart(df_agrupado_pizza).mark_arc().encode(
                        theta=alt.Theta(field=valor_campo, type="quantitative"),
                        color=alt.Color(field=col_categoria_grafico, type="nominal", title="Categoria",
                                        legend=alt.Legend(title=col_categoria_grafico)),
                        tooltip=[
                            col_categoria_grafico,
                            alt.Tooltip(valor_campo, format=".2f", title="Valor"),
                        ],
                        opacity=alt.condition(selection_visual, alt.value(1), alt.value(0.2)),
                    ).add_params(
                        selection_visual
                    ).properties(
                        title=f"Distribuição de {valor_campo} por {col_categoria_grafico}"
                    )
                    
                    st.altair_chart(chart_pizza, use_container_width=True)

                else:
                    st.warning("Para Gráficos de Pizza com múltiplas colunas numéricas, será mostrada a soma total. Considere o Gráfico de Barras Agrupadas para comparação individual.")
                    df_temp_sum = df_final_graf.copy()
                    df_temp_sum['Total_Mlti_Colunas'] = df_temp_sum[col_valores_numericos_multi].sum(axis=1)
                    df_agrupado_pizza_multi = df_temp_sum.groupby(col_categoria_grafico)['Total_Mlti_Colunas'].sum().reset_index()
                    
                    selection_visual_multi = alt.selection_point(fields=[col_categoria_grafico], on="click", empty="none")

                    chart_pizza_multi = alt.Chart(df_agrupado_pizza_multi).mark_arc().encode(
                        theta=alt.Theta(field='Total_Mlti_Colunas', type="quantitative"),
                        color=alt.Color(field=col_categoria_grafico, type="nominal", title="Categoria",
                                        legend=alt.Legend(title=col_categoria_grafico)),
                        tooltip=[
                            col_categoria_grafico,
                            alt.Tooltip('Total_Mlti_Colunas', format=".2f", title="Soma Total"),
                        ],
                        opacity=alt.condition(selection_visual_multi, alt.value(1), alt.value(0.2)),
                    ).add_params(
                        selection_visual_multi
                    ).properties(
                        title=f"Soma Total das Colunas Selecionadas por {col_categoria_grafico}"
                    )
                    
                    st.altair_chart(chart_pizza_multi, use_container_width=True)


            elif tipo_grafico == "Barras Agrupadas":
                if col_valores_numericos_multi:
                    df_long = df_final_graf.melt(
                        id_vars=[col_categoria_grafico],
                        value_vars=col_valores_numericos_multi,
                        var_name="Métrica",
                        value_name="Valor"
                    )
                    df_agrupado_barras = df_long.groupby([col_categoria_grafico, "Métrica"])["Valor"].sum().reset_index()

                    selection_visual_bar = alt.selection_point(fields=[col_categoria_grafico], on="click", empty="none")

                    chart_barras = alt.Chart(df_agrupado_barras).mark_bar().encode(
                        x=alt.X(col_categoria_grafico, axis=alt.Axis(labels=True), title=""),
                        y=alt.Y("Valor", type="quantitative", title="Valor Total"),
                        color=alt.Color("Métrica", title="Métrica"),
                        column=alt.Column("Métrica", header=alt.Header(titleOrient="bottom", labelOrient="bottom"), title=""),
                        tooltip=[
                            col_categoria_grafico, "Métrica", alt.Tooltip("Valor", format=".2f"),
                        ],
                        opacity=alt.condition(selection_visual_bar, alt.value(1), alt.value(0.2)),
                    ).add_params(
                        selection_visual_bar
                    ).properties(
                        title=f"Valores de Múltiplas Colunas por {col_categoria_grafico}"
                    ).resolve_scale(
                        y="independent"
                    )
                    
                    st.altair_chart(chart_barras, use_container_width=True)

                else:
                    st.info("Selecione uma ou mais colunas numéricas para o gráfico de barras.")
        else:
            st.warning("Nenhum dado para exibir com os filtros selecionados.")
    else:
        st.info("Selecione uma coluna categórica para gerar os gráficos.")

# --- 10. Exportação do DataFrame ---
buffer = BytesIO()
# LINHA CORRIGIDA AQUI: engine="openpyxl"
df_editado.to_excel(buffer, index=False, engine="openpyxl") 
buffer.seek(0)
st.download_button(
    "⬇️ Baixar SunniExcel",
    data=buffer,
    file_name="SunniExcel_resultado.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
