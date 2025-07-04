import streamlit as st
import pandas as pd
import altair as alt
from io import BytesIO
import numpy as np

st.set_page_config(page_title="SunniExcel", layout="wide")
st.title("🌞 SunniExcel — Sua Planilha Inteligente e Visual")

# --- 1. Inicialização do Estado da Sessão ---
if "df_editado" not in st.session_state:
    st.session_state.df_editado = pd.DataFrame([["" for _ in range(3)] for _ in range(5)], columns=["Coluna 1", "Coluna 2", "Coluna 3"])
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=st.session_state.df_editado.index, columns=st.session_state.df_editado.columns)
if "selecao_grafico" not in st.session_state:
    st.session_state.selecao_grafico = {}
if "nome_arquivo_upload" not in st.session_state:
    st.session_state.nome_arquivo_upload = None

# --- 2. Upload ou Criação de Planilha ---
st.sidebar.header("📥 Upload ou Criação")
arquivo = st.sidebar.file_uploader("Envie um .xlsx ou .csv", type=["xlsx", "csv"])

if arquivo is not None:
    if st.session_state.nome_arquivo_upload != arquivo.name:
        try:
            if arquivo.name.endswith('.xlsx'):
                df_carregado = pd.read_excel(arquivo)
            elif arquivo.name.endswith('.csv'):
                df_carregado = pd.read_csv(arquivo)
            
            st.session_state.df_editado = df_carregado.copy()
            st.session_state.celulas_modificadas = pd.DataFrame(False, index=df_carregado.index, columns=df_carregado.columns)
            st.session_state.selecao_grafico = {}
            st.session_state.nome_arquivo_upload = arquivo.name
            st.success(f"Arquivo '{arquivo.name}' carregado com sucesso!")
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}. Certifique-se de que é um arquivo Excel/CSV válido.")
            st.session_state.df_editado = pd.DataFrame([["" for _ in range(3)] for _ in range(5)], columns=["Coluna 1", "Coluna 2", "Coluna 3"])
            st.session_state.celulas_modificadas = pd.DataFrame(False, index=st.session_state.df_editado.index, columns=st.session_state.df_editado.columns)
            st.session_state.selecao_grafico = {}
            st.session_state.nome_arquivo_upload = None
            st.rerun()

if "df_editado" not in st.session_state or st.sidebar.button("Criar nova planilha", key="create_new_df_btn"):
    st.sidebar.header("🧩 Criar nova planilha")
    linhas = st.sidebar.number_input("Linhas", 1, 100, 5, key="new_rows")
    colunas = st.sidebar.number_input("Colunas", 1, 20, 3, key="new_cols")
    nomes = [st.sidebar.text_input(f"Coluna {i+1}", f"Coluna {i+1}", key=f"new_col_name_{i}") for i in range(colunas)]
    df_novo = pd.DataFrame([["" for _ in range(colunas)] for _ in range(linhas)], columns=nomes)
    st.session_state.df_editado = df_novo.copy()
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=df_novo.index, columns=df_novo.columns)
    st.session_state.selecao_grafico = {}
    st.session_state.nome_arquivo_upload = None
    st.rerun()

df_editado = st.session_state.df_editado
celulas_modificadas = st.session_state.celulas_modificadas

# --- 3. Limpeza de Dados Básica ---
st.sidebar.header("🧹 Limpeza de Dados")
if st.sidebar.button("Remover Linhas Duplicadas"):
    linhas_antes = len(df_editado)
    df_editado.drop_duplicates(inplace=True)
    st.session_state.df_editado = df_editado
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=df_editado.index, columns=df_editado.columns)
    st.sidebar.success(f"Removidas {linhas_antes - len(df_editado)} linhas duplicadas.")
    st.rerun()

st.sidebar.subheader("🔄 Converter Tipos de Coluna")
colunas_para_converter = st.sidebar.selectbox("Selecionar coluna para converter", ["(nenhuma)"] + df_editado.columns.tolist(), key="col_convert_type")

