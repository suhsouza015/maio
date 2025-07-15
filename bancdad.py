import sqlite3
import streamlit as st
import pandas as pd
import funcoes


conexao = sqlite3.connect('clientes.db')

cursor = conexao.cursor()

cursor.execute(
    '''CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL
    )'''
)


cursor.close()
print("Tabela 'clientes' criada com sucesso!") 

def connectaDB():
    conexao = sqlite3.connect('clientes.db')
    return conexao

def inserirDados(nome, email, telefone):
    conexao = connectaDB()
    cursor = conexao.cursor()
    cursor.execute("insert into clientes (nome, email, telefone) values (?, ?, ?)", (nome, email, telefone))
    conexao.commit()
    conexao.close()

def listarDados():
    conexao = connectaDB()
    cursor = conexao.cursor()
    cursor.execute("select * from clientes")
    dados = cursor.fetchall()
    cursor.close()
    return dados

st.title('Cadastro de Clientes')
nome = st.text_input('Nome do Cliente')
email = st.text_input('Email do Cliente')
telefone = st.text_input('Telefone do Cliente')

if st.button('Cadastrar'):
    funcoes.inserirDados(nome, email, telefone)
    st.success('Cliente cadastrado com sucesso!')

if st.button('Listar Clientes'):
    dados = funcoes.listarDados()
    tb = pd.DataFrame(dados, columns=['ID', 'Nome', 'Email', 'Telefone'])
    st.header('Lista de Clientes')
    st.table(tb)
    st.success('Dados listados com sucesso!')
