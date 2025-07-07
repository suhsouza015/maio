import streamlit as st
import random # Para o quiz

def modulo_basico():
    st.header("Módulo Básico: Primeiros Passos em Python")
    st.write("Este módulo cobre os fundamentos essenciais da programação em Python.")

    st.subheader("1. Variáveis e Tipos de Dados")
    st.write("""
    Variáveis são usadas para armazenar informações que podem ser usadas e manipuladas em seu programa.
    Python é dinamicamente tipado, o que significa que você não precisa declarar o tipo de uma variável.
    """)
    st.code("""
    # Exemplo de variáveis e tipos de dados
    nome = "Python" # String (texto)
    idade = 30      # Inteiro (número sem casas decimais)
    altura = 1.75   # Float (número com casas decimais)
    estudante = True # Booleano (Verdadeiro/Falso)

    print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudante: {estudante}")
    """)
    st.write("---")

    st.subheader("2. Operadores Aritméticos e Lógicos")
    st.write("""
    Operadores aritméticos são usados para realizar operações matemáticas.
    Operadores lógicos (AND, OR, NOT) são usados para combinar ou negar condições.
    """)
    st.code("""
    # Operadores aritméticos
    a = 10
    b = 5

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    resto = a % b
    potencia = a ** b

    print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}, Resto: {resto}, Potência: {potencia}")

    # Operadores lógicos
    tem_idade = True
    tem_carteira = False

    pode_dirigir = tem_idade and tem_carteira # Ambas precisam ser Verdadeiras
    print(f"Pode dirigir (AND): {pode_dirigir}")

    tem_dinheiro = False
    tem_cartao = True
    pode_comprar = tem_dinheiro or tem_cartao # Uma ou ambas precisam ser Verdadeiras
    print(f"Pode comprar (OR): {pode_comprar}")

    nao_chove = not True # Negação
    print(f"Não chove (NOT): {nao_chove}")
    """)
    st.write("---")

    st.subheader("3. Entrada de Dados (input()) e Formatação de Strings")
    st.write("""
    Use `input()` para obter dados do usuário. F-strings (formatted string literals) são uma forma moderna e fácil de formatar strings.
    """)
    st.code("""
    # Exemplo de input() (execute no seu terminal Python para testar a entrada)
    # nome_usuario = input("Qual o seu nome? ")
    # print(f"Olá, {nome_usuario}! Bem-vindo ao curso.")

    # Formatação de strings com f-strings
    produto = "Celular"
    preco = 999.99
    quantidade = 2
    total = preco * quantidade

    print(f"Você comprou {quantidade} unidades de {produto}. O total é R${total:.2f}.")
    """)
    st.write("---")

    st.subheader("4. Estruturas Condicionais (if/elif/else)")
    st.write("""
    Estruturas condicionais permitem que você execute diferentes blocos de código
    com base em uma condição ser verdadeira ou falsa.
    """)
    st.code("""
    # Estruturas condicionais
    idade = 18

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

    temperatura = 25
    if temperatura > 30:
        print("Está muito quente!")
    elif temperatura > 20:
        print("Temperatura agradável.")
    else:
        print("Está frio.")
    """)
    st.write("---")

    st.subheader("5. Estruturas de Repetição (for/while)")
    st.write("""
    Estruturas de repetição permitem que você execute um bloco de código
    repetidamente.
    """)
    st.code("""
    # Loop for
    frutas = ["maçã", "banana", "cereja"]
    for fruta in frutas:
        print(f"Eu gosto de {fruta}")

    # Loop while
    contador = 0
    while contador < 5:
        print(f"Contador: {contador}")
        contador += 1
    """)
    st.write("---")

    st.subheader("Exercício Interativo: Verificador de Par ou Ímpar")
    st.write("Digite um número para verificar se ele é par ou ímpar.")
    numero_str = st.text_input("Digite um número inteiro:", key="ex1_basico")
    if numero_str:
        try:
            numero = int(numero_str)
            if numero % 2 == 0:
                st.success(f"O número {numero} é PAR.")
            else:
                st.info(f"O número {numero} é ÍMPAR.")
        except ValueError:
            st.error("Por favor, digite um número inteiro válido.")
    st.write("---")