if colunas_para_converter != "(nenhuma)":
    tipo_alvo = st.sidebar.selectbox(
        f"Converter '{colunas_para_converter}' para:",
        ["(selecione)", "Número (Inteiro)", "Número (Decimal)", "Texto", "Data"],
        key="target_type"
    )
    if tipo_alvo != "(selecione)":
        if st.sidebar.button("Aplicar Conversão"):
            try:
                if tipo_alvo == "Número (Inteiro)":
                    df_editado[colunas_para_converter] = pd.to_numeric(df_editado[colunas_para_converter], errors='coerce').astype(pd.Int64Dtype())
                elif tipo_alvo == "Número (Decimal)":
                    df_editado[colunas_para_converter] = pd.to_numeric(df_editado[colunas_para_converter], errors='coerce')
                elif tipo_alvo == "Texto":
                    df_editado[colunas_para_converter] = df_editado[colunas_para_converter].astype(str)
                elif tipo_alvo == "Data":
                    df_editado[colunas_para_converter] = pd.to_datetime(df_editado[colunas_para_converter], errors='coerce')
                
                st.session_state.df_editado = df_editado
                st.sidebar.success(f"Coluna '{colunas_para_converter}' convertida para '{tipo_alvo}'.")
                st.rerun()
            except Exception as e:
                st.sidebar.error(f"Erro ao converter coluna: {e}. Verifique se os dados são compatíveis com o tipo alvo.")


preencher_nan_opcao = st.sidebar.radio(
    "Preencher valores ausentes (NaN)?",
    ["Não", "Com valor específico", "Com média (numérico)", "Com mediana (numérico)"]
)

if preencher_nan_opcao != "Não":
    colunas_com_nan = df_editado.columns[df_editado.isnull().any()].tolist()
    if colunas_com_nan:
        coluna_para_preencher = st.sidebar.selectbox("Selecionar coluna com NaN", colunas_com_nan)
        
        if preencher_nan_opcao == "Com valor específico":
            valor_para_preencher = st.sidebar.text_input(f"Valor para preencher NaN em '{coluna_para_preencher}'")
            if st.sidebar.button(f"Aplicar preenchimento '{coluna_para_preencher}'"):
                df_editado[coluna_para_preencher].fillna(valor_para_preencher, inplace=True)
                st.session_state.df_editado = df_editado
                st.sidebar.success(f"NaNs preenchidos em '{coluna_para_preencher}' com '{valor_para_preencher}'.")
                st.rerun()
        elif preencher_nan_opcao in ["Com média (numérico)", "Com mediana (numérico)"]:
            if pd.api.types.is_numeric_dtype(df_editado[coluna_para_preencher]):
                if preencher_nan_opcao == "Com média (numérico)":
                    valor_calc = df_editado[coluna_para_preencher].mean()
                else:
                    valor_calc = df_editado[coluna_para_preencher].median()
                
                if st.sidebar.button(f"Aplicar preenchimento '{coluna_para_preencher}' com {preencher_nan_opcao.split(' ')[1]}"):
                    df_editado[coluna_para_preencher].fillna(valor_calc, inplace=True)
                    st.session_state.df_editado = df_editado
                    st.sidebar.success(f"NaNs preenchidos em '{coluna_para_preencher}' com {valor_calc:.2f} ({preencher_nan_opcao.split(' ')[1]}).")
                    st.rerun()
            else:
                st.sidebar.warning(f"A coluna '{coluna_para_preencher}' não é numérica para aplicar média/mediana.")
    else:
        st.sidebar.info("Nenhuma coluna com valores ausentes (NaN) encontrada.")


# --- 4. Renomear Colunas ---
st.sidebar.header("✏️ Renomear Colunas")
colunas_atuais = df_editado.columns.tolist()
coluna_antiga = st.sidebar.selectbox("Selecionar coluna para renomear", ["(nenhuma)"] + colunas_atuais, key="col_rename_old")

if coluna_antiga != "(nenhuma)":
    nova_nome_coluna = st.sidebar.text_input(f"Novo nome para '{coluna_antiga}'", coluna_antiga, key="col_rename_new")
    if st.sidebar.button("Renomear Coluna"):
        if nova_nome_coluna and nova_nome_coluna != coluna_antiga:
            if nova_nome_coluna in df_editado.columns:
                st.sidebar.warning(f"O nome '{nova_nome_coluna}' já existe. Por favor, escolha um nome diferente.")
            else:
                df_editado.rename(columns={coluna_antiga: nova_nome_coluna}, inplace=True)
                if coluna_antiga in celulas_modificadas.columns:
                    celulas_modificadas.rename(columns={coluna_antiga: nova_nome_coluna}, inplace=True)
                st.session_state.df_editado = df_editado
                st.session_state.celulas_modificadas = celulas_modificadas
                st.sidebar.success(f"Coluna '{coluna_antiga}' renomeada para '{nova_nome_coluna}'.")
                st.rerun()
        else:
            st.sidebar.info("O novo nome não pode ser vazio ou igual ao nome atual.")


