import streamlit as st
import json
import os

set_page_config = st.set_page_config(
    page_title="Gerenciador de Jogadores",
    page_icon=":video_game:",
    layout="centered",
    initial_sidebar_state="auto"
)

# Define o nome do arquivo para persistência de dados.
NOME_ARQUIVO = 'lista_de_jogadores.json'

def carregar_dados():
    """Carrega a lista de jogadores do arquivo JSON."""
    if os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []

def salvar_dados(lista_jogadores):
    """Salva a lista de jogadores no arquivo JSON."""
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_jogadores, arquivo, indent=4, ensure_ascii=False)

def inicializar_estado():
    """Inicializa o estado da sessão do Streamlit."""
    if 'lista_jogadores' not in st.session_state:
        st.session_state.lista_jogadores = carregar_dados()

def adicionar_jogador(nome, lane):
    """Adiciona um novo jogador à lista e salva."""
    if nome and lane:
        novo_jogador = {'nome': nome, 'lane': lane}
        st.session_state.lista_jogadores.append(novo_jogador)
        salvar_dados(st.session_state.lista_jogadores)
        st.success(f"Jogador '{nome}' adicionado com sucesso!")
    else:
        st.warning("Por favor, preencha todos os campos para adicionar um jogador.")

def editar_jogador(indice, novo_nome, nova_lane):
    """Edita um jogador existente na lista e salva."""
    if novo_nome and nova_lane:
        st.session_state.lista_jogadores[indice]['nome'] = novo_nome
        st.session_state.lista_jogadores[indice]['lane'] = nova_lane
        salvar_dados(st.session_state.lista_jogadores)
        st.success("Jogador editado com sucesso!")
    else:
        st.warning("O nome e a lane não podem ser vazios.")
        
# --- Inicialização da Aplicação ---
inicializar_estado()

st.title("Gerenciador de Jogadores")

# --- Seção para Adicionar Jogador ---
st.header("Adicionar Novo Jogador")
with st.form("form_adicionar", clear_on_submit=True):
    novo_nome = st.text_input("Nome do jogador")
    nova_lane = st.text_input("Lane do jogador")
    submit_button = st.form_submit_button("Adicionar")
    if submit_button:
        adicionar_jogador(novo_nome, nova_lane)

# --- Seção para Visualizar Jogadores ---
st.header("Lista de Jogadores")
if st.session_state.lista_jogadores:
    st.dataframe(st.session_state.lista_jogadores, use_container_width=True)
else:
    st.info("A lista de jogadores está vazia.")

# --- Seção para Editar Jogador ---
st.header("Editar Jogador")
if st.session_state.lista_jogadores:
    nomes_jogadores = [f"{i+1}. {p['nome']} ({p['lane']})" for i, p in enumerate(st.session_state.lista_jogadores)]
    jogador_selecionado = st.selectbox("Selecione um jogador para editar", nomes_jogadores)
    
    indice_selecionado = nomes_jogadores.index((str(jogador_selecionado)))
    jogador_atual = st.session_state.lista_jogadores[indice_selecionado]
    
    with st.form("form_editar"):
        novo_nome_edit = st.text_input("Novo nome", value=jogador_atual['nome'])
        nova_lane_edit = st.text_input("Nova lane", value=jogador_atual['lane'])
        submit_edit_button = st.form_submit_button("Salvar Edição")
        if submit_edit_button:
            editar_jogador(indice_selecionado, novo_nome_edit, nova_lane_edit)

# --- Seção para Remover Jogador ---
st.header("Remover Jogador")
if st.session_state.lista_jogadores:
    nomes_jogadores_remocao = [f"{i+1}. {p['nome']} ({p['lane']})" for i, p in enumerate(st.session_state.lista_jogadores)]
    jogador_remover = st.selectbox("Selecione um jogador para remover", nomes_jogadores_remocao, key="remocao_select")
    
    indice_remover = nomes_jogadores_remocao.index(str(jogador_remover))
    
    if st.button("Remover Jogador"):
        remover_jogador(indice_remover)