def modulo_intermediario():
    st.header("Módulo Intermediário: Aprofundando em Python")
    st.write("Este módulo aborda tópicos que aprofundam seu conhecimento em Python.")

    st.subheader("1. Funções")
    st.write("""
    Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
    Elas ajudam a organizar o código e torná-lo mais modular.
    """)
    st.code("""
    # Definição e chamada de uma função
    def saudar(nome):
        return f"Olá, {nome}!"

    mensagem = saudar("Mundo")
    print(mensagem)

    def soma(a, b):
        return a + b

    resultado = soma(10, 20)
    print(f"A soma é: {resultado}")
    """)
    st.write("---")

    st.subheader("2. Listas, Tuplas, Dicionários e Conjuntos")
    st.write("""
    Python oferece diversas estruturas de dados para organizar informações.
    """)
    st.markdown("""
    * **Listas**: Coleções ordenadas e **mutáveis** (podem ser alteradas).
        * `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `len()`
    * **Tuplas**: Coleções ordenadas e **imutáveis** (não podem ser alteradas).
        * Úteis para dados que não devem mudar, como coordenadas.
    * **Dicionários**: Coleções não ordenadas de pares **chave-valor**.
        * Acesso rápido a valores através de suas chaves.
    * **Conjuntos**: Coleções **não ordenadas** de itens **únicos**.
        * Úteis para remover duplicatas e operações de conjuntos (união, interseção).
    """)
    st.code("""
    # Exemplos de estruturas de dados
    lista = [1, 2, 3, "quatro"]
    lista.append(5) # Adiciona um item
    lista.remove(1) # Remove um item
    print(f"Lista: {lista}")

    tupla = (10, 20, 30)
    # tupla.append(40) # Isso causaria um erro, tuplas são imutáveis
    print(f"Tupla: {tupla}")

    dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
    dicionario["idade"] = 31 # Altera um valor
    dicionario["email"] = "joao@email.com" # Adiciona um novo par
    print(f"Dicionário: {dicionario}")
    print(f"Idade do dicionário: {dicionario['idade']}")

    conjunto = {1, 2, 2, 3, 4, 4} # Itens duplicados são ignorados
    conjunto.add(5) # Adiciona um item
    print(f"Conjunto: {conjunto}")

    # Compreensões de lista (List Comprehensions) - forma concisa de criar listas
    quadrados = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
    print(f"Quadrados: {quadrados}")
    """)
    st.write("---")

    st.subheader("3. Manipulação de Strings")
    st.write("""
    Python oferece métodos poderosos para trabalhar com strings.
    """)
    st.code("""
    texto = "Hello, Python!"

    print(f"Tamanho da string: {len(texto)}")
    print(f"Maiúscula: {texto.upper()}")
    print(f"Minúscula: {texto.lower()}")
    print(f"Substituir 'Python' por 'Streamlit': {texto.replace('Python', 'Streamlit')}")
    print(f"Começa com 'Hello': {texto.startswith('Hello')}")
    print(f"Split por vírgula: {texto.split(',')}")
    """)
    st.write("---")

    st.subheader("4. Tratamento de Erros (try/except)")
    st.write("""
    O tratamento de erros permite que seu programa lide com exceções
    (erros) de forma elegante, evitando que o programa trave.
    """)
    st.code("""
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
    except TypeError: # Você pode capturar múltiplos tipos de erro
        print("Erro de tipo!")
    finally: # O bloco finally sempre será executado, ocorrendo erro ou não
        print("Operação finalizada (mesmo com erro).")

    try:
        numero = int("abc")
    except ValueError:
        print("Erro: Não foi possível converter para número inteiro.")
    """)
    st.write("---")

    st.subheader("Exercício: Calculadora Simples com Tratamento de Erros")
    st.write("Digite dois números e uma operação (+, -, *, /).")
    num1_str = st.text_input("Primeiro número:", key="ex_calc_num1")
    num2_str = st.text_input("Segundo número:", key="ex_calc_num2")
    operacao = st.text_input("Operação (+, -, *, /):", key="ex_calc_op")

    if st.button("Calcular", key="btn_calcular"):
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    st.error("Erro: Divisão por zero não é permitida.")
                    resultado = "Erro"
                else:
                    resultado = num1 / num2
            else:
                st.warning("Operação inválida. Use +, -, *, ou /.")
                resultado = "Erro"

            if resultado != "Erro":
                st.success(f"Resultado: {resultado}")

        except ValueError:
            st.error("Erro: Por favor, insira números válidos.")

    st.write("---")