# --- 5. Editor de Dados Principal ---
st.subheader("📝 Editar Dados")
df_editado = st.data_editor(df_editado, num_rows="dynamic", use_container_width=True, key="main_data_editor")
st.session_state.df_editado = df_editado

# --- 6. Seleção de Colunas Visíveis ---
st.subheader("👁️ Colunas Visíveis")
colunas_visiveis = st.multiselect("Selecionar colunas para exibição", df_editado.columns.tolist(), default=df_editado.columns.tolist())

# --- 7. Regras de Operação com Filtro Específico ---
st.subheader("🧮 Regras de Operação com Filtro Específico")
# Atualiza as listas de colunas após possíveis conversões de tipo
col_numericas = df_editado.select_dtypes(include="number").columns.tolist()
col_categoricas = df_editado.select_dtypes(include=["object", "category"]).columns.tolist()
col_datas = df_editado.select_dtypes(include=["datetime64[ns]"]).columns.tolist()

# --- FILTRO GLOBAL DE PALAVRA-CHAVE PARA AS OPERAÇÕES ---
st.markdown("##### Aplicar filtro de palavra-chave nas operações:")
keyword_filter_op = st.text_input("Filtrar por palavra-chave (em qualquer coluna) antes de aplicar operações:", key="keyword_op_filter")
if keyword_filter_op:
    st.info(f"Operações serão aplicadas apenas às linhas que contêm '{keyword_filter_op}'.")

st.markdown("---") # Separador visual

# --- FILTRO POR COLUNA ESPECÍFICA PARA REGRAS DE OPERAÇÃO ---
st.markdown("##### Ou aplicar filtro por coluna específica nas operações:")
coluna_filtro_op = st.selectbox(
    "Selecionar coluna para filtro nas operações",
    ["(nenhuma)"] + df_editado.columns.tolist(),
    key="filter_op_col_select"
)

valores_filtro_op = []
if coluna_filtro_op != "(nenhuma)":
    if pd.api.types.is_numeric_dtype(df_editado[coluna_filtro_op]):
        min_val_op, max_val_op = float(df_editado[coluna_filtro_op].min()), float(df_editado[coluna_filtro_op].max())
        intervalo_op = st.slider(f"Intervalo para '{coluna_filtro_op}'", min_val_op, max_val_op, (min_val_op, max_val_op), key="filter_op_range")
        valores_filtro_op = {'min': intervalo_op[0], 'max': intervalo_op[1]}
    elif pd.api.types.is_datetime64_any_dtype(df_editado[coluna_filtro_op]):
        df_editado[coluna_filtro_op] = pd.to_datetime(df_editado[coluna_filtro_op], errors='coerce')
        min_date_op = df_editado[coluna_filtro_op].min().date() if not df_editado[coluna_filtro_op].min() is pd.NaT else pd.Timestamp.now().date()
        max_date_op = df_editado[coluna_filtro_op].max().date() if not df_editado[coluna_filtro_op].max() is pd.NaT else pd.Timestamp.now().date()
        data_inicio_op, data_fim_op = st.date_input(
            f"Intervalo de datas para '{coluna_filtro_op}'",
            value=(min_date_op, max_date_op),
            min_value=min_date_op,
            max_value=max_date_op,
            key="filter_op_date_range"
        )
        valores_filtro_op = {'start': data_inicio_op, 'end': data_fim_op}
    else:
        opcoes_op = df_editado[coluna_filtro_op].dropna().unique().tolist()
        valores_filtro_op = st.multiselect(f"Valores para '{coluna_filtro_op}'", opcoes_op, key="filter_op_vals")

st.markdown("---") # Separador visual

num_ops = st.number_input("Número de operações", 0, 10, 0)
regras = []

for i in range(int(num_ops)):
    st.markdown(f"---")
    st.write(f"**Operação {i+1}**")
    col = st.selectbox("Coluna Numérica", ["(nenhuma)"] + col_numericas, key=f"colop{i}")
    
    # MODIFICAÇÃO AQUI: Adiciona a opção de aumentar/diminuir porcentagem
    tipo_operacao = st.selectbox("Tipo", ["Soma", "Subtração", "Multiplicação", "Divisão", "Aumentar Porcentagem", "Diminuir Porcentagem"], key=f"tipoop{i}")
    
    val = st.number_input("Valor", format="%.2f", key=f"valop{i}")
    regras.append({"col": col, "tipo": tipo_operacao, "val": val}) # Usa tipo_operacao

