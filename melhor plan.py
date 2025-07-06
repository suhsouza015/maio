import streamlit as st
import pandas as pd
import altair as alt
from io import BytesIO
import numpy as np
from datetime import date

st.set_page_config(page_title="SunniExcel", layout="wide")
st.title("🌞 SunniExcel — Sua Planilha Inteligente e Visual")

# --- Funções de Histórico (Mover para o topo para melhor organização) ---
if "historico_df" not in st.session_state:
    st.session_state.historico_df = []
if "historico_celulas_modificadas" not in st.session_state:
    st.session_state.historico_celulas_modificadas = []
if "historico_financas" not in st.session_state:
    st.session_state.historico_financas = []

def salvar_estado():
    """Salva o estado atual do DataFrame e das células modificadas no histórico."""
    st.session_state.historico_df.append(st.session_state.df_editado.copy())
    st.session_state.historico_celulas_modificadas.append(st.session_state.celulas_modificadas.copy())
    
    # Adicionar o estado atual do df_financas ao histórico de finanças
    if 'df_financas' in st.session_state and not st.session_state.df_financas.empty:
        st.session_state.historico_financas.append(st.session_state.df_financas.copy())
    elif 'df_financas' in st.session_state and st.session_state.df_financas.empty and len(st.session_state.historico_financas) > 0:
        # Se df_financas estiver vazio, mas o histórico não, adicione uma cópia do último estado vazio ou um df vazio
        st.session_state.historico_financas.append(pd.DataFrame(columns=["Data", "Tipo", "Categoria", "Valor"]))
    elif 'df_financas' not in st.session_state and not st.session_state.historico_financas:
        st.session_state.historico_financas.append(pd.DataFrame(columns=["Data", "Tipo", "Categoria", "Valor"]))


    # Limitar o histórico para evitar consumo excessivo de memória
    if len(st.session_state.historico_df) > 10:
        st.session_state.historico_df.pop(0)
        st.session_state.historico_celulas_modificadas.pop(0)
    if len(st.session_state.historico_financas) > 10: # Limitar histórico financeiro também
        st.session_state.historico_financas.pop(0)

def restaurar_ultimo_estado():
    """Restaura o DataFrame e as células modificadas para o estado anterior."""
    if len(st.session_state.historico_df) > 1:
        st.session_state.historico_df.pop()
        st.session_state.celulas_modificadas.pop()

        st.session_state.df_editado = st.session_state.historico_df[-1].copy()
        st.session_state.celulas_modificadas = st.session_state.historico_celulas_modificadas[-1].copy()
        st.sidebar.success("Última alteração do Editor de Dados desfeita!")
        st.rerun()
    elif len(st.session_state.historico_df) == 1:
        st.sidebar.info("Não há mais alterações para desfazer no Editor de Dados.")
    else:
        st.sidebar.info("Nenhuma alteração para desfazer no Editor de Dados.")

def restaurar_ultimo_estado_financas():
    """Restaura o DataFrame de finanças para o estado anterior."""
    if len(st.session_state.historico_financas) > 1:
        st.session_state.historico_financas.pop()
        st.session_state.df_financas = st.session_state.historico_financas[-1].copy()
        st.success("Última alteração financeira desfeita!")
        st.rerun()
    elif len(st.session_state.historico_financas) == 1:
        st.info("Não há mais alterações para desfazer na Gestão Financeira.")
    else:
        st.info("Nenhuma alteração para desfazer na Gestão Financeira.")

# --- 1. Inicialização do Estado da Sessão ---
if "df_editado" not in st.session_state:
    st.session_state.df_editado = pd.DataFrame([["" for _ in range(3)] for _ in range(5)], columns=["Coluna 1", "Coluna 2", "Coluna 3"])
    st.session_state.celulas_modificadas = pd.DataFrame(False, index=st.session_state.df_editado.index, columns=st.session_state.df_editado.columns)
if "selecao_grafico" not in st.session_state:
    st.session_state.selecao_grafico = {}
if "nome_arquivo_upload" not in st.session_state:
    st.session_state.nome_arquivo_upload = None

# Inicialização do DataFrame de Gestão Financeira
if "df_financas" not in st.session_state:
    st.session_state.df_financas = pd.DataFrame(columns=["Data", "Tipo", "Categoria", "Valor"])
    st.session_state.historico_financas.append(st.session_state.df_financas.copy())