def modulo_avancado():
    st.header("Módulo Avançado: Tópicos Complexos em Python")
    st.write("Este módulo explora conceitos mais avançados e poderosos de Python.")

    st.subheader("1. Programação Orientada a Objetos (POO)")
    st.write("""
    POO é um paradigma de programação baseado no conceito de "**objetos**",
    que podem conter **dados** (atributos) e **código** (métodos).
    Abstracão, Encapsulamento, Herança e Polimorfismo são pilares da POO.
    """)
    st.code("""
    class Carro:
        def __init__(self, marca, modelo, ano): # Construtor da classe
            self.marca = marca # Atributos
            self.modelo = modelo
            self.ano = ano
            self.velocidade = 0

        def acelerar(self, incremento): # Método
            self.velocidade += incremento
            return f"{self.modelo} acelerou para {self.velocidade} km/h."

        def exibir_info(self): # Método
            return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

    # Criando objetos (instâncias da classe Carro)
    meu_carro = Carro("Toyota", "Corolla", 2023)
    outro_carro = Carro("Honda", "Civic", 2024)

    st.write(f"Informações do meu carro: {meu_carro.exibir_info()}")
    st.write(f"Informações do outro carro: {outro_carro.exibir_info()}")
    st.write(meu_carro.acelerar(50))

    # Herança: Criando uma subclasse
    class Eletrico(Carro):
        def __init__(self, marca, modelo, ano, autonomia):
            super().__init__(marca, modelo, ano) # Chama o construtor da classe pai
            self.autonomia = autonomia

        def carregar(self):
            return f"{self.modelo} está carregando a bateria."

    tesla = Eletrico("Tesla", "Model S", 2024, 600)
    st.write(tesla.exibir_info())
    st.write(tesla.carregar())
    """)
    st.write("---")

    st.subheader("2. Manipulação de Arquivos")
    st.write("""
    Aprenda a ler e escrever em arquivos de texto.
    O uso de `with open(...) as f:` garante que o arquivo seja fechado automaticamente.
    """)
    st.code("""
    # Escrever em um arquivo
    conteudo_para_escrever = "Olá, este é um teste de escrita de arquivo.\\nMais uma linha.\\n"
    with open("meu_arquivo.txt", "w") as f: # 'w' para escrita (cria/sobrescreve)
        f.write(conteudo_para_escrever)

    st.write("Arquivo 'meu_arquivo.txt' criado e escrito.")

    # Ler de um arquivo
    try:
        with open("meu_arquivo.txt", "r") as f: # 'r' para leitura
            conteudo = f.read() # Lê todo o conteúdo
            st.write("Conteúdo do arquivo 'meu_arquivo.txt':")
            st.code(conteudo)
    except FileNotFoundError:
        st.error("Arquivo 'meu_arquivo.txt' não encontrado.")

    # Adicionar conteúdo ao arquivo (modo 'a' - append)
    with open("meu_arquivo.txt", "a") as f:
        f.write("Esta linha foi adicionada depois.\\n")
    st.write("Conteúdo adicional foi escrito no arquivo.")

    with open("meu_arquivo.txt", "r") as f:
        conteudo_atualizado = f.read()
        st.write("Conteúdo atualizado do arquivo 'meu_arquivo.txt':")
        st.code(conteudo_atualizado)
    """)
    st.write("---")

    st.subheader("3. Módulos e Pacotes")
    st.write("""
    **Módulos** são arquivos Python contendo definições e declarações Python (funções, classes, variáveis).
    **Pacotes** são coleções de módulos, organizados em diretórios.
    """)
    st.code("""
    # Exemplo de importação de módulo
    import math

    st.write(f"Valor de PI: {math.pi}")
    st.write(f"Raiz quadrada de 16: {math.sqrt(16)}")

    # Você também pode importar partes específicas de um módulo
    from datetime import date, datetime # Importando múltiplas coisas
    hoje = date.today()
    agora = datetime.now()
    st.write(f"Data de hoje: {hoje}")
    st.write(f"Data e hora agora: {agora}")

    # Importando com alias
    import numpy as np
    array_numpy = np.array([1, 2, 3])
    st.write(f"Array numpy: {array_numpy}")
    """)
    st.write("---")

    st.subheader("4. Decoradores")
    st.write("""
    **Decoradores** são funções que modificam o comportamento de outras funções
    ou métodos. Eles usam a sintaxe `@` antes da definição da função.
    """)
    st.code("""
    def meu_decorador(func):
        def wrapper(*args, **kwargs): # Permite que a função decorada receba argumentos
            st.write("Antes da função ser chamada.")
            resultado = func(*args, **kwargs) # Chama a função original
            st.write("Depois da função ser chamada.")
            return resultado
        return wrapper

    @meu_decorador
    def saudacao(nome):
        st.write(f"Olá, {nome}! Minha função está sendo executada.")
        return f"Saudação para {nome} concluída."

    saudacao("Alice")

    @meu_decorador
    def soma_dois_numeros(a, b):
        s = a + b
        st.write(f"A soma de {a} e {b} é {s}")
        return s

    soma_dois_numeros(5, 3)
    """)
    st.write("---")

    st.subheader("5. Geradores e Iteradores")
    st.write("""
    **Geradores** são funções que retornam um iterador que produz uma sequência
    de resultados sob demanda usando a palavra-chave `yield`, economizando memória.
    **Iteradores** são objetos que implementam os métodos `__iter__()` e `__next__()`.
    """)
    st.code("""
    def gerador_numeros_pares(limite):
        n = 0
        while n <= limite:
            yield n
            n += 2

    st.write("Números pares gerados (até 10):")
    for num in gerador_numeros_pares(10):
        st.write(num)

    # Exemplo de iterador manual
    minha_lista = [10, 20, 30]
    meu_iterador = iter(minha_lista) # Obtém um iterador da lista

    try:
        st.write(f"Primeiro item: {next(meu_iterador)}") # Pega o próximo item
        st.write(f"Segundo item: {next(meu_iterador)}")
        st.write(f"Terceiro item: {next(meu_iterador)}")
        # st.write(f"Quarto item: {next(meu_iterador)}") # Isso causaria um StopIteration
    except StopIteration:
        st.write("Fim dos itens do iterador.")
    """)
    st.write("---")

    st.subheader("6. Expressões Regulares (regex)")
    st.write("""
    **Expressões Regulares** (regex) são sequências de caracteres que formam um
    padrão de busca. Elas são usadas para encontrar e manipular textos complexos.
    O módulo `re` do Python é usado para trabalhar com regex.
    """)
    st.code("""
    import re

    texto = "Meu e-mail é exemplo@dominio.com.br e outro é teste@mail.org"

    # Encontrar todos os e-mails no texto
    padrao_email = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
    emails_encontrados = re.findall(padrao_email, texto)
    st.write(f"E-mails encontrados: {emails_encontrados}")

    # Substituir um padrão
    texto_modificado = re.sub(r'e-mail', 'endereço eletrônico', texto)
    st.write(f"Texto modificado: {texto_modificado}")

    # Verificar se um padrão existe (match)
    if re.match(r'Meu', texto):
        st.write("O texto começa com 'Meu'.")
    else:
        st.write("O texto não começa com 'Meu'.")
    """)
    st.write("---")


