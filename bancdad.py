# Conteúdo do arquivo: funcoes.py
# Este arquivo deve ser salvo como 'funcoes.py'

import sqlite3

def connectaDB():
    """
    Estabelece e retorna uma conexão com o banco de dados 'clientes.db'.
    """
    conexao = sqlite3.connect('clientes.db')
    return conexao

def inserirDados(nome, email, telefone):
    """
    Insere novos dados de cliente no banco de dados.

    Args:
        nome (str): O nome do cliente.
        email (str): O email do cliente (deve ser único).
        telefone (str): O telefone do cliente.

    Returns:
        tuple: Uma tupla contendo (bool, str).
               - True e uma mensagem de sucesso se a inserção for bem-sucedida.
               - False e uma mensagem de erro se a inserção falhar (ex: campos vazios, email duplicado, erro inesperado).
    """
    if not nome or not email or not telefone:
        return False, "Todos os campos (Nome, Email, Telefone) são obrigatórios."

    conexao = connectaDB()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone)
        )
        conexao.commit()
        return True, "Cliente cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        # Erro específico para violação de UNIQUE constraint (email duplicado)
        return False, f"O e-mail '{email}' já existe. Por favor, use um e-mail único."
    except Exception as e:
        # Captura outros erros inesperados durante a inserção
        return False, f"Ocorreu um erro inesperado ao cadastrar: {e}"
    finally:
        # Garante que a conexão seja sempre fechada
        conexao.close()

def listarDados():
    """
    Busca e retorna todos os dados de clientes do banco de dados.

    Returns:
        list: Uma lista de tuplas, onde cada tupla representa uma linha (cliente).
              Retorna uma lista vazia se não houver clientes.
    """
    conexao = connectaDB()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        dados = cursor.fetchall()
        return dados
    except Exception as e:
        print(f"Erro ao listar dados: {e}") # Para depuração no console
        return []
    finally:
        conexao.close()


# --- Fim do conteúdo de funcoes.py ---


# --- Início do conteúdo do arquivo principal do Streamlit (Ex: app.py) ---
# Este arquivo deve ser salvo como 'app.py' no mesmo diretório de 'funcoes.py'

import streamlit as st
import pandas as pd
import sqlite3 # Importado para a função de inicialização do DB
import funcoes # Importa todas as funções do nosso arquivo funcoes.py

# --- Função de Inicialização do Banco de Dados ---
# Esta função garante que a tabela 'clientes' exista no banco de dados.
# Ela é chamada uma única vez quando o aplicativo Streamlit é iniciado.
def inicializar_banco_dados():
    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()
    try:
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefone TEXT NOT NULL
            )'''
        )
        # print("Tabela 'clientes' criada ou já existe.") # Descomente para depuração no terminal
    except Exception as e:
        st.error(f"Erro crítico ao inicializar o banco de dados: {e}")
    finally:
        conexao.close()

# Chama a função de inicialização do banco de dados ao iniciar o aplicativo
inicializar_banco_dados()

# --- Interface do Usuário Streamlit ---
st.set_page_config(page_title="Cadastro de Clientes", layout="centered") # Configurações básicas da página
st.title('Sistema de Cadastro de Clientes')

st.markdown("""
Este aplicativo permite **cadastrar e visualizar** informações de clientes de forma simples e eficiente.
""")

# --- Seção para Cadastrar Novo Cliente ---
st.subheader('Cadastrar Novo Cliente')
# Usamos st.form para criar um formulário. Quando o botão 'Cadastrar Cliente' é clicado,
# todo o conteúdo dentro do 'with st.form' é reprocessado.
with st.form(key="cadastro_form", clear_on_submit=True):
    nome = st.text_input('Nome do Cliente', key="nome_input")
    email = st.text_input('Email do Cliente', key="email_input")
    telefone = st.text_input('Telefone do Cliente', key="telefone_input")

    # Botão de submissão do formulário
    submitted = st.form_submit_button('Cadastrar Cliente')

    if submitted:
        # Chama a função de inserirDados do funcoes.py e obtém o status e a mensagem
        success, message = funcoes.inserirDados(nome, email, telefone)
        if success:
            st.success(message)
            # Para limpar os campos após o sucesso, clear_on_submit=True no st.form já faz isso.
        else:
            st.error(message)

st.markdown("---") # Linha separadora visual

# --- Seção para Listar Clientes ---
st.subheader('Lista de Clientes Cadastrados')
if st.button('Mostrar Todos os Clientes', key="listar_button"):
    dados = funcoes.listarDados()
    if dados:
        # Cria um DataFrame do pandas para exibir os dados de forma tabular e interativa
        df = pd.DataFrame(dados, columns=['ID', 'Nome', 'Email', 'Telefone'])
        st.dataframe(df) # st.dataframe oferece funcionalidades como ordenação e busca
    else:
        st.info("Nenhum cliente cadastrado ainda. Use a seção acima para adicionar um novo cliente.")

# Opcional: Adicionar um rodapé
st.markdown("---")
st.markdown("Desenvolvido com Streamlit e SQLite.")
