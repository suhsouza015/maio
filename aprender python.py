import streamlit as st
import random
import time # Para simular um tempo de carregamento em exemplo

# --- Configurações da Página ---
st.set_page_config(
    page_title="Curso de Python Interativo",
    page_icon="🐍",
    layout="wide" # Usa a largura máxima da tela
)

# --- Função do Módulo Básico ---
def modulo_basico():
    st.header("Módulo Básico: Primeiros Passos em Python")
    st.write("Este módulo cobre os fundamentos essenciais da programação em Python, preparando você para construir lógicas simples e entender como o Python funciona.")

    with st.expander("1. Variáveis e Tipos de Dados", expanded=True):
        st.write("""
        Em programação, **variáveis** são como "caixas" nomeadas na memória do computador que armazenam informações. Imagine que você está rotulando uma caixa para saber o que tem dentro dela mais tarde. Em Python, você não precisa dizer qual tipo de coisa vai guardar na caixa (como número, texto, etc.); o Python descobre isso automaticamente no momento da atribuição. Isso é chamado de **tipagem dinâmica**. Além disso, Python é uma linguagem de **tipagem forte**, o que significa que ela não fará conversões de tipo implícitas onde pode haver perda de dados ou comportamento inesperado (por exemplo, você não pode somar um número diretamente com um texto sem converter um deles).

        Os **tipos de dados** básicos (ou "primitivos") em Python incluem:
        * **Inteiros (`int`)**: Números inteiros, positivos ou negativos, sem casas decimais. Usados para contagens, IDs, etc. (ex: `10`, `-5`, `1000000`).
        * **Floats (`float`)**: Números com casas decimais, representando valores reais. Essenciais para cálculos financeiros, medições, etc. (ex: `3.14`, `-0.5`, `2.0`).
        * **Strings (`str`)**: Sequências de caracteres, como letras, palavras ou frases. São sempre delimitadas por aspas simples (`'`) ou duplas (`"`). Usadas para manipular texto em geral.
        * **Booleanos (`bool`)**: Representam apenas dois valores: `True` (verdadeiro) ou `False` (falso). São a base de toda a lógica de decisão em programação.

        **Por que são importantes?** Escolher o tipo de dado correto não só otimiza o uso da memória, mas também garante que as operações realizadas sobre os dados sejam semanticamente corretas e eficientes.
        """)
        st.code("""
# Exemplo de variáveis e tipos de dados
nome = "Alice"           # String (texto entre aspas)
idade = 25               # Inteiro (número sem ponto decimal)
altura = 1.68            # Float (número com ponto decimal)
eh_estudante = True      # Booleano (Verdadeiro ou Falso)
preco_unitario = 49.99   # Float

print(f"Nome: {nome} (Tipo: {type(nome)})") # type() retorna o tipo da variável
print(f"Idade: {idade} (Tipo: {type(idade)})")
print(f"Altura: {altura} (Tipo: {type(altura)})")
print(f"É estudante: {eh_estudante} (Tipo: {type(eh_estudante)})")
print(f"Preço: {preco_unitario} (Tipo: {type(preco_unitario)})")

# Reatribuindo uma variável (a caixa pode guardar outra coisa)
# Atenção: Isso muda o tipo da variável 'idade' de int para str.
idade = "vinte e cinco"
print(f"Nova idade: {idade} (Tipo: {type(idade)})")

# Conversão de tipos (Type Casting)
# Às vezes, você precisa explicitamente mudar o tipo de uma variável.
numero_como_texto = "123"
numero_inteiro = int(numero_como_texto) # Converte string para inteiro
print(f"Número como texto: {numero_como_texto} (Tipo: {type(numero_como_texto)})")
print(f"Número inteiro: {numero_inteiro} (Tipo: {type(numero_inteiro)})")

# float para int trunca a parte decimal, não arredonda
pi_arredondado = int(3.99)
print(f"int(3.99): {pi_arredondado}") # Saída: 3

""")
        st.write("""
        **Melhores Práticas:**
        * Use nomes de variáveis descritivos (ex: `nome_cliente` em vez de `nc`).
        * Siga as convenções do Python: nomes de variáveis e funções em `snake_case` (minúsculas com underscores).
        * Evite usar palavras reservadas do Python (como `if`, `for`, `class`) como nomes de variáveis.

        **Erro Comum:** Tentar operar com tipos de dados incompatíveis sem conversão, como `5 + "olá"`, o que resultaria em um `TypeError`.
        """)
        st.write("---")

    with st.expander("2. Operadores Aritméticos e Lógicos"):
        st.write("""
        **Operadores aritméticos** são símbolos usados para realizar cálculos matemáticos. Eles seguem a tradicional **ordem de precedência** (similar ao PEMDAS/BODMAS): Parênteses, Expoentes, Multiplicação e Divisão (da esquerda para a direita), Adição e Subtração (da esquerda para a direita). Compreender essa ordem é crucial para evitar erros lógicos em seus cálculos.

        **Operadores de comparação** (`==`, `!=`, `<`, `<=`, `>`, `>=`) são usados para comparar dois valores e sempre retornam um valor booleano (`True` ou `False`).

        **Operadores lógicos** (`and`, `or`, `not`) são usados para combinar ou inverter expressões booleanas, ajudando a construir condições mais complexas em suas tomadas de decisão. Eles são a espinha dorsal de qualquer fluxo de controle.
        """)
        st.markdown("""
        * **Aritméticos:**
            * `+` : Adição (ex: `5 + 3` resulta `8`)
            * `-` : Subtração (ex: `10 - 4` resulta `6`)
            * `*` : Multiplicação (ex: `2 * 7` resulta `14`)
            * `/` : Divisão (sempre retorna um `float`, ex: `7 / 2` resulta `3.5`)
            * `//` : Divisão inteira (descarta a parte decimal, ex: `7 // 2` resulta `3`)
            * `%` : Módulo (retorna o resto da divisão, ex: `7 % 2` resulta `1`)
            * `**` : Potenciação (ex: `2 ** 3` resulta `8`, 2 elevado a 3)
        * **Comparação:**
            * `==` : Igual a (ex: `5 == 5` é `True`, `5 == 6` é `False`)
            * `!=` : Diferente de (ex: `5 != 6` é `True`)
            * `<` : Menor que
            * `<=` : Menor ou igual a
            * `>` : Maior que
            * `>=` : Maior ou igual a
        * **Lógicos:**
            * `and` : Retorna `True` se *ambas* as condições forem verdadeiras. Usado quando todas as condições precisam ser satisfeitas.
            * `or` : Retorna `True` se *pelo menos uma* das condições for verdadeira. Usado quando qualquer uma das condições é suficiente.
            * `not` : Inverte o valor booleano ( `not True` é `False`, `not False` é `True`). Usado para negar uma condição.
        """)
        st.code("""
# Operadores aritméticos em ação
x = 20
y = 7

print(f"x + y = {x + y}")        # Adição: 27
print(f"x - y = {x - y}")        # Subtração: 13
print(f"x * y = {x * y}")        # Multiplicação: 140
print(f"x / y = {x / y}")        # Divisão (float): 2.857...
print(f"x // y = {x // y}")      # Divisão inteira: 2
print(f"x % y = {x % y}")        # Módulo (resto): 6 (20 = 2*7 + 6)
print(f"x ** 2 = {x ** 2}")      # Potenciação: 400 (20 elevado a 2)

# Exemplo de precedência: Multiplicação/divisão antes de adição/subtração
calculo = 5 + 3 * 2 # É 5 + (3 * 2) = 5 + 6 = 11, não (5 + 3) * 2 = 16
print(f"Resultado de 5 + 3 * 2 = {calculo}")

# Operadores de Comparação em ação
print(f"x == y? {x == y}")   # False (20 não é igual a 7)
print(f"x > y? {x > y}")     # True (20 é maior que 7)
print(f"x != y? {x != y}")   # True (20 é diferente de 7)

# Operadores lógicos em ação
tem_permissao = True
idade_minima = 18
minha_idade = 20

# Usando 'and': Precisa ser maior ou igual a 18 E ter permissão
pode_entrar = (minha_idade >= idade_minima) and tem_permissao
print(f"Pode entrar (idade >= 18 e permissão)? {pode_entrar}") # True (ambas as condições são True)

tem_ingresso = False
tem_convite = True

# Usando 'or': Precisa ter ingresso OU convite
pode_assistir = tem_ingresso or tem_convite
print(f"Pode assistir (ingresso ou convite)? {pode_assistir}") # True (pelo menos uma condição é True)

# Usando 'not': Inverte o valor booleano
tem_dinheiro = False
nao_tem_dinheiro = not tem_dinheiro
print(f"Não tem dinheiro? {nao_tem_dinheiro}") # True (inverte False para True)

# Combinando operadores: Cuidado com parênteses para clareza e precedência
condicao_complexa = (minha_idade > 25 and tem_permissao) or tem_convite
print(f"Condição complexa: {condicao_complexa}") # (False and True) or True = False or True = True
""")
        st.write("""
        **Melhores Práticas:**
        * Use parênteses para agrupar operações complexas e deixar a intenção clara, mesmo que a precedência já garanta o resultado desejado. Isso melhora a legibilidade.
        * Não confunda `=` (atribuição) com `==` (comparação de igualdade).

        **Erro Comum:** Esquecer a precedência de operadores, levando a resultados inesperados em cálculos complexos.
        """)
        st.write("---")

    with st.expander("3. Entrada de Dados (`input()`) e Formatação de Strings (f-strings)"):
        st.write("""
        Para que seus programas sejam interativos, muitas vezes você precisará obter informações do usuário. A função `input()` faz exatamente isso: ela pausa o programa, exibe uma mensagem no console e espera que o usuário digite algo, retornando essa entrada sempre como uma **string**. Mesmo que o usuário digite um número, `input()` o lerá como texto, e você precisará convertê-lo (com `int()` ou `float()`) se quiser realizar operações numéricas.

        Quando você quer exibir informações combinando texto estático e valores de variáveis de forma elegante e eficiente, as **f-strings** (formatted string literals) são a melhor ferramenta em Python 3.6+. Elas permitem que você incorpore expressões Python (variáveis, chamadas de função simples, etc.) diretamente dentro de strings, prefixando a string com um `f` ou `F`. Isso as torna muito mais legíveis e concisas do que métodos de formatação mais antigos como `%` ou `.format()`.
        """)
        st.code("""
# Usando input() para obter dados do usuário
# Observação: 'input()' só funciona no console/terminal, não em interfaces web como Streamlit diretamente.
# Você usará st.text_input no Streamlit para essa finalidade.

# Formatação de strings com f-strings (o 'f' antes das aspas é crucial!)
produto = "Notebook Gamer"
preco = 7500.50
desconto = 0.10 # 10%

preco_final = preco * (1 - desconto)

# Formatação de float para 2 casas decimais com ': .2f'
print(f"O produto '{produto}' custa R${preco:.2f}.") # :.2f formata para 2 casas decimais

# Formatação de float como porcentagem com ': .0%'
print(f"Com um desconto de {desconto:.0%}, o preço final é R${preco_final:.2f}.") # :.0% formata como porcentagem sem casas decimais

# F-strings são poderosas para combinar diferentes tipos e expressões
minha_idade = 30
print(f"Eu tenho {minha_idade} anos e no ano que vem terei {minha_idade + 1} anos.")

# Alinhamento e preenchimento
nome_aluno = "Ana"
nota = 9.5
print(f"|{nome_aluno:<10}|{nota:^5.1f}|") # Alinha à esquerda (10 chars), centraliza (5 chars, 1 decimal)
# Saída no terminal: |Ana        | 9.5 |
""")
        st.write("""
        **Melhores Práticas:**
        * Sempre use f-strings para formatação de strings em código moderno Python.
        * Após coletar entrada com `st.text_input` no Streamlit, use `int()`, `float()`, etc., para converter para o tipo numérico adequado antes de realizar operações matemáticas.

        **Erro Comum:** Esquecer de converter a entrada do `input()` (ou `st.text_input`) para um tipo numérico ao tentar fazer cálculos, resultando em `TypeError` (e.g., `ValueError` se a conversão falhar, como `int("abc")`).
        """)
        st.write("---")

    with st.expander("4. Estruturas Condicionais (`if`/`elif`/`else`)"):
        st.write("""
        As **estruturas condicionais** são o que permitem que seu programa "tome decisões" e execute diferentes blocos de código com base em certas condições. Elas são a base para criar lógica de ramificação em seus programas. Uma condição é uma expressão que resulta em `True` ou `False` (um booleano).

        * **`if`**: O bloco de código sob o `if` só é executado se a condição for `True`. É o ponto de partida de qualquer cadeia condicional.
        * **`elif` (else if)**: Se a condição `if` for `False`, o programa verifica a condição do `elif` seguinte. Você pode ter múltiplos `elif` para testar várias condições sequencialmente. O primeiro `elif` cuja condição for `True` terá seu bloco executado, e o resto da cadeia será ignorado.
        * **`else`**: Se *todas* as condições `if` e `elif` anteriores forem `False`, o bloco `else` é executado. O `else` é opcional e serve como uma "captura" para qualquer caso que não se encaixe nas condições anteriores.

        A **indentação** (espaçamento no início da linha, geralmente 4 espaços) é crucial em Python! Ela define os blocos de código pertencentes a cada `if`, `elif` ou `else`. Python usa indentação para delimitar blocos, enquanto outras linguagens podem usar chaves `{}`.

        **Por que são importantes?** Sem condicionais, seu programa seguiria sempre o mesmo caminho. Elas permitem criar programas que respondem a diferentes entradas, estados ou situações, tornando-os dinâmicos e úteis.
        """)
        st.code("""
# Exemplo: Verificando a faixa etária e dando recomendações
idade_visitante = 17

if idade_visitante >= 18:
    print("Você é maior de idade. Acesso liberado para todas as áreas.")
elif idade_visitante >= 13: # Se não for >= 18, verifica se é >= 13
    print("Você é adolescente. Acesso com restrições para algumas áreas.")
else: # Se não for nem >= 18 nem >= 13
    print("Você é criança. Acesso negado, necessário acompanhamento de adulto.")

# Exemplo com uma única condição
chovendo = True
if chovendo: # É o mesmo que 'if chovendo == True:' - mais conciso
    print("Leve um guarda-chuva!")
    print("Considere usar galochas.") # Múltiplas linhas dentro do bloco

# Exemplo com 'not' na condição
saldo = 500
compra = 600
# if not (saldo >= compra): significa "Se não for verdade que saldo é maior ou igual à compra"
if not (saldo >= compra):
    print("Saldo insuficiente para a compra.")
else:
    print("Compra realizada com sucesso!")

# Múltiplas condições na mesma linha com operadores lógicos
# Apenas entra se a idade estiver entre 18 e 60 (inclusive)
idade_candidato = 25
if idade_candidato >= 18 and idade_candidato <= 60:
    print("Candidato elegível pela idade.")

# Se for jovem ou idoso, oferece desconto
if idade_candidato < 18 or idade_candidato > 60:
    print("Cliente tem direito a desconto especial.")
""")
        st.write("""
        **Melhores Práticas:**
        * Mantenha suas condições claras e concisas. Se uma condição se tornar muito complexa, considere dividi-la em variáveis booleanas intermediárias para melhorar a legibilidade.
        * Use `elif` para cadeias de condições mutuamente exclusivas para evitar que o Python verifique condições desnecessariamente.
        * Sempre se atente à indentação! É a fonte de muitos erros de lógica para iniciantes.

        **Erro Comum:** Erros de indentação, que podem levar a `IndentationError` ou, pior, a um código que executa sem erro mas com lógica incorreta porque um bloco não está onde deveria.
        """)
        st.write("---")

    with st.expander("5. Estruturas de Repetição (`for`/`while`)"):
        st.write("""
        As **estruturas de repetição** (ou laços/loops) são ferramentas poderosas que permitem que você execute um bloco de código várias vezes. Isso é fundamental para automatizar tarefas repetitivas, processar coleções de dados e simular comportamentos contínuos.

        * **`for` loop**: É usado para iterar (percorrer) sobre uma **sequência** (como uma string, lista, tupla, ou um `range` de números) ou outros objetos "iteráveis". Ele executa o bloco de código uma vez para cada item na sequência, atribuindo o item atual a uma variável temporária em cada iteração.
            * `range(n)`: Gera uma sequência de números de 0 até `n-1`. Ideal para repetir um bloco de código um número fixo de vezes.
            * `range(inicio, fim)`: Gera de `inicio` (inclusive) até `fim-1` (exclusive).
            * `range(inicio, fim, passo)`: Gera de `inicio` até `fim-1` pulando `passo`. `passo` pode ser negativo para contagem regressiva.
        * **`while` loop**: Continua executando o bloco de código *enquanto* uma determinada condição for verdadeira. É ideal quando você não sabe de antemão quantas vezes o loop precisa rodar; a repetição depende de uma condição que muda durante a execução.
            * É crucial garantir que a condição se torne falsa em algum momento, caso contrário, você terá um **loop infinito**, fazendo com que seu programa trave ou consuma muitos recursos!

        Assim como nas condicionais, a **indentação** é crucial para definir o que está dentro do loop.

        **Palavras-chave úteis em loops:**
        * `break`: Sai do loop imediatamente, independentemente da condição do loop. Útil para terminar um loop quando uma condição específica é atingida.
        * `continue`: Pula o restante do código do bloco atual do loop e vai para a próxima iteração. Útil para ignorar certos itens ou situações dentro de um loop.

        **Por que são importantes?** Loops permitem que você trabalhe com grandes volumes de dados (ex: processar todos os itens em uma lista), implemente algoritmos de busca e ordenação, e crie jogos ou simulações onde ações se repetem.
        """)
        st.code("""
# Loop 'for' com uma lista: Processando cada item
ingredientes = ["farinha", "açúcar", "ovos", "leite"]
print("Ingredientes para o bolo:")
for item in ingredientes: # 'item' assume o valor de cada elemento da lista, um por vez
    print(f"- {item}")

# Loop 'for' com range (para repetir um número fixo de vezes)
print("\\nContagem regressiva:")
for i in range(5, 0, -1): # Começa em 5, vai até 1 (0 não incluso), decrementa 1
    print(i)
print("Decolar!")

# Loop 'for' com 'enumerate': Para acessar o item e seu índice
print("\\nItens com seus índices:")
for index, fruta in enumerate(["maçã", "banana", "cereja"]):
    print(f"Índice {index}: {fruta}")

# Loop 'while': Senha com tentativas limitadas (simulada para Streamlit)
# Em um app real, st.text_input ou similar seria usado em vez de simulação
tentativas_senha = 0
senha_correta = "segredo123"
simular_entrada_senha = ""

st.subheader("Simulação de Loop 'While' (Senha)")
st.write("Imagine que você está digitando a senha. Este exemplo usa um loop `while`.")
placeholder_senha = st.empty() # Placeholder para o print dinâmico

while tentativas_senha < 3:
    simular_entrada_senha = placeholder_senha.text_input(
        f"Tentativa {tentativas_senha + 1} de 3: Digite a senha (dica: segredo123)",
        key=f"senha_input_{tentativas_senha}"
    )
    if simular_entrada_senha: # Só processa se algo foi digitado
        if simular_entrada_senha == senha_correta:
            st.success("Senha correta! Acesso concedido.")
            break # Sai do loop
        else:
            st.warning("Senha incorreta. Tente novamente.")
        tentativas_senha += 1
    time.sleep(0.1) # Pequena pausa para evitar sobrecarga no Streamlit

if tentativas_senha >= 3 and simular_entrada_senha != senha_correta:
    st.error("Número máximo de tentativas atingido. Acesso negado.")

st.write("---")

# Exemplo de 'continue': Pulando números pares
print("\\nNúmeros ímpares de 1 a 10 (no terminal):")
for numero in range(1, 11):
    if numero % 2 == 0: # Se o número for par...
        continue # ...pula para a próxima iteração do loop, sem executar o print abaixo
    print(numero) # Este print aparecerá no terminal

st.write("---")
""")
        st.write("""
        **Melhores Práticas:**
        * Use `for` loops quando souber o número de iterações (ou quando estiver iterando sobre uma coleção finita).
        * Use `while` loops quando o número de iterações for desconhecido e depender de uma condição ser satisfeita.
        * Sempre garanta que a condição de um `while` loop eventualmente se tornará falsa para evitar loops infinitos.
        * Aproveite `enumerate()` para acessar tanto o item quanto seu índice em `for` loops.

        **Erro Comum:** Loops infinitos (`while True:` sem uma condição de `break` interna) ou erros de `Off-by-one` (`range(5)` vai de 0 a 4, não a 5).
        """)
        st.write("---")

    st.subheader("Exercício Interativo: Verificador de Par ou Ímpar")
    st.write("Digite um número inteiro no campo abaixo para verificar se ele é par ou ímpar. Observe como o código usa operadores aritméticos (o operador de módulo `%`) e condicionais (`if`/`else`) para tomar essa decisão.")
    numero_str = st.text_input("Digite um número inteiro:", key="ex1_basico")
    if numero_str:
        try:
            numero = int(numero_str)
            if numero % 2 == 0: # O operador % (módulo) retorna o resto da divisão. Se o resto da divisão por 2 for 0, é par.
                st.success(f"O número {numero} é **PAR**.")
            else:
                st.info(f"O número {numero} é **ÍMPAR**.")
        except ValueError:
            st.error("Ops! Isso não parece um número inteiro. Por favor, digite apenas dígitos numéricos.")
    st.write("---")

