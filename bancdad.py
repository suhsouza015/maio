# funcoes.py
import sqlite3

def connectaDB():
    """Estabelece uma conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect('clientes.db')
    return conexao

def inserirDados(nome, email, telefone):
    """
    Insere novos dados de cliente no banco de dados.
    Retorna True e uma mensagem de sucesso em caso de êxito,
    ou False e uma mensagem de erro em caso de falha (ex: e-mail duplicado, campos vazios).
    """
    if not nome or not email or not telefone:
        return False, "Todos os campos são obrigatórios."

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
        return False, f"O e-mail '{email}' já existe. Por favor, use um e-mail único."
    except Exception as e:
        return False, f"Ocorreu um erro inesperado: {e}"
    finally:
        conexao.close()

def listarDados():
    """Busca todos os dados de clientes no banco de dados."""
    conexao = connectaDB()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()
    conexao.close()
    return dados