if st.button("⚡ Aplicar operações"):
    df_temp = df_editado.copy()
    
    # Inicia com todas as linhas selecionadas
    filtro_global_operacao = pd.Series([True] * len(df_temp), index=df_temp.index) 

    # Aplica o filtro de palavra-chave, se houver
    if keyword_filter_op:
        df_str_temp = df_temp.astype(str)
        mask_keyword_op = df_str_temp.apply(lambda row: row.astype(str).str.contains(keyword_filter_op, case=False, na=False).any(), axis=1)
        filtro_global_operacao = filtro_global_operacao & mask_keyword_op
        
    # Aplica o filtro por coluna específica, se houver
    if coluna_filtro_op != "(nenhuma)":
        if pd.api.types.is_numeric_dtype(df_temp[coluna_filtro_op]) and isinstance(valores_filtro_op, dict):
            mask_col_filter = (df_temp[coluna_filtro_op] >= valores_filtro_op['min']) & \
                              (df_temp[coluna_filtro_op] <= valores_filtro_op['max'])
        elif pd.api.types.is_datetime64_any_dtype(df_temp[coluna_filtro_op]) and isinstance(valores_filtro_op, dict):
            df_temp[coluna_filtro_op] = pd.to_datetime(df_temp[coluna_filtro_op], errors='coerce')
            mask_col_filter = (df_temp[coluna_filtro_op].dt.date >= valores_filtro_op['start']) & \
                              (df_temp[coluna_filtro_op].dt.date <= valores_filtro_op['end'])
        elif valores_filtro_op:
            mask_col_filter = df_temp[coluna_filtro_op].isin(valores_filtro_op)
        else:
            mask_col_filter = pd.Series([False] * len(df_temp), index=df_temp.index)
        
        filtro_global_operacao = filtro_global_operacao & mask_col_filter

    if filtro_global_operacao.empty or not filtro_global_operacao.any():
        st.warning("A combinação de filtros selecionada não retornou nenhuma linha. Nenhuma operação será aplicada.")
        st.stop()

    for r in regras:
        col, tipo, val = r.values()
        try:
            if col != "(nenhuma)":
                df_temp.loc[filtro_global_operacao, col] = pd.to_numeric(df_temp.loc[filtro_global_operacao, col], errors='coerce')
                
                if tipo == "Soma":
                    df_temp.loc[filtro_global_operacao, col] += val
                elif tipo == "Subtração":
                    df_temp.loc[filtro_global_operacao, col] -= val
                elif tipo == "Multiplicação":
                    df_temp.loc[filtro_global_operacao, col] *= val
                elif tipo == "Divisão" and val != 0:
                    df_temp.loc[filtro_global_operacao, col] /= val
                # LÓGICA DE AUMENTAR/DIMINUIR PORCENTAGEM
                elif tipo == "Aumentar Porcentagem":
                    df_temp.loc[filtro_global_operacao, col] *= (1 + val / 100)
                elif tipo == "Diminuir Porcentagem":
                    df_temp.loc[filtro_global_operacao, col] *= (1 - val / 100)

                if filtro_global_operacao.any():
                    celulas_modificadas.loc[df_temp.index[filtro_global_operacao], col] = True
        except Exception as e:
            st.warning(f"Erro ao aplicar regra em {col}: {e}")

    st.session_state.df_editado = df_temp
    st.session_state.celulas_modificadas = celulas_modificadas
    st.success("✅ Regras aplicadas com sucesso!")
    st.rerun()

# --- 8. Regras Visuais (Condicionais) ---
st.subheader("🎯 Regras Visuais")
regras_visual = []
qtd_visuais = st.number_input("Número de regras visuais", 0, 5, 0)

for i in range(int(qtd_visuais)):
    st.markdown(f"---")
    st.write(f"**Regra Visual {i+1}**")
    colv = st.selectbox("Coluna Numérica", col_numericas, key=f"colv{i}")
    op = st.selectbox("Operador", [">", "<", ">=", "<=", "==", "!="], key=f"opv{i}")
    valv = st.number_input("Valor", key=f"valv{i}")
    cor = st.radio("Cor de destaque", ["Verde", "Vermelha"], key=f"corv{i}")
    regras_visual.append({"col": colv, "op": op, "val": valv, "cor": cor})