# Variável de estado para controlar a página exibida
if "current_page" not in st.session_state:
    st.session_state.current_page = "editor_dados"


# --- 2. Upload ou Criação de Planilha (Editor de Dados) ---
st.sidebar.header("📥 Upload ou Criação")
arquivo = st.sidebar.file_uploader("Envie um .xlsx ou .csv para o Editor de Dados", type=["xlsx", "csv"], key="editor_file_uploader")

if arquivo is not None:
    if st.session_state.nome_arquivo_upload != arquivo.name:
        try:
            salvar_estado()
            if arquivo.name.endswith('.xlsx'):
                df_carregado = pd.read_excel(arquivo)
            elif arquivo.name.endswith('.csv'):
                df_carregado = pd.read_csv(arquivo)
            
            st.session_state.df_editado = df_carregado.copy()
            st.session_state.celulas_modificadas = pd.DataFrame(False, index=df_carregado.index, columns=df_carregado.columns)
            st.session_state.selecao_grafico = {}
            st.session_state.nome_arquivo_upload = arquivo.name
            st.success(f"Arquivo '{arquivo.name}' carregado com sucesso para o Editor de Dados!")
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}. Certifique-se de que é um arquivo Excel/CSV válido.")
            if st.session_state.historico_df:
                st.session_state.df_editado = st.session_state.historico_df[-1]
                st.session_state.celulas_modificadas = st.session_state.historico_celulas_modificadas[-1]
            else:
                st.session_state.df_editado = pd.DataFrame([["" for _ in range(3)] for _ in range(5)], columns=["Coluna 1", "Coluna 2", "Coluna 3"])
                st.session_state.celulas_modificadas = pd.DataFrame(False, index=st.session_state.df_editado.index, columns=st.session_state.df_editado.columns)
            st.session_state.selecao_grafico = {}
            st.session_state.nome_arquivo_upload = None
            st.rerun()

if "df_editado" not in st.session_state or st.sidebar.button("Criar nova planilha", key="create_new_df_btn"):
    salvar_estado()
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

# --- Sidebar de Navegação Principal ---
st.sidebar.markdown("---")
st.sidebar.header("Navegação")
if st.sidebar.button("⚙️ Editor de Dados", key="nav_editor"):
    st.session_state.current_page = "editor_dados"
if st.sidebar.button("💰 Gestão Financeira", key="nav_financas"):
    st.session_state.current_page = "gestao_financas"

# --- Conteúdo da Página Principal baseado na seleção da sidebar ---