# --- Quizes ---
def quiz_basico():
    st.subheader("Quiz: Módulo Básico")
    st.write("Teste seus conhecimentos do Módulo Básico!")

    perguntas = [
        {
            "pergunta": "Qual operador é usado para potenciação em Python?",
            "opcoes": ["*", "**", "/", "%"],
            "resposta": "**"
        },
        {
            "pergunta": "Qual estrutura de controle usamos para decidir entre diferentes blocos de código?",
            "opcoes": ["for", "while", "if/elif/else", "def"],
            "resposta": "if/elif/else"
        },
        {
            "pergunta": "Qual função é usada para obter entrada de texto do usuário?",
            "opcoes": ["print()", "input()", "len()", "str()"],
            "resposta": "input()"
        }
    ]

    respostas_corretas = 0
    for i, p in enumerate(perguntas):
        st.markdown(f"**{i+1}. {p['pergunta']}**")
        resposta_usuario = st.radio(
            "Selecione sua resposta:",
            p["opcoes"],
            key=f"q_basico_{i}"
        )
        if st.button("Verificar Resposta", key=f"btn_basico_{i}"):
            if resposta_usuario == p["resposta"]:
                st.success("Correto!")
                respostas_corretas += 1
            else:
                st.error(f"Incorreto. A resposta correta é: **{p['resposta']}**")
        st.write("---")

    if st.button("Finalizar Quiz Básico", key="finalizar_basico"):
        st.info(f"Você acertou {respostas_corretas} de {len(perguntas)} perguntas.")