# --- 9. Filtros para Visualização Final ---
st.subheader("🔍 Filtros de Visualização")

df_para_visualizacao_final = df_editado.copy()

# O filtro de palavra-chave principal permanece aqui
keyword_filter = st.text_input("Filtrar por palavra-chave (em qualquer coluna) para visualização:", key="keyword_main_filter")
if keyword_filter:
    df_str = df_para_visualizacao_final.astype(str)
    mask_keyword = df_str.apply(lambda row: row.astype(str).str.contains(keyword_filter, case=False, na=False).any(), axis=1)
    df_para_visualizacao_final = df_para_visualizacao_final[mask_keyword]
    if df_para_visualizacao_final.empty:
        st.warning(f"Nenhum dado encontrado com a palavra-chave '{keyword_filter}'.")

st.markdown("---") # Separador visual

if col_categoricas:
    col_filtro_cat = st.selectbox("Filtrar por coluna categórica", ["(nenhuma)"] + col_categoricas, key="filter_cat_col")
    if col_filtro_cat != "(nenhuma)":
        opcoes_cat = df_para_visualizacao_final[col_filtro_cat].dropna().unique().tolist()
        valores_selecionados_cat = st.multiselect(f"Valores para '{col_filtro_cat}'", opcoes_cat, default=opcoes_cat, key="filter_cat_vals")
        df_para_visualizacao_final = df_para_visualizacao_final[df_para_visualizacao_final[col_filtro_cat].isin(valores_selecionados_cat)]

if col_numericas:
    col_filtro_num = st.selectbox("Filtrar por coluna numérica", ["(nenhuma)"] + col_numericas, key="filter_num_col")
    if col_filtro_num != "(nenhuma)":
        min_val, max_val = float(df_para_visualizacao_final[col_filtro_num].min()), float(df_para_visualizacao_final[col_filtro_num].max())
        intervalo = st.slider(f"Intervalo para '{col_filtro_num}'", min_val, max_val, (min_val, max_val), key="filter_num_range")
        df_para_visualizacao_final = df_para_visualizacao_final[
            (df_para_visualizacao_final[col_filtro_num] >= intervalo[0]) &
            (df_para_visualizacao_final[col_filtro_num] <= intervalo[1])
        ]

if col_datas:
    col_filtro_data = st.selectbox("Filtrar por coluna de data", ["(nenhuma)"] + col_datas, key="filter_date_col")
    if col_filtro_data != "(nenhuma)":
        df_para_visualizacao_final[col_filtro_data] = pd.to_datetime(df_para_visualizacao_final[col_filtro_data], errors='coerce')
        min_date = df_para_visualizacao_final[col_filtro_data].min().date() if not df_para_visualizacao_final[col_filtro_data].min() is pd.NaT else pd.Timestamp.now().date()
        max_date = df_para_visualizacao_final[col_filtro_data].max().date() if not df_para_visualizacao_final[col_filtro_data].max() is pd.NaT else pd.Timestamp.now().date()

        data_inicio, data_fim = st.date_input(
            f"Intervalo de datas para '{col_filtro_data}'",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            key="filter_date_range"
        )
        if data_inicio and data_fim:
            df_para_visualizacao_final = df_para_visualizacao_final[
                (df_para_visualizacao_final[col_filtro_data].dt.date >= data_inicio) &
                (df_para_visualizacao_final[col_filtro_data].dt.date <= data_fim)
            ]


# --- 10. Lógica de Destaque da Visualização Final ---
df_visivel = df_para_visualizacao_final[colunas_visiveis]

def aplicar_estilos(row):
    estilos = []
    for col_name in df_visivel.columns:
        estilo = ""
        if col_name in celulas_modificadas.columns and row.name in celulas_modificadas.index:
            if celulas_modificadas.at[row.name, col_name]:
                estilo = "background-color: mediumorchid; color: white;"
        
        if not estilo: 
            for r in regras_visual:
                if col_name == r["col"]:
                    try:
                        v = row[col_name]
                        if pd.notna(v) and pd.api.types.is_numeric_dtype(type(v)) and eval(f"v {r['op']} {r['val']}"):
                            estilo = "background-color: lightgreen;" if r["cor"] == "Verde" else "background-color: salmon;"
                            break
                    except:
                        pass

        estilos.append(estilo)
    return estilos