# --- Função do Módulo Intermediário ---
def modulo_intermediario():
    st.header("Módulo Intermediário: Aprofundando em Python")
    st.write("Este módulo aprofunda seu conhecimento em Python, apresentando conceitos que permitem organizar e otimizar seu código, além de lidar com dados de forma mais eficiente.")

    with st.expander("1. Funções", expanded=True):
        st.write("""
        **Funções** são blocos de código reutilizáveis que realizam uma tarefa específica. Pense nelas como pequenas "máquinas" que você pode chamar a qualquer momento para fazer um trabalho, sem precisar reescrever o mesmo código. Elas são a espinha dorsal de um código bem organizado e são essenciais para:
        * **Organização do código**: Dividir seu programa em partes menores e gerenciáveis, facilitando a leitura e a manutenção.
        * **Reutilização**: Evitar a repetição de código (Princípio DRY - **D**on't **R**epeat **Y**ourself), o que torna o código mais eficiente e menos propenso a erros.
        * **Modularidade**: Tornar o código mais fácil de entender, testar individualmente (unit testing) e depurar, pois cada função tem uma responsabilidade clara.
        * **Abstração**: Esconder a complexidade interna de uma operação, expondo apenas o que é necessário para usá-la.

        Para definir uma função, usamos a palavra-chave `def`, seguida do nome da função, parênteses (que podem conter **parâmetros**), e dois pontos (`:`). O corpo da função (o código que ela executa) é indentado. A palavra-chave `return` é usada para enviar um ou mais valores de volta ao ponto onde a função foi chamada. Se uma função não tem um `return` explícito, ela implicitamente retorna `None`.

        **Parâmetros vs. Argumentos:**
        * **Parâmetros**: São os nomes das variáveis listadas na definição da função (ex: `nome`, `saudacao` em `def saudar_usuario(nome, saudacao)`).
        * **Argumentos**: São os valores reais passados para a função quando ela é chamada (ex: `"Carlos"`, `"Oi"` em `saudar_usuario("Carlos", "Oi")`).
        """)
        st.code("""
# Definindo uma função sem parâmetros e sem retorno (apenas executa uma ação)
def exibir_mensagem_boas_vindas():
    print("Bem-vindo ao mundo das funções em Python!")

exibir_mensagem_boas_vindas() # Chamando a função para executá-la

# Definindo uma função com parâmetros e com retorno
# 'saudacao="Olá"' define um parâmetro com valor padrão.
# Se o chamador não fornecer um valor para 'saudacao', "Olá" será usado.
def saudar_usuario(nome, saudacao="Olá"):
    mensagem = f"{saudacao}, {nome}!"
    return mensagem # Retorna a string resultante

# Chamando a função com diferentes argumentos
mensagem1 = saudar_usuario("Carlos") # Usa o valor padrão para 'saudacao'
print(mensagem1) # Saída: Olá, Carlos!

mensagem2 = saudar_usuario("Maria", "Oi") # Passando um valor explícito para 'saudacao'
print(mensagem2) # Saída: Oi, Maria!

# Funções podem ter múltiplos retornos (retornam uma tupla)
def calcular_operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao # Retorna uma tupla de valores

# Desempacotando os múltiplos retornos em variáveis separadas
resultado_soma, resultado_subtracao, resultado_multiplicacao = calcular_operacoes(10, 5)
print(f"Soma: {resultado_soma}, Subtração: {resultado_subtracao}, Multiplicação: {resultado_multiplicacao}")

# Argumentos nomeados (Keyword Arguments) - Melhoram a legibilidade
print(saudar_usuario(nome="Pedro", saudacao="Bom dia"))
print(saudar_usuario(saudacao="Boa noite", nome="Ana")) # A ordem não importa com argumentos nomeados
""")
        st.write("""
        **Melhores Práticas:**
        * Cada função deve ter uma **única responsabilidade** (Princípio da Responsabilidade Única).
        * Use nomes de funções descritivos (verbos) que indiquem o que a função faz (ex: `calcular_media`, `gerar_relatorio`).
        * Documente suas funções usando **docstrings** (strings de documentação de múltiplas linhas logo abaixo da definição da função) para explicar o que a função faz, seus parâmetros e o que ela retorna.
        * Limite o número de parâmetros para manter a função simples e fácil de usar.

        **Erro Comum:** Esquecer os parênteses ao chamar uma função (o que a referenciaria como um objeto, em vez de executá-la) ou tentar acessar variáveis definidas dentro de uma função fora dela (elas têm escopo local).
        """)
        st.write("---")

    with st.expander("2. Listas, Tuplas, Dicionários e Conjuntos"):
        st.write("""
        Python oferece diversas **estruturas de dados** embutidas, cada uma com suas características e usos específicos, para organizar e armazenar coleções de informações. A escolha da estrutura de dados correta é fundamental para a eficiência e clareza do seu código.

        * **Listas (`list`)**:
            * Coleções **ordenadas** de itens (a ordem de inserção é mantida).
            * São **mutáveis**, ou seja, você pode adicionar, remover, modificar ou reordenar itens após a criação.
            * Permitem itens duplicados e podem conter itens de diferentes tipos de dados.
            * Definidas com colchetes `[]`.
            * **Uso Ideal**: Quando você precisa de uma coleção flexível de itens que pode mudar ao longo do tempo, como uma lista de compras ou resultados de uma query.
        * **Tuplas (`tuple`)**:
            * Coleções **ordenadas** de itens (a ordem de inserção é mantida).
            * São **imutáveis**, o que significa que, uma vez criadas, você não pode alterar seus itens (adicionar, remover ou modificar).
            * Permitem itens duplicados e de diferentes tipos de dados.
            * Definida com parênteses `()`.
            * **Uso Ideal**: Para dados que não devem mudar, como coordenadas geográficas, configurações fixas, ou para retornar múltiplos valores de uma função.
        * **Dicionários (`dict`)**:
            * Coleções **ordenadas** (a partir do Python 3.7+ mantêm a ordem de inserção) de pares **chave-valor**.
            * Cada item é um par `chave: valor`. As **chaves** devem ser únicas e **imutáveis** (geralmente strings, números ou tuplas). Os valores podem ser de qualquer tipo.
            * São **mutáveis**.
            * Definidos com chaves `{}`.
            * **Uso Ideal**: Para representar dados onde você precisa associar um valor a um nome ou identificador único (como um cadastro de usuário, ou configurações de um objeto).
        * **Conjuntos (`set`)**:
            * Coleções **não ordenadas** de itens **únicos**.
            * Automaticamente removem duplicatas.
            * São **mutáveis**.
            * Definidos com chaves `{}`, mas sem pares chave-valor. Para criar um conjunto vazio, use `set()` (pois `{}` cria um dicionário vazio).
            * **Uso Ideal**: Para armazenar uma coleção de itens únicos, testar a presença de um item de forma muito eficiente, ou realizar operações matemáticas de conjuntos (união, interseção, diferença).

        **Acesso a Elementos:**
        * Listas e Tuplas: Usam **índices numéricos** (começando do 0) dentro de colchetes. Ex: `minha_lista[0]`. Índices negativos contam a partir do final (`-1` é o último elemento).
        * Dicionários: Usam as **chaves** dentro de colchetes. Ex: `meu_dicionario['chave']`.
        * Conjuntos: Não possuem ordem nem acesso por índice ou chave. Você apenas verifica a presença de um elemento.
        """)
        st.code("""
# Exemplos detalhados de estruturas de dados

# --- Listas: Flexíveis e comuns ---
frutas = ["maçã", "banana", "laranja", "maçã", "abacaxi"] # Lista com duplicata
print(f"Lista original: {frutas}")
print(f"Primeira fruta (índice 0): {frutas[0]}")
print(f"Última fruta (índice -1): {frutas[-1]}")

frutas.append("uva") # Adiciona um item no final
print(f"Lista após append('uva'): {frutas}")
frutas.insert(1, "kiwi") # Insere 'kiwi' no índice 1 (desloca outros itens)
print(f"Lista após insert(1, 'kiwi'): {frutas}")
frutas.remove("maçã") # Remove a *primeira* ocorrência do valor "maçã"
print(f"Lista após remove('maçã'): {frutas}")
ultima_fruta_removida = frutas.pop() # Remove e retorna o *último* item
print(f"Última fruta removida com pop(): {ultima_fruta_removida}, Lista atualizada: {frutas}")
print(f"Tamanho da lista: {len(frutas)}") # len() retorna o número de elementos

# --- Tuplas: Para dados fixos ---
coordenadas = (10.5, 20.3, 5.0) # Tupla de coordenadas (latitude, longitude, altitude)
print(f"Coordenadas: {coordenadas}")
print(f"Latitude: {coordenadas[0]}, Longitude: {coordenadas[1]}")
# coordenadas[0] = 11.0 # Isso causaria um erro (TypeError)! Tuplas são imutáveis.

# --- Dicionários: Para dados com rótulos (chaves) ---
pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "Rio de Janeiro",
    "profissao": "Engenheiro"
}
print(f"Dicionário original: {pessoa}")
print(f"Nome da pessoa: {pessoa['nome']}") # Acessa o valor associado à chave 'nome'

pessoa["idade"] = 31 # Altera o valor de uma chave existente
pessoa["email"] = "joao.silva@email.com" # Adiciona um novo par chave-valor
print(f"Dicionário atualizado: {pessoa}")

# Verificando se uma chave existe
if "profissao" in pessoa:
    print(f"Profissão: {pessoa['profissao']}")

# Usando .get() para acessar valores (evita KeyError se a chave não existir)
telefone = pessoa.get("telefone", "Não informado") # Se 'telefone' não existe, retorna "Não informado"
print(f"Telefone: {telefone}")

# Percorrendo um dicionário
print("\\nIterando sobre o dicionário:")
for chave, valor in pessoa.items(): # .items() retorna pares chave-valor
    print(f"{chave.capitalize()}: {valor}") # .capitalize() deixa a primeira letra maiúscula

# --- Conjuntos: Para itens únicos ---
numeros_duplicados = [1, 2, 2, 3, 4, 4, 5, 1]
conjunto_numeros = set(numeros_duplicados) # Converte lista para conjunto, removendo duplicatas
print(f"Lista com duplicatas: {numeros_duplicados}")
print(f"Conjunto de números únicos: {conjunto_numeros}")

conjunto_numeros.add(6) # Adiciona um item (se já existir, não faz nada)
print(f"Conjunto após adicionar 6: {conjunto_numeros}")
conjunto_numeros.remove(2) # Remove um item (causa KeyError se o item não estiver presente)
print(f"Conjunto após remover 2: {conjunto_numeros}")

# Testando pertencimento (muito rápido em conjuntos, O(1) em média)
if 3 in conjunto_numeros:
    print("O número 3 está no conjunto.")
if 9 not in conjunto_numeros:
    print("O número 9 NÃO está no conjunto.")

# Operações de conjunto
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"União (set1 | set2): {set1 | set2}")         # Elementos presentes em set1 OU set2
print(f"Interseção (set1 & set2): {set1 & set2}")    # Elementos presentes em set1 E set2
print(f"Diferença (set1 - set2): {set1 - set2}")      # Elementos em set1 MAS NÃO em set2
""")
        st.write("""
        **Melhores Práticas:**
        * Escolha a estrutura de dados mais adequada para o problema. Listas para coleções ordenadas mutáveis, tuplas para dados fixos, dicionários para mapeamentos chave-valor, e conjuntos para coleções de itens únicos.
        * Para dicionários, use `.get(chave, valor_padrao)` para acessar valores se houver chance de a chave não existir, evitando `KeyError`.
        * Aproveite as operações de conjunto para eficientemente lidar com elementos únicos e relações entre coleções.

        **Erro Comum:** `IndexError` ao tentar acessar um índice que não existe em listas/tuplas, ou `KeyError` ao tentar acessar uma chave que não existe em dicionários. Tentar modificar uma tupla.
        """)
        st.write("---")

    with st.expander("3. Manipulação de Strings", expanded=True):
        st.write("""
        Strings são sequências de caracteres e, por serem tão fundamentais em quase todos os programas, Python oferece uma vasta gama de métodos para manipulá-las de forma eficiente. Você pode combinar, dividir, substituir, formatar e muito mais.

        * **Imutabilidade**: Uma propriedade crucial das strings em Python é que elas são **imutáveis**. Isso significa que, uma vez criada, uma string não pode ser alterada. Qualquer operação que "modifique" uma string (como converter para maiúsculas) na verdade retorna uma **nova string**.
        """)
        st.code("""
texto = "Olá, Mundo Python!"

# Métodos comuns de string:
print(f"Original: '{texto}'")
print(f"Maiúsculas: '{texto.upper()}'")
print(f"Minúsculas: '{texto.lower()}'")
print(f"Primeira letra maiúscula: '{texto.capitalize()}'") # Apenas a primeira letra da frase

# Substituição
novo_texto = texto.replace("Python", "Streamlit")
print(f"Substituído: '{novo_texto}'")

# Dividir string (split)
palavras = texto.split(" ") # Divide pelo espaço em branco
print(f"Palavras (split): {palavras}")

# Juntar strings (join)
lista_de_palavras = ["Python", "é", "incrível"]
frase_nova = " ".join(lista_de_palavras) # Junta as palavras com espaço
print(f"Frase juntada: '{frase_nova}'")

# Verificação (startswith, endswith, in)
print(f"Começa com 'Olá'? {texto.startswith('Olá')}")
print(f"Termina com '!'? {texto.endswith('!')}")
print(f"'Mundo' está em texto? {'Mundo' in texto}")

# Remover espaços em branco (strip)
texto_com_espacos = "    Olá, espaço!   "
print(f"Original com espaços: '{texto_com_espacos}'")
print(f"Sem espaços (strip): '{texto_com_espacos.strip()}'")

# Fatiamento (Slicing) - [inicio:fim:passo]
# Lembrar: o 'fim' é exclusivo (não incluído)
print(f"Primeiros 4 caracteres: '{texto[0:4]}'")
print(f"Do 5º ao 10º caracter: '{texto[4:10]}'")
print(f"Do 6º caracter até o final: '{texto[5:]}'")
print(f"Os últimos 5 caracteres: '{texto[-5:]}'")
print(f"Inverter string: '{texto[::-1]}'") # Passo negativo inverte
""")
        st.write("""
        **Melhores Práticas:**
        * Sempre se lembre da **imutabilidade** das strings. Os métodos retornam novas strings.
        * Use `strip()` para limpar entradas de usuário de espaços indesejados.
        * Explore a documentação para descobrir outros métodos úteis (ex: `isdigit()`, `isalpha()`, `count()`).

        **Erro Comum:** Tentar modificar uma string no lugar (ex: `minha_string.upper()` não muda `minha_string`, você precisa `minha_string = minha_string.upper()`).
        """)
        st.write("---")

    with st.expander("4. Classes e Objetos (Programação Orientada a Objetos - POO)"):
        st.write("""
        A **Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código em torno de **objetos**, em vez de apenas funções e lógica. Ela visa modelar entidades do mundo real ou conceitos abstratos, tornando o código mais modular, reutilizável e fácil de manter.

        Os conceitos chave da POO são:
        * **Classe**: É um "molde" ou "planta" para criar objetos. Ela define as características (atributos) e os comportamentos (métodos) que os objetos daquela classe terão. Pense em uma classe `Carro` que define que todo carro tem `cor`, `modelo` e pode `acelerar`.
        * **Objeto (Instância)**: É uma realização concreta de uma classe. Cada carro específico (um Fiat Uno vermelho, um Tesla azul) seria um objeto da classe `Carro`.
        * **Atributos**: São as variáveis que pertencem a uma classe ou objeto, representando suas características (ex: `cor`, `modelo` de um carro).
        * **Métodos**: São as funções que pertencem a uma classe ou objeto, representando seus comportamentos (ex: `acelerar()`, `frear()` de um carro).
        * **`self`**: É o primeiro parâmetro de qualquer método em uma classe Python. Ele referencia a própria instância do objeto, permitindo acessar seus atributos e outros métodos. É uma convenção e é crucial.
        * **`__init__` (Método Construtor)**: Um método especial que é automaticamente chamado quando um novo objeto (instância) da classe é criado. É usado para inicializar os atributos do objeto.

        **Pilares da POO (breve introdução):**
        * **Encapsulamento**: Agrupar dados (atributos) e métodos que operam sobre esses dados dentro de uma única unidade (a classe), controlando o acesso externo.
        * **Herança**: Permite que uma nova classe (subclasse) herde atributos e métodos de uma classe existente (superclasse), promovendo a reutilização de código.
        * **Polimorfismo**: A capacidade de objetos de diferentes classes responderem à mesma mensagem (chamada de método) de maneiras diferentes.
        * **Abstração**: Focar nos aspectos essenciais de um objeto e esconder os detalhes complexos de implementação.

        **Por que usar POO?** Para programas maiores e mais complexos, a POO ajuda a gerenciar a complexidade, promover a reutilização de código e criar sistemas mais flexíveis e fáceis de escalar.
        """)
        st.code("""
# Definindo uma Classe 'Cachorro'
class Cachorro:
    # Método construtor: chamado ao criar um novo objeto Cachorro
    def __init__(self, nome, raca, idade):
        self.nome = nome  # Atributo 'nome'
        self.raca = raca  # Atributo 'raca'
        self.idade = idade # Atributo 'idade'
        print(f"Um novo cachorro chamado {self.nome} foi criado!")

    # Método para o cachorro latir
    def latir(self):
        return f"{self.nome} diz: Au au!"

    # Método para o cachorro envelhecer
    def envelhecer(self):
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos."

# Criando objetos (instâncias) da classe Cachorro
meu_cachorro = Cachorro("Buddy", "Golden Retriever", 3)
outro_cachorro = Cachorro("Luna", "Poodle", 1)

# Acessando atributos dos objetos
print(f"Meu cachorro é um {meu_cachorro.raca} chamado {meu_cachorro.nome}.")
print(f"O outro cachorro é uma {outro_cachorro.raca} de {outro_cachorro.idade} ano(s).")

# Chamando métodos dos objetos
print(meu_cachorro.latir())
print(outro_cachorro.latir())

# Alterando um atributo diretamente
meu_cachorro.idade = 4
print(f"Idade do {meu_cachorro.nome} foi atualizada para {meu_cachorro.idade}.")

# Usando o método para alterar o estado do objeto
print(outro_cachorro.envelhecer())
print(f"Nova idade de {outro_cachorro.nome}: {outro_cachorro.idade}")


# Exemplo de Herança
class Gato(Cachorro): # Gato herda de Cachorro
    def __init__(self, nome, raca, idade, cor_pelo):
        super().__init__(nome, raca, idade) # Chama o construtor da classe pai
        self.cor_pelo = cor_pelo # Atributo específico de Gato

    def miar(self): # Método específico de Gato
        return f"{self.nome} diz: Miau!"

    # Exemplo de Polimorfismo: sobrescrevendo um método da classe pai
    def latir(self):
        return f"{self.nome} (o gato) tenta latir: Meow-au!"

meu_gato = Gato("Whiskers", "Siamês", 2, "Creme")
print(f"Meu gato é um {meu_gato.raca} de {meu_gato.cor_pelo} chamado {meu_gato.nome}.")
print(meu_gato.miar())
print(meu_gato.latir()) # Apesar de herdar latir(), ele usa a versão de Gato
""")
        st.write("""
        **Melhores Práticas:**
        * Nomes de classes começam com letra maiúscula (`CamelCase`).
        * Defina atributos essenciais no construtor `__init__`.
        * Mantenha os métodos com uma única responsabilidade.
        * Use `super().__init__()` ao herdar para inicializar a classe pai.

        **Erro Comum:** Esquecer o `self` como primeiro parâmetro dos métodos de instância, ou tentar acessar atributos de instância sem `self.`.
        """)
        st.write("---")

