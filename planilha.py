import streamlit as st
import pandas as pd
import sqlite3
import calendar
import plotly.express as pl
from datetime import datetime
import uuid

# ——————————————————————————————————————
# GERAÇÃO E ARMAZENAMENTO DE USER_ID
# ——————————————————————————————————————
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# Pegar data atual
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Planejador Financeiro", layout="wide")
st.sidebar.markdown(f"**Seu User ID:**  {st.session_state.user_id}")
st.title("📘 Planejador Financeiro")

DB_NAME = "planf.db"

# ——————————————————————————————————————
# FUNÇÃO: CRIAR TABELA COM user_id
# ——————————————————————————————————————
def criar_banco():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS financeiro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                ano INTEGER,
                mes INTEGER,
                dia INTEGER,
                faturamento REAL,
                categoria_fat TEXT,
                gastos REAL,
                categoria_gastos TEXT,
                lucro REAL
            )
        ''')
        conn.commit()

# ——————————————————————————————————————
# FUNÇÃO: SALVAR DADOS COM user_id
# ——————————————————————————————————————
def salvar_dados(user_id, ano, mes, dados):
    with sqlite3.connect(DB_NAME) as conn:
        for d in dados:
            f = d["faturamento"]
            g = d["gastos"]
            lucro = f - g
            conn.execute('''
                INSERT INTO financeiro (
                    user_id, ano, mes, dia,
                    faturamento, categoria_fat,
                    gastos, categoria_gastos, lucro
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id, ano, mes, d["dia"],
                f, d["categoria_fat"],
                g, d["categoria_gastos"], lucro
            ))
        conn.commit()

criar_banco()

# ——————————————————————————————————————
# SELETORES DE ANO E MÊS (padrão data atual)
# ——————————————————————————————————————
col1, col2 = st.columns(2)
ano = col1.number_input(
    "Ano",
    min_value=2000,
    max_value=2100,
    value=current_year,
    step=1,
    format="%d"
)
mes = col2.selectbox(
    "Mês",
    list(range(1, 13)),
    index=current_month - 1,
    format_func=lambda m: calendar.month_name[m]
)

num_dias = calendar.monthrange(ano, mes)[1]
st.subheader(f"📅 Entradas para {calendar.month_name[mes]} de {ano} ({num_dias} dias)")

# ——————————————————————————————————————
# FORMULÁRIO DIÁRIO (EXPANDERS)
# ——————————————————————————————————————
dados = []
for dia in range(1, num_dias + 1):
    with st.expander(f"Dia {dia:02d}"):
        c1, c2, c3 = st.columns(3)
        faturamento = c1.number_input(
            "Faturamento",
            min_value=0,
            step=1,
            key=f"f_{dia}",
            format="%d"
        )
        cat_fat = c1.text_input("Categoria Fat.", key=f"cf_{dia}")
        gastos = c2.number_input(
            "Gastos",
            min_value=0,
            step=1,
            key=f"g_{dia}",
            format="%d"
        )
        cat_gastos = c2.text_input("Categoria Gastos", key=f"cg_{dia}")
        lucro = faturamento - gastos
        c3.metric("💰 Lucro", f"R$ {lucro:,}", delta_color="inverse")

        dados.append({
            "dia": dia,
            "faturamento": faturamento,
            "categoria_fat": cat_fat or "Não informado",
            "gastos": gastos,
            "categoria_gastos": cat_gastos or "Não informado"
        })

# ——————————————————————————————————————
# BOTÃO PARA SALVAR NO BANCO
# ——————————————————————————————————————
if st.button("💾 Salvar Mês"):
    salvar_dados(st.session_state.user_id, ano, mes, dados)
    st.success("✅ Dados salvos com sucesso!")

st.markdown("---")

# ——————————————————————————————————————
# HISTÓRICO COM FILTROS E GRÁFICOS DINÂMICOS
# ——————————————————————————————————————
if st.checkbox("📊 Ver histórico com filtros"):
    query = '''
        SELECT * FROM financeiro
        WHERE user_id = ? AND ano = ? AND mes = ?
        ORDER BY dia
    '''
    with sqlite3.connect(DB_NAME) as conn:
        df = pd.read_sql_query(
            query,
            conn,
            params=(st.session_state.user_id, ano, mes)
        )

    if df.empty:
        st.info("📌 Nenhum dado disponível para esse mês.")
    else:
        # —————— Filtros ——————
        st.markdown("### 🔍 Filtros")
        f1, f2, f3 = st.columns(3)

        dias = sorted(df["dia"].unique())
        # define default até dia atual se estiver no mês/ano corrente
        if ano == current_year and mes == current_month:
            default_range = (dias[0], min(current_day, dias[-1]))
        else:
            default_range = (dias[0], dias[-1])

        dia_inicio, dia_fim = f1.select_slider(
            "Intervalo de dias",
            options=dias,
            value=default_range
        )

        categorias = sorted(df["categoria_gastos"].unique())
        sel_cat = f2.multiselect(
            "Categoria de Gasto", categorias, default=categorias
        )

        op_lucro = f3.radio(
            "Tipo de Lucro",
            ["Todos", "Apenas Positivo", "Apenas Negativo"]
        )

        # aplica filtros
        df_f = df[
            (df["dia"] >= dia_inicio) &
            (df["dia"] <= dia_fim) &
            (df["categoria_gastos"].isin(sel_cat))
        ]
        if op_lucro == "Apenas Positivo":
            df_f = df_f[df_f["lucro"] >= 0]
        elif op_lucro == "Apenas Negativo":
            df_f = df_f[df_f["lucro"] < 0]

        # tabela enxuta
        df_vis = df_f[["dia", "faturamento", "gastos", "categoria_gastos", "lucro"]]
        st.dataframe(df_vis, use_container_width=True)
        st.markdown(f"💡 {len(df_vis)} registro(s) encontrado(s).")

        # — Gráficos na sidebar —
        st.sidebar.markdown("## 📈 Visualização de Dados")
        tipo_graf = st.sidebar.radio("Tipo de Gráfico:", ["Barras", "Pizza"])

        st.subheader("📊 Gráfico Dinâmico")
        if tipo_graf == "Barras":
            grp = df_f.groupby("categoria_gastos")["lucro"].sum().reset_index()
            fig = pl.bar(
                grp, x="categoria_gastos", y="lucro", color="categoria_gastos",
                title="Lucro por Categoria de Gasto",
                labels={"categoria_gastos": "Categoria", "lucro": "Lucro (R$)"}
            )
        else:
            grp = df_f.groupby("categoria_gastos")["gastos"].sum().reset_index()
            fig = pl.pie(
                grp, names="categoria_gastos", values="gastos",
                title="Distribuição de Gastos por Categoria"
            )
        st.plotly_chart(fig, use_container_width=True)