if st.session_state.current_page == "editor_dados":
    # --- 3. Limpeza de Dados Básica ---
    st.sidebar.header("🧹 Limpeza de Dados")
    if st.sidebar.button("Remover Linhas Duplicadas"):
        salvar_estado()
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
                salvar_estado()
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
                    salvar_estado()
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
                        salvar_estado()
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
                    salvar_estado()
                    df_editado.rename(columns={coluna_antiga: nova_nome_coluna}, inplace=True)
                    if coluna_antiga in celulas_modificadas.columns:
                        celulas_modificadas.rename(columns={coluna_antiga: nova_nome_coluna}, inplace=True)
                    st.session_state.df_editado = df_editado
                    st.session_state.celulas_modificadas = celulas_modificadas
                    st.sidebar.success(f"Coluna '{coluna_antiga}' renomeada para '{nova_nome_coluna}'.")
                    st.rerun()
            else:
                st.sidebar.info("O novo nome não pode ser vazio ou igual ao nome atual.")

    # --- 5. Remover Colunas ---
    st.sidebar.header("🗑️ Remover Colunas")
    colunas_para_remover = st.sidebar.multiselect(
        "Selecionar colunas para remover",
        df_editado.columns.tolist(),
        key="cols_to_drop"
    )
    if st.sidebar.button("Remover Colunas Selecionadas"):
        if colunas_para_remover:
            salvar_estado()
            colunas_removidas_str = ", ".join(colunas_para_remover)
            df_editado.drop(columns=colunas_para_remover, inplace=True)
            
            for col_to_remove in colunas_para_remover:
                if col_to_remove in celulas_modificadas.columns:
                    celulas_modificadas = celulas_modificadas.drop(columns=[col_to_remove])
            
            st.session_state.df_editado = df_editado
            st.session_state.celulas_modificadas = celulas_modificadas
            st.sidebar.success(f"Colunas '{colunas_removidas_str}' removidas com sucesso!")
            st.rerun()
        else:
            st.sidebar.info("Nenhuma coluna selecionada para remover.")

    # Botão para desfazer última remoção (ou qualquer ação)
    st.sidebar.markdown("---")
    st.sidebar.subheader("↩️ Desfazer Ação (Editor de Dados)")
    if st.sidebar.button("Desfazer Última Alteração no Editor"):
        restaurar_ultimo_estado()


    # --- 6. Editor de Dados Principal ---
    st.subheader("📝 Editar Dados")
    df_antes_edicao = st.session_state.df_editado.copy() 
    df_editado_novo = st.data_editor(df_editado, num_rows="dynamic", use_container_width=True, key="main_data_editor")

    if not df_antes_edicao.equals(df_editado_novo):
        salvar_estado()
        st.session_state.df_editado = df_editado_novo
        st.rerun()

    df_editado = st.session_state.df_editado
    celulas_modificadas = st.session_state.celulas_modificadas


    # --- 7. Seleção de Colunas Visíveis ---
    st.subheader("👁️ Colunas Visíveis")
    colunas_visiveis = st.multiselect("Selecionar colunas para exibição", df_editado.columns.tolist(), default=df_editado.columns.tolist())

    # --- 8. Regras de Operação com Filtro Específico ---
    st.subheader("🧮 Regras de Operação com Filtro Específico")
    col_numericas = df_editado.select_dtypes(include="number").columns.tolist()
    col_categoricas = df_editado.select_dtypes(include=["object", "category"]).columns.tolist()
    col_datas = df_editado.select_dtypes(include=["datetime64[ns]"]).columns.tolist()

    st.markdown("##### Aplicar filtro de palavra-chave nas operações:")
    keyword_filter_op = st.text_input("Filtrar por palavra-chave (em qualquer coluna) antes de aplicar operações:", key="keyword_op_filter")
    if keyword_filter_op:
        st.info(f"Operações serão aplicadas apenas às linhas que contêm '{keyword_filter_op}'.")

    st.markdown("---")

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

    st.markdown("---")

    num_ops = st.number_input("Número de operações", 0, 10, 0)
    regras = []

    for i in range(int(num_ops)):
        st.markdown(f"---")
        st.write(f"**Operação {i+1}**")
        col = st.selectbox("Coluna Numérica", ["(nenhuma)"] + col_numericas, key=f"colop{i}")
        
        tipo_operacao = st.selectbox("Tipo", ["Soma", "Subtração", "Multiplicação", "Divisão", "Aumentar Porcentagem", "Diminuir Porcentagem"], key=f"tipoop{i}")
        
        val = st.number_input("Valor", format="%.2f", key=f"valop{i}")
        regras.append({"col": col, "tipo": tipo_operacao, "val": val})

    if st.button("⚡ Aplicar operações"):
        salvar_estado()
        df_temp = df_editado.copy()
        
        filtro_global_operacao = pd.Series([True] * len(df_temp), index=df_temp.index) 

        if keyword_filter_op:
            df_str_temp = df_temp.astype(str)
            mask_keyword_op = df_str_temp.apply(lambda row: row.astype(str).str.contains(keyword_filter_op, case=False, na=False).any(), axis=1)
            filtro_global_operacao = filtro_global_operacao & mask_keyword_op
            
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

    # --- 9. Regras Visuais (Condicionais) ---
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


    # --- 10. Filtros para Visualização Final ---
    st.subheader("🔍 Filtros de Visualização")

    df_para_visualizacao_final = df_editado.copy()

    keyword_filter = st.text_input("Filtrar por palavra-chave (em qualquer coluna) para visualização:", key="keyword_main_filter")
    if keyword_filter:
        df_str = df_para_visualizacao_final.astype(str)
        mask_keyword = df_str.apply(lambda row: row.astype(str).str.contains(keyword_filter, case=False, na=False).any(), axis=1)
        df_para_visualizacao_final = df_para_visualizacao_final[mask_keyword]
        if df_para_visualizacao_final.empty:
            st.warning(f"Nenhum dado encontrado com a palavra-chave '{keyword_filter}'.")

    st.markdown("---")

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


    # --- 11. Lógica de Destaque da Visualização Final ---
    colunas_visiveis_existentes = [col for col in colunas_visiveis if col in df_para_visualizacao_final.columns]
    df_visivel = df_para_visualizacao_final[colunas_visiveis_existentes]


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

    # --- 12. Visualização Final da Tabela ---
    st.subheader("📋 Visualização Final")
    if regras_visual or celulas_modificadas.any().any():
        if not df_visivel.empty and not df_visivel.columns.empty:
            df_final_styled = df_visivel.style.format(precision=2).apply(aplicar_estilos, axis=1)
        else:
            df_final_styled = df_visivel.style.format(precision=2)
    else:
        df_final_styled = df_visivel.style.format(precision=2)
    st.dataframe(df_final_styled, use_container_width=True)

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
                                x=alt.X("Categoria:N", axis=alt.Axis(title="Categoria")),
                                y=alt.Y("Valor:Q", axis=alt.Axis(title="Valor")),
                                color=alt.Color("Métrica:N", title="Métrica"),
                                column=alt.Column("Tipo:N", header=alt.Header(titleOrient="bottom", labelOrient="bottom")),
                                tooltip=[col_categoria_grafico, "Métrica", alt.Tooltip("Valor", format=".2f")],
                                opacity=alt.condition(selection_visual_bar, alt.value(1), alt.value(0.2))
                            ).add_params(
                                selection_visual_bar
                            ).properties(
                                title=f"Gráfico de Barras Agrupadas por {col_categoria_grafico} e Métrica"
                            )
                            st.altair_chart(chart_barras, use_container_width=True)
                        else:
                            st.info("Selecione pelo menos uma coluna numérica para o Gráfico de Barras Agrupadas.")
                else:
                    st.info("Selecione uma coluna categórica para o Gráfico de Pizza ou Barras Agrupadas.")
            else:
                st.info("Nenhuma coluna categórica disponível para o Gráfico de Pizza ou Barras Agrupadas.")

    else:
        st.info("DataFrame vazio. Sem gráficos para exibir.")