# --- Função do Módulo Avançado ---
def modulo_avancado():
    st.header("Módulo Avançado: Tópicos Essenciais e Aplicações Reais")
    st.write("Este módulo cobre técnicas avançadas para tornar seus programas mais robustos, eficientes e interativos, além de abordar conceitos cruciais para o desenvolvimento de aplicações.")

    with st.expander("1. Tratamento de Erros (`try`/`except`/`finally`)", expanded=True):
        st.write("""
        Em programação, erros (ou exceções) acontecem. Eles podem ser causados por entradas inválidas do usuário, arquivos que não existem, problemas de rede, etc. Um programa bem construído não "trava" quando um erro ocorre, mas sim **trata** a situação de forma elegante.

        O Python oferece o bloco `try-except-finally` para o tratamento de exceções:
        * **`try`**: O código que *pode* gerar um erro é colocado dentro deste bloco.
        * **`except`**: Se um erro ocorrer no bloco `try`, o Python procura por um bloco `except` que corresponda ao tipo de erro. Se encontrar, o código dentro deste `except` é executado. Você pode ter múltiplos blocos `except` para diferentes tipos de erro, ou um `except` genérico para capturar qualquer erro.
        * **`else`**: (Opcional) O código dentro do `else` é executado **somente** se o bloco `try` for executado com sucesso (sem nenhum erro).
        * **`finally`**: (Opcional) O código dentro do `finally` é **sempre** executado, independentemente de um erro ter ocorrido ou não. É ideal para tarefas de limpeza, como fechar arquivos ou conexões de banco de dados.

        **Por que são importantes?** O tratamento de erros melhora a **robustez** e a **experiência do usuário** do seu programa, evitando que ele crash e fornecendo feedback útil em caso de problemas.
        """)
        st.code("""
# Exemplo 1: Tratamento de divisão por zero
try:
    numero1 = float(st.text_input("Digite o primeiro número (para divisão):", key="num1_div"))
    numero2 = float(st.text_input("Digite o segundo número (para divisão):", key="num2_div"))
    
    # Validação adicional para evitar ValueError se o input for vazio
    if not st.session_state.get("num1_div") or not st.session_state.get("num2_div"):
        st.info("Digite ambos os números para ver o resultado da divisão.")
    else:
        resultado = numero1 / numero2
        st.success(f"Resultado da divisão: {resultado}")
except ValueError:
    st.error("Erro: Por favor, digite apenas números válidos.")
except ZeroDivisionError:
    st.error("Erro: Não é possível dividir por zero!")
except Exception as e: # Captura qualquer outro erro inesperado
    st.error(f"Ocorreu um erro inesperado: {e}")
finally:
    st.info("Operação de divisão finalizada (bloco finally).")

st.write("---")

# Exemplo 2: Tratamento de arquivo não encontrado
st.subheader("Simulação de Leitura de Arquivo")
st.write("Este exemplo simula a leitura de um arquivo. Tente com um nome que não existe, como 'meu_arquivo_inexistente.txt'.")
nome_arquivo = st.text_input("Nome do arquivo para tentar ler (ex: 'dados.txt'):", key="file_name_input")

if st.button("Tentar Ler Arquivo", key="read_file_btn"):
    if not nome_arquivo:
        st.warning("Por favor, digite um nome de arquivo.")
    else:
        try:
            with open(nome_arquivo, 'r') as f: # Tenta abrir o arquivo no modo leitura
                conteudo = f.read()
                st.code(f"Conteúdo de '{nome_arquivo}':\\n{conteudo}")
        except FileNotFoundError:
            st.error(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Certifique-se de que ele existe e o caminho está correto.")
        except IOError: # Erros de entrada/saída mais genéricos
            st.error(f"Erro de I/O ao tentar ler '{nome_arquivo}'.")
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")
        finally:
            st.info("Tentativa de leitura de arquivo concluída.")

# Para testar o FileNotFoundError, você pode criar um arquivo temporário:
# with open("dados.txt", "w") as f:
#    f.write("Linha 1\\nLinha 2")
# E depois apagar para testar o erro.
""")
        st.write("""
        **Melhores Práticas:**
        * Seja específico nos blocos `except`: capture os tipos de exceção que você espera (ex: `ValueError`, `FileNotFoundError`) para lidar com eles de forma adequada.
        * Evite um `except` genérico (`except Exception as e:`) a menos que você queira pegar *todos* os erros e registrar/exibir a mensagem para depuração.
        * Use o bloco `finally` para garantir que recursos (arquivos, conexões) sejam fechados ou liberados, mesmo que um erro ocorra.

        **Erro Comum:** Não tratar erros, fazendo com que o programa "quebre" (crash) para o usuário, ou usar um `except` muito genérico que esconde problemas reais de lógica.
        """)
        st.write("---")

    with st.expander("2. Manipulação de Arquivos"):
        st.write("""
        Interagir com arquivos é uma funcionalidade fundamental para a maioria dos programas, permitindo que eles salvem dados, carreguem configurações ou processem informações persistentes. Em Python, a manipulação de arquivos é feita principalmente com a função `open()`.

        **Modos de Abertura:**
        * `'r'` (read): Abre o arquivo para leitura. É o modo padrão. O arquivo deve existir, caso contrário, `FileNotFoundError` será levantado.
        * `'w'` (write): Abre o arquivo para escrita. Se o arquivo não existir, um novo é criado. **Cuidado**: Se o arquivo já existir, **seu conteúdo será TRUNCADO (apagado)!**
        * `'a'` (append): Abre o arquivo para escrita no final (apêndice). Se o arquivo não existir, um novo é criado. Se existir, o novo conteúdo é adicionado ao final do arquivo, sem apagar o que já está lá.
        * `'x'` (exclusive creation): Cria um novo arquivo para escrita. Se o arquivo já existir, levanta um `FileExistsError`.
        * `'t'` (text): Modo texto (padrão). Usado para lidar com strings.
        * `'b'` (binary): Modo binário. Usado para lidar com bytes (imagens, vídeos, executáveis).

        **Context Manager (`with open(...) as ...`)**:
        É a forma **recomendada** de manipular arquivos em Python. Ele garante que o arquivo seja automaticamente fechado, mesmo que ocorra um erro durante a operação, evitando vazamentos de recursos.

        **Leitura:**
        * `f.read()`: Lê todo o conteúdo do arquivo como uma única string.
        * `f.readline()`: Lê uma única linha do arquivo.
        * `f.readlines()`: Lê todas as linhas do arquivo em uma lista de strings.
        * Iterar sobre o objeto arquivo (`for linha in f:`): A forma mais eficiente de ler arquivos linha por linha, especialmente para arquivos grandes.

        **Escrita:**
        * `f.write(string)`: Escreve uma string no arquivo. Não adiciona quebras de linha automaticamente.
        * `f.writelines(lista_de_strings)`: Escreve uma lista de strings no arquivo. Também não adiciona quebras de linha automaticamente, então inclua `\\n` nas suas strings, se desejar.

        **Por que são importantes?** A manipulação de arquivos é fundamental para persistir dados, ler configurações, gerar relatórios e interagir com o sistema de arquivos do computador.
        """)
        st.code("""
import os # Módulo para interagir com o sistema operacional (ex: verificar se arquivo existe)

# --- Exemplo de Escrita em Arquivo (Modo 'w') ---
st.subheader("Escrevendo em um Arquivo (Modo 'w')")
st.write("Isso irá criar ou sobrescrever o arquivo 'exemplo_escrita.txt'.")
conteudo_para_escrever = st.text_area("Conteúdo para o arquivo 'exemplo_escrita.txt':", 
                                        "Linha 1: Olá Python!\nLinha 2: Streamlit é legal.", 
                                        key="write_content")
if st.button("Escrever no Arquivo (Sobrescrever)", key="write_file_btn"):
    try:
        with open("exemplo_escrita.txt", "w") as f:
            f.write(conteudo_para_escrever)
        st.success("Conteúdo gravado com sucesso em 'exemplo_escrita.txt'!")
    except IOError as e:
        st.error(f"Erro de I/O ao escrever: {e}")

# --- Exemplo de Leitura de Arquivo (Modo 'r') ---
st.subheader("Lendo de um Arquivo (Modo 'r')")
st.write("Tente ler o arquivo que você acabou de criar ou um que já exista.")
nome_arquivo_leitura = st.text_input("Nome do arquivo para ler:", "exemplo_escrita.txt", key="read_file_name")

if st.button("Ler Arquivo", key="read_file_btn_2"):
    if not os.path.exists(nome_arquivo_leitura):
        st.warning(f"O arquivo '{nome_arquivo_leitura}' não existe. Crie-o primeiro ou digite um nome válido.")
    else:
        try:
            with open(nome_arquivo_leitura, "r") as f:
                conteudo_lido = f.read()
                st.info(f"Conteúdo de '{nome_arquivo_leitura}':")
                st.code(conteudo_lido)
        except Exception as e:
            st.error(f"Ocorreu um erro ao ler o arquivo: {e}")

# --- Exemplo de Adicionar Conteúdo (Modo 'a') ---
st.subheader("Adicionando Conteúdo a um Arquivo (Modo 'a')")
st.write("Isso adicionará uma nova linha ao arquivo 'exemplo_escrita.txt'.")
conteudo_para_adicionar = st.text_input("Conteúdo para adicionar:", "Nova linha adicionada em " + time.ctime(), key="append_content")
if st.button("Adicionar ao Arquivo", key="append_file_btn"):
    try:
        with open("exemplo_escrita.txt", "a") as f:
            f.write("\\n" + conteudo_para_adicionar) # Adiciona uma quebra de linha antes
        st.success("Conteúdo adicionado com sucesso a 'exemplo_escrita.txt'!")
    except IOError as e:
        st.error(f"Erro de I/O ao adicionar: {e}")

st.write("---")
""")
        st.write("""
        **Melhores Práticas:**
        * Sempre use o `with open(...)` para garantir que os arquivos sejam fechados corretamente.
        * Escolha o modo de abertura (`'r'`, `'w'`, `'a'`) com cuidado, especialmente `'w'` que pode apagar dados.
        * Lembre-se que `write()` não adiciona quebras de linha (`\\n`). Adicione-as manualmente se precisar.
        * Para arquivos grandes, leia linha por linha (`for linha in f:`) em vez de carregar tudo com `f.read()` para economizar memória.

        **Erro Comum:** `FileNotFoundError` ao tentar ler um arquivo que não existe, ou sobrescrever acidentalmente um arquivo importante usando o modo `'w'`.
        """)
        st.write("---")

    st.subheader("Exercício Interativo: Contador de Palavras")
    st.write("Cole um texto abaixo e descubra quantas palavras únicas ele contém. Este exercício usa manipulação de strings, conjuntos e tratamento de erros.")
    
    texto_para_contar = st.text_area("Cole seu texto aqui:", key="text_counter_input")
    
    if st.button("Contar Palavras Únicas", key="count_words_btn"):
        if not texto_para_contar:
            st.warning("Por favor, cole algum texto para contar as palavras.")
        else:
            try:
                # Converte para minúsculas e remove pontuações para melhor contagem
                texto_limpo = texto_para_contar.lower()
                
                # Poderíamos usar uma expressão regular, mas para simplificar:
                # Remove caracteres não alfanuméricos e substitui por espaço
                for char in '.,;!?:()"':
                    texto_limpo = texto_limpo.replace(char, ' ')
                
                palavras = texto_limpo.split() # Divide em palavras usando espaços
                
                # Usa um conjunto para obter palavras únicas
                palavras_unicas = set(palavras)
                
                st.success(f"Seu texto contém **{len(palavras_unicas)}** palavras únicas.")
                st.write("As palavras únicas são:", sorted(list(palavras_unicas))) # Exibe ordenado
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar o texto: {e}")
    st.write("---")