def quiz_avancado():
    st.subheader("Quiz: Módulo Avançado")
    st.write("Teste seus conhecimentos do Módulo Avançado!")

    perguntas_avancadas = [
        {
            "pergunta": "Qual palavra-chave é usada para definir uma classe em Python?",
            "opcoes": ["function", "class", "def", "object"],
            "resposta": "class"
        },
        {
            "pergunta": "Em POO, o que `__init__` representa?",
            "opcoes": ["Um método normal", "Um construtor", "Um destrutor", "Uma variável de classe"],
            "resposta": "Um construtor"
        },
        {
            "pergunta": "Qual a principal diferença entre um gerador e uma função normal?",
            "opcoes": ["Geradores usam 'return'", "Geradores usam 'yield'", "Funções são mais lentas", "Geradores não podem receber argumentos"],
            "resposta": "Geradores usam 'yield'"
        }
    ]

    respostas_corretas_avancado = 0
    for i, p in enumerate(perguntas_avancadas):
        st.markdown(f"**{i+1}. {p['pergunta']}**")
        resposta_usuario = st.radio(
            "Selecione sua resposta:",
            p["opcoes"],
            key=f"q_avancado_{i}"
        )
        if st.button("Verificar Resposta", key=f"btn_avancado_{i}"):
            if resposta_usuario == p["resposta"]:
                st.success("Correto!")
                respostas_corretas_avancado += 1
            else:
                st.error(f"Incorreto. A resposta correta é: **{p['resposta']}**")
        st.write("---")

    if st.button("Finalizar Quiz Avançado", key="finalizar_avancado"):
        st.info(f"Você acertou {respostas_corretas_avancado} de {len(perguntas_avancadas)} perguntas.")

# --- Configuração da página do Streamlit ---
st.set_page_config(layout="wide", page_title="Curso de Python Interativo")

st.title("Curso Interativo de Python com Streamlit")
st.write("Bem-vindo ao seu guia completo para aprender Python, do básico ao avançado!")

# Barra lateral para navegação
st.sidebar.title("Navegação")
modulo_selecionado = st.sidebar.radio(
    "Escolha um módulo:",
    ("Introdução", "Básico", "Intermediário", "Avançado", "Quiz Básico", "Quiz Avançado")
)

if modulo_selecionado == "Introdução":
    st.header("Comece sua jornada em Python!")
    st.write("""
    Este aplicativo interativo foi criado para te ajudar a aprender Python de forma prática e didática.
    Utilize a barra lateral para navegar entre os módulos. Cada módulo contém explicações e exemplos de código que você pode copiar e testar.

    **O que é Python?**
    Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. É amplamente utilizada em desenvolvimento web, análise de dados, inteligência artificial, automação e muito mais.

    **Por que aprender Python?**
    * **Simples e legível**: Sintaxe clara e concisa.
    * **Versátil**: Usado em diversas áreas.
    * **Comunidade Ativa**: Grande suporte e muitos recursos disponíveis.
    * **Bibliotecas e Frameworks**: Enorme ecossistema para diversas finalidades.
    """)
    st.image("https://www.python.org/static/community_logos/python-logo-only.png", width=200)

elif modulo_selecionado == "Básico":
    modulo_basico()
elif modulo_selecionado == "Intermediário":
    modulo_intermediario()
elif modulo_selecionado == "Avançado":
    modulo_avancado()
elif modulo_selecionado == "Quiz Básico":
    quiz_basico()
elif modulo_selecionado == "Quiz Avançado":
    quiz_avancado()

st.sidebar.markdown("---")
st.sidebar.info("Este é um projeto em desenvolvimento. Novas funcionalidades e conteúdos serão adicionados!")
