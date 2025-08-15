from altair.vegalite.v5.theme import theme
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

def adicionar_jogador(nome, lane, id):
    """Adiciona um novo jogador à lista e salva."""
    if nome and lane and id:
        novo_jogador = {'nome': nome, 'lane': lane, 'id': id}
        st.session_state.lista_jogadores.append(novo_jogador)
        salvar_dados(st.session_state.lista_jogadores)
        st.success(f"Jogador '{nome}' adicionado com sucesso!")
    else:
        st.warning("Por favor, preencha todos os campos para adicionar um jogador.")

# --- Inicialização da Aplicação ---
inicializar_estado()

st.title("Gerenciador de Jogadores")

# --- Seção para Adicionar Jogador ---
st.header("Adicionar Novo Jogador")
with st.form("form_adicionar", clear_on_submit=True):
    novo_nome = st.text_input("Nome do jogador")
    nova_lane = st.text_input("Lane do jogador")
    novo_id = st.text_input("ID do jogador")
    submit_button = st.form_submit_button("Adicionar")
    if submit_button:
        adicionar_jogador(novo_nome, nova_lane, novo_id)

# --- Seção para Visualizar Jogadores ---
st.header("Lista de Jogadores")
if st.session_state.lista_jogadores:
    st.dataframe(st.session_state.lista_jogadores, use_container_width=True)
else:
    st.info("A lista de jogadores está vazia.")


 