# --- Estrutura Principal do Aplicativo Streamlit ---
if __name__ == "__main__":
    st.title("🐍 Curso de Python Interativo")
    st.markdown("Bem-vindo(a) ao curso aprofundado de Python! Selecione um módulo no menu lateral para começar ou continuar sua jornada.")

    st.sidebar.title("📚 Módulos do Curso")
    modulo_selecionado = st.sidebar.radio(
        "Navegue pelos tópicos:",
        ("Introdução", "Módulo Básico", "Módulo Intermediário", "Módulo Avançado"),
        key="main_navigation"
    )

    if modulo_selecionado == "Introdução":
        st.write("Use o menu ao lado para explorar os diferentes módulos do curso. Cada módulo contém explicações, exemplos de código e exercícios interativos para praticar seus conhecimentos.")
        st.image("https://www.python.org/static/community_logos/python-powered-h-140x182.png", width=200) # Exemplo de imagem
        st.write("Desenvolvido com ❤️ e Streamlit.")
    elif modulo_selecionado == "Módulo Básico":
        modulo_basico()
    elif modulo_selecionado == "Módulo Intermediário":
        modulo_intermediario()
    elif modulo_selecionado == "Módulo Avançado":
        modulo_avancado()

    # Mensagem de depuração no terminal (visível apenas onde você rodou 'streamlit run')
    print(f"Módulo '{modulo_selecionado}' selecionado e carregado.")