# --- 11. Visualização Final da Tabela ---
st.subheader("📋 Visualização Final")
if regras_visual or celulas_modificadas.any().any():
    df_final_styled = df_visivel.style.format(precision=2).apply(aplicar_estilos, axis=1)
else:
    df_final_styled = df_visivel.style.format(precision=2)
st.dataframe(df_final_styled, use_container_width=True)

# --- 12. Estatísticas Descritivas ---
st.subheader("📊 Estatísticas Descritivas")
if not df_para_visualizacao_final.empty:
    df_desc = df_para_visualizacao_final.select_dtypes(include=np.number)
    if not df_desc.empty:
        st.dataframe(df_desc.describe().transpose().round(2))
    else:
        st.info("Nenhuma coluna numérica para estatísticas descritivas.")
else:
    st.info("DataFrame vazio. Sem estatísticas para exibir.")


# --- 13. Gráficos de Visualização ---
st.subheader("📈 Gráficos")

if not df_para_visualizacao_final.empty:
    grafico_tipo = st.radio(
        "Escolha o tipo de gráfico",
        ["Linha", "Pizza", "Barras Agrupadas", "Dispersão", "Histograma"],
        key="chart_type_selector"
    )

    if grafico_tipo == "Linha":
        if len(col_numericas) >= 2:
            x_line = st.selectbox("Eixo X (Linha)", col_numericas, key="xgraf_line")
            y_line = st.selectbox("Eixo Y (Linha)", col_numericas, key="ygraf_line")
            chart_line = alt.Chart(df_para_visualizacao_final).mark_line(point=True).encode(
                x=x_line, y=y_line, tooltip=list(df_para_visualizacao_final.columns)
            ).properties(width=700, height=400, title=f"Gráfico de Linha: {y_line} vs {x_line}")
            st.altair_chart(chart_line, use_container_width=True)
        else:
            st.info("Necessita de pelo menos duas colunas numéricas para o Gráfico de Linha.")

    elif grafico_tipo == "Dispersão":
        if len(col_numericas) >= 2:
            x_scatter = st.selectbox("Eixo X (Dispersão)", col_numericas, key="xgraf_scatter")
            y_scatter = st.selectbox("Eixo Y (Dispersão)", col_numericas, key="ygraf_scatter")
            color_scatter_options = ["(nenhuma)"] + col_categoricas
            color_scatter = st.selectbox("Colorir por (categórica)", color_scatter_options, key="color_scatter")
            
            tooltip_cols = list(df_para_visualizacao_final.columns)
            
            chart_scatter = alt.Chart(df_para_visualizacao_final).mark_point().encode(
                x=x_scatter,
                y=y_scatter,
                color=alt.Color(color_scatter, title=color_scatter) if color_scatter != "(nenhuma)" else alt.value("steelblue"),
                tooltip=tooltip_cols
            ).properties(width=700, height=400, title=f"Gráfico de Dispersão: {y_scatter} vs {x_scatter}")
            st.altair_chart(chart_scatter, use_container_width=True)
        else:
            st.info("Necessita de pelo menos duas colunas numéricas para o Gráfico de Dispersão.")

    elif grafico_tipo == "Histograma":
        if col_numericas:
            hist_col = st.selectbox("Coluna para Histograma", col_numericas, key="hist_col")
            
            df_hist = df_para_visualizacao_final.dropna(subset=[hist_col]) 
            
            if not df_hist.empty:
                chart_hist = alt.Chart(df_hist).mark_bar().encode(
                    alt.X(hist_col, bin=True, title=hist_col),
                    alt.Y('count()', title="Frequência"),
                    tooltip=[hist_col, 'count()']
                ).properties(width=700, height=400, title=f"Histograma de {hist_col}")
                st.altair_chart(chart_hist, use_container_width=True)
            else:
                st.info(f"Coluna '{hist_col}' não possui dados válidos para o histograma.")
        else:
            st.info("Necessita de colunas numéricas para o Histograma.")

    elif grafico_tipo in ["Pizza", "Barras Agrupadas"]:
        if col_categoricas:
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
                
                selection_visual = alt.selection_point(fields=[col_categoria_grafico], on="click", empty="none")

                if grafico_tipo == "Pizza":
                    if len(col_valores_numericos_multi) <= 1:
                        valor_campo = col_valores_numericos_multi[0] if col_valores_numericos_multi else "Contagem"
                        
                        if not col_valores_numericos_multi:
                            df_agrupado_pizza = df_para_visualizacao_final[col_categoria_grafico].value_counts().reset_index()
                            df_agrupado_pizza.columns = [col_categoria_grafico, "Contagem"]
                        else:
                            df_agrupado_pizza = df_para_visualizacao_final.groupby(col_categoria_grafico)[valor_campo].sum().reset_index()
                        
                        chart_pizza = alt.Chart(df_agrupado_pizza).mark_arc().encode(
                            theta=alt.Theta(field=valor_campo, type="quantitative"),
                            color=alt.Color(field=col_categoria_grafico, type="nominal", title="Categoria",
                                            legend=alt.Legend(title=col_categoria_grafico)),
                            tooltip=[col_categoria_grafico, alt.Tooltip(valor_campo, format=".2f", title="Valor")],
                            opacity=alt.condition(selection_visual, alt.value(1), alt.value(0.2)),
                        ).add_params(
                            selection_visual
                        ).properties(
                            title=f"Distribuição de {valor_campo} por {col_categoria_grafico}"
                        )
                        st.altair_chart(chart_pizza, use_container_width=True)

                    else:
                        st.warning("Para Gráficos de Pizza com múltiplas colunas numéricas, será mostrada a soma total. Considere o Gráfico de Barras Agrupadas para comparação individual.")
                        df_temp_sum = df_para_visualizacao_final.copy()
                        df_temp_sum['Total_Mlti_Colunas'] = df_temp_sum[col_valores_numericos_multi].sum(axis=1)
                        df_agrupado_pizza_multi = df_temp_sum.groupby(col_categoria_grafico)['Total_Mlti_Colunas'].sum().reset_index()
                        
                        selection_visual_multi = alt.selection_point(fields=[col_categoria_grafico], on="click", empty="none")

                        chart_pizza_multi = alt.Chart(df_agrupado_pizza_multi).mark_arc().encode(
                            theta=alt.Theta(field='Total_Mlti_Colunas', type="quantitative"),
                            color=alt.Color(field=col_categoria_grafico, type="nominal", title="Categoria",
                                            legend=alt.Legend(title=col_categoria_grafico)),
                            tooltip=[col_categoria_grafico, alt.Tooltip('Total_Mlti_Colunas', format=".2f", title="Soma Total")],
                            opacity=alt.condition(selection_visual_multi, alt.value(1), alt.value(0.2)),
                        ).add_params(
                            selection_visual_multi
                        ).properties(
                            title=f"Soma Total das Colunas Selecionadas por {col_categoria_grafico}"
                        )
                        st.altair_chart(chart_pizza_multi, use_container_width=True)


                elif grafico_tipo == "Barras Agrupadas":
                    if col_valores_numericos_multi:
                        df_long = df_para_visualizacao_final.melt(
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
                            tooltip=[col_categoria_grafico, "Métrica", alt.Tooltip("Valor", format=".2f")],
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
                st.info("Selecione uma coluna categórica para gerar os gráficos de Pizza ou Barras Agrupadas.")
        else:
            st.info("Nenhuma coluna categórica disponível para os gráficos de Pizza ou Barras Agrupadas.")
else:
    st.info("O DataFrame está vazio ou filtrado. Não há dados para gerar gráficos.")

# --- 14. Exportação do DataFrame ---
st.subheader("⬇️ Exportar Dados")
if not df_editado.empty:
    col1, col2 = st.columns(2)
    with col1:
        buffer_xlsx = BytesIO()
        df_editado.to_excel(buffer_xlsx, index=False, engine="openpyxl")
        buffer_xlsx.seek(0)
        st.download_button(
            "Baixar como Excel (.xlsx)",
            data=buffer_xlsx,
            file_name="SunniExcel_resultado.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    with col2:
        buffer_csv = BytesIO()
        df_editado.to_csv(buffer_csv, index=False)
        buffer_csv.seek(0)
        st.download_button(
            "Baixar como CSV (.csv)",
            data=buffer_csv,
            file_name="SunniExcel_resultado.csv",
            mime="text/csv"
        )
else:
    st.info("DataFrame vazio. Não há dados para exportar.")