elif st.session_state.current_page == "gestao_financas":
    st.subheader("💰 Adicionar Nova Transação")
    # --- Formulário de Adição de Transação ---
    with st.form("form_financas"):
        tipo_transacao = st.radio("Tipo", ["Gasto", "Ganho"], key="tipo_transacao")
        valor_transacao = st.number_input("Valor", min_value=0.01, format="%.2f", key="valor_transacao")
        categoria_transacao = st.text_input("Categoria (ex: Alimentação, Salário, Lazer)", key="categoria_transacao")
        data_transacao = st.date_input("Data da Movimentação", value=date.today(), key="data_transacao")

        submit_button = st.form_submit_button("Adicionar Transação")

        if submit_button:
            if valor_transacao and categoria_transacao:
                salvar_estado() # Salva o estado ANTES de adicionar a nova transação
                nova_transacao = pd.DataFrame([{
                    "Data": data_transacao,
                    "Tipo": tipo_transacao,
                    "Categoria": categoria_transacao,
                    "Valor": valor_transacao
                }])
                st.session_state.df_financas = pd.concat([st.session_state.df_financas, nova_transacao], ignore_index=True)
                st.success("Transação adicionada com sucesso!")
                st.rerun()
            else:
                st.warning("Por favor, preencha o valor e a categoria da transação.")
    # --- Fim do Formulário ---

    st.markdown("---")

    # --- Uploader de Planilha Excel para Gestão Financeira ---
    st.subheader("⬆️ Importar Transações de Planilha Excel (.xlsx)")
    uploaded_finances_file = st.file_uploader(
        "Envie um arquivo Excel com suas transações financeiras.",
        type=["xlsx"],
        key="finances_excel_uploader"
    )

    if uploaded_finances_file is not None:
        try:
            df_importado_financas = pd.read_excel(uploaded_finances_file)
            
            # Padronizar nomes das colunas para facilitar o merge
            df_importado_financas.columns = df_importado_financas.columns.str.strip().str.capitalize()
            
            # Mapeamento para garantir as colunas esperadas
            required_cols = ["Data", "Tipo", "Categoria", "Valor"]
            
            # Verificar se as colunas essenciais existem ou podem ser inferidas
            if not all(col in df_importado_financas.columns for col in required_cols):
                st.warning("As colunas esperadas ('Data', 'Tipo', 'Categoria', 'Valor') não foram encontradas. Por favor, revise sua planilha ou mapeie as colunas abaixo.")
                
                col_mapping = {}
                for r_col in required_cols:
                    col_mapping[r_col] = st.selectbox(f"Mapear '{r_col}' para qual coluna do seu arquivo?", ["(Não mapeado)"] + df_importado_financas.columns.tolist(), key=f"map_col_{r_col}")

                if st.button("Aplicar Mapeamento e Importar"):
                    # Aplicar o mapeamento e renomear as colunas
                    df_to_merge = df_importado_financas.rename(columns={v: k for k, v in col_mapping.items() if v != "(Não mapeado)"})
                    
                    # Filtrar apenas as colunas mapeadas e verificar se as essenciais estão presentes
                    final_cols = [col for col in required_cols if col in df_to_merge.columns]
                    if len(final_cols) == 4:
                        df_to_merge = df_to_merge[final_cols].copy()
                        # Realizar conversões de tipo
                        df_to_merge["Data"] = pd.to_datetime(df_to_merge["Data"], errors='coerce').dt.date
                        df_to_merge["Tipo"] = df_to_merge["Tipo"].astype(str)
                        df_to_merge["Categoria"] = df_to_merge["Categoria"].astype(str)
                        df_to_merge["Valor"] = pd.to_numeric(df_to_merge["Valor"], errors='coerce')
                        df_to_merge.dropna(subset=["Data", "Tipo", "Categoria", "Valor"], inplace=True) # Remove linhas com dados faltantes após conversão

                        if not df_to_merge.empty:
                            salvar_estado() # Salva o estado ANTES da importação
                            st.session_state.df_financas = pd.concat([st.session_state.df_financas, df_to_merge], ignore_index=True)
                            st.success(f"Dados do arquivo '{uploaded_finances_file.name}' importados e combinados com sucesso!")
                            st.rerun()
                        else:
                            st.warning("Nenhum dado válido encontrado para importação após o mapeamento.")
                    else:
                        st.error("Por favor, mapeie todas as colunas essenciais: Data, Tipo, Categoria, Valor.")

            else: # Se as colunas já estão corretas
                df_to_merge = df_importado_financas[required_cols].copy()
                # Realizar conversões de tipo
                df_to_merge["Data"] = pd.to_datetime(df_to_merge["Data"], errors='coerce').dt.date
                df_to_merge["Tipo"] = df_to_merge["Tipo"].astype(str)
                df_to_merge["Categoria"] = df_to_merge["Categoria"].astype(str)
                df_to_merge["Valor"] = pd.to_numeric(df_to_merge["Valor"], errors='coerce')
                df_to_merge.dropna(subset=["Data", "Tipo", "Categoria", "Valor"], inplace=True)

                if not df_to_merge.empty:
                    salvar_estado() # Salva o estado ANTES da importação
                    st.session_state.df_financas = pd.concat([st.session_state.df_financas, df_to_merge], ignore_index=True)
                    st.success(f"Dados do arquivo '{uploaded_finances_file.name}' importados e combinados com sucesso!")
                    st.rerun()
                else:
                    st.warning("Nenhum dado válido encontrado para importação no arquivo.")

        except Exception as e:
            st.error(f"Erro ao processar o arquivo Excel: {e}. Verifique o formato e o conteúdo do arquivo. Certifique-se de que as colunas 'Data', 'Tipo', 'Categoria' e 'Valor' estão presentes e com dados válidos.")

    st.markdown("---")

    # --- Novos Botões de Controle ---
    st.subheader("Controle de Dados Financeiros")
    col1_btns, col2_btns, col3_btns = st.columns(3)

    with col1_btns:
        if st.button("🗑️ Limpar Todas as Transações", key="clear_all_finances"):
            if st.session_state.df_financas.empty:
                st.info("Não há transações para limpar.")
            else:
                salvar_estado() # Salva o estado ANTES de limpar
                st.session_state.df_financas = pd.DataFrame(columns=["Data", "Tipo", "Categoria", "Valor"])
                st.success("Todas as transações financeiras foram limpas!")
                st.rerun()
    with col2_btns:
        if st.button("↩️ Desfazer Última Ação Financeira", key="undo_finances"):
            restaurar_ultimo_estado_financas()
    with col3_btns:
        # Função para salvar o DataFrame de finanças em Excel
        def to_excel(df):
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df.to_excel(writer, index=False, sheet_name='TransacoesFinanceiras')
            writer.close()
            processed_data = output.getvalue()
            return processed_data

        excel_data = to_excel(st.session_state.df_financas)
        st.download_button(
            label="💾 Salvar Transações Atuais (.xlsx)",
            data=excel_data,
            file_name="transacoes_financeiras.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="save_finances_excel"
        )
    
    st.markdown("---")


    st.subheader("📊 Resumo Financeiro Detalhado")
    if not st.session_state.df_financas.empty:
        # data_editor para permitir edição direta da tabela de finanças
        df_financas_editado = st.data_editor(
            st.session_state.df_financas.sort_values(by="Data", ascending=False),
            num_rows="dynamic",
            use_container_width=True,
            key="finances_data_editor"
        )
        # Se houver mudanças na tabela editada, atualiza o estado
        if not df_financas_editado.equals(st.session_state.df_financas):
            salvar_estado() # Salva o estado ANTES de aplicar a edição
            st.session_state.df_financas = df_financas_editado
            st.success("Tabela de transações atualizada!")
            st.rerun()

        total_ganhos = st.session_state.df_financas[st.session_state.df_financas["Tipo"] == "Ganho"]["Valor"].sum()
        total_gastos = st.session_state.df_financas[st.session_state.df_financas["Tipo"] == "Gasto"]["Valor"].sum()
        saldo = total_ganhos - total_gastos

        st.markdown(f"**Total de Ganhos:** R$ {total_ganhos:,.2f}")
        st.markdown(f"**Total de Gastos:** R$ {total_gastos:,.2f}")
        st.markdown(f"**Saldo Atual:** R$ {saldo:,.2f}")

        # Gráfico de Ganhos vs Gastos por Categoria
        st.subheader("Ganhos e Gastos por Categoria")
        df_grouped_financas = st.session_state.df_financas.groupby(["Categoria", "Tipo"])["Valor"].sum().reset_index()

        chart_financas = alt.Chart(df_grouped_financas).mark_bar().encode(
            x=alt.X("Categoria:N", axis=alt.Axis(title="Categoria")),
            y=alt.Y("Valor:Q", axis=alt.Axis(title="Valor (R$)")),
            color=alt.Color("Tipo:N", legend=alt.Legend(title="Tipo de Transação")),
            tooltip=["Categoria", "Tipo", alt.Tooltip("Valor", format=".2f")]
        ).properties(
            title="Ganhos e Gastos por Categoria"
        ).interactive()
        st.altair_chart(chart_financas, use_container_width=True)

        # Gráfico de Linha para Saldo ao longo do tempo (se tiver coluna de data)
        st.subheader("Saldo ao longo do Tempo")
        if "Data" in st.session_state.df_financas.columns and not st.session_state.df_financas.empty:
            df_saldo_tempo = st.session_state.df_financas.copy()
            df_saldo_tempo['Impacto_Saldo'] = df_saldo_tempo.apply(
                lambda row: row['Valor'] if row['Tipo'] == 'Ganho' else -row['Valor'], axis=1
            )
            df_saldo_tempo = df_saldo_tempo.sort_values(by="Data")
            df_saldo_tempo['Saldo_Acumulado'] = df_saldo_tempo['Impacto_Saldo'].cumsum()

            chart_saldo_tempo = alt.Chart(df_saldo_tempo).mark_line(point=True).encode(
                x=alt.X("Data:T", axis=alt.Axis(title="Data")),
                y=alt.Y("Saldo_Acumulado:Q", axis=alt.Axis(title="Saldo Acumulado (R$)")),
                tooltip=["Data", alt.Tooltip("Saldo_Acumulado", format=".2f")]
            ).properties(
                title="Evolução do Saldo ao Longo do Tempo"
            ).interactive()
            st.altair_chart(chart_saldo_tempo, use_container_width=True)
        else:
            st.info("Adicione transações com datas para ver a evolução do saldo.")

    else:
        st.info("Nenhuma transação financeira adicionada ainda. Use o formulário ou importe uma planilha para adicionar transações.")
