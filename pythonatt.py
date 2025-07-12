import streamlit as st
import random # Para o quiz

def modulo_basico():
    st.header("Módulo Básico: Primeiros Passos em Python")
    st.write("Este módulo cobre os fundamentos essenciais da programação em Python, preparando você para construir lógicas simples e entender como o Python funciona.")

    st.subheader("1. Variáveis e Tipos de Dados")
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

    st.subheader("2. Operadores Aritméticos e Lógicos")
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

    st.subheader("3. Entrada de Dados (`input()`) e Formatação de Strings (f-strings)")
    st.write("""
    Para que seus programas sejam interativos, muitas vezes você precisará obter informações do usuário. A função `input()` faz exatamente isso: ela pausa o programa, exibe uma mensagem no console e espera que o usuário digite algo, retornando essa entrada sempre como uma **string**. Mesmo que o usuário digite um número, `input()` o lerá como texto, e você precisará convertê-lo (com `int()` ou `float()`) se quiser realizar operações numéricas.

    Quando você quer exibir informações combinando texto estático e valores de variáveis de forma elegante e eficiente, as **f-strings** (formatted string literals) são a melhor ferramenta em Python 3.6+. Elas permitem que você incorpore expressões Python (variáveis, chamadas de função simples, etc.) diretamente dentro de strings, prefixando a string com um `f` ou `F`. Isso as torna muito mais legíveis e concisas do que métodos de formatação mais antigos como `%` ou `.format()`.
    """)
    st.code("""
# Usando input() para obter dados do usuário
# Ao rodar este código localmente, você verá o prompt no terminal onde o streamlit foi iniciado.
# No navegador, esta entrada é simulada pelo Streamlit (veja o exemplo do exercício).
# Observação: 'input()' só funciona no console, não em interfaces web como Streamlit diretamente.
# nome_usuario = input("Por favor, digite seu nome: ")
# print(f"Olá, {nome_usuario}! Seja bem-vindo(a).")

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
# Saída: |Ana       | 9.5 |
""")
    st.write("""
    **Melhores Práticas:**
    * Sempre use f-strings para formatação de strings em código moderno Python.
    * Quando usar `input()`, sempre avise o usuário o tipo de dado esperado.
    * Após coletar entrada com `input()`, use `int()`, `float()`, etc., para converter para o tipo numérico adequado antes de realizar operações matemáticas.

    **Erro Comum:** Esquecer de converter a entrada do `input()` para um tipo numérico ao tentar fazer cálculos, resultando em `TypeError` (e.g., `ValueError` se a conversão falhar, como `int("abc")`).
    """)
    st.write("---")

    st.subheader("4. Estruturas Condicionais (`if`/`elif`/`else`)")
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

    st.subheader("5. Estruturas de Repetição (`for`/`while`)")
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

# Loop 'while': Senha com tentativas limitadas
senhas_corretas = 0
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas: # Repete enquanto o contador for menor que o máximo
    print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")
    # No Streamlit, você usaria st.text_input para coletar a entrada
    # entrada_senha = st.text_input("Digite a senha:", key=f"senha_{tentativas}")
    entrada_senha = "segredo123" if tentativas == 0 else "errada" # Simulação de entrada
    st.write(f"Simulando entrada de senha: {entrada_senha}") # Para mostrar no Streamlit

    if entrada_senha == "segredo123":
        print("Senha correta!")
        senhas_corretas += 1 # Incrementa o contador de senhas corretas
        if senhas_corretas == 1: # Exemplo de 'break'
            print("Parabéns, você acertou a senha!")
            break # Sai do loop imediatamente
    else:
        print("Senha incorreta. Tente novamente.")
    tentativas += 1 # Garante que o loop um dia termine

print("Tentativas encerradas.")

# Exemplo de 'continue': Pulando números pares
print("\\nNúmeros ímpares de 1 a 10:")
for numero in range(1, 11):
    if numero % 2 == 0: # Se o número for par...
        continue # ...pula para a próxima iteração do loop, sem executar o print abaixo
    print(numero)
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

def modulo_intermediario():
    st.header("Módulo Intermediário: Aprofundando em Python")
    st.write("Este módulo aprofunda seu conhecimento em Python, apresentando conceitos que permitem organizar e otimizar seu código, além de lidar com dados de forma mais eficiente.")

    st.subheader("1. Funções")
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

    st.subheader("2. Listas, Tuplas, Dicionários e Conjuntos")
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
print(f"Diferença (set1 - set2): {set1 - set2}")     # Elementos em set1 MAS NÃO em set2
""")
    st.write("""
    **Melhores Práticas:**
    * Escolha a estrutura de dados mais adequada para o problema. Listas para coleções ordenadas mutáveis, tuplas para dados fixos, dicionários para mapeamentos chave-valor, e conjuntos para coleções de itens únicos.
    * Para dicionários, use `.get(chave, valor_padrao)` para acessar valores se houver chance de a chave não existir, evitando `KeyError`.
    * Aproveite as operações de conjunto para eficientemente lidar com elementos únicos e relações entre coleções.

    **Erro Comum:** `IndexError` ao tentar acessar um índice que não existe em listas/tuplas, ou `KeyError` ao tentar acessar uma chave que não existe em dicionários. Tentar modificar uma tupla.
    """)
    st.write("---")

    st.subheader("3. Manipulação de Strings")
    st.write("""
    Strings são sequências de caracteres e, por serem tão fundamentais em quase todos os programas, Python oferece uma vasta gama de métodos para manipulá-las de forma eficiente. Você pode combinar, dividir, substituir, formatar e muito mais.

    * **Imutabilidade**: Uma propriedade crucial das strings em Python é que elas são **imutáveis**. Isso significa que, uma vez que uma string é criada, seu conteúdo não pode ser alterado no local. Quando você "modifica" uma string (por exemplo, convertendo para maiúsculas ou substituindo uma parte), na verdade, você está criando uma *nova* string com as alterações, e a variável original passa a referenciar essa nova string (se você a reatribuir). A string original permanece intacta na memória até que o coletor de lixo a remova.
    * **Métodos Comuns**: Python fornece dezenas de métodos embutidos para strings que simplificam tarefas comuns.
        * `len(string)`: (Função global) Retorna o comprimento (número de caracteres) da string.
        * `.lower()`, `.upper()`: Converte a string para minúsculas ou maiúsculas, respectivamente.
        * `.strip()`, `.lstrip()`, `.rstrip()`: Remove espaços em branco (ou caracteres especificados) do início e do fim, apenas do início, ou apenas do fim da string.
        * `.replace(old, new)`: Substitui *todas* as ocorrências de uma substring por outra.
        * `.split(delimiter)`: Divide a string em uma **lista** de substrings com base em um delimitador especificado. Se nenhum delimitador for fornecido, divide por qualquer sequência de espaços em branco.
        * `.join(list_of_strings)`: O inverso de `split()`. Une uma lista de strings em uma única string, usando a string na qual o método `.join()` é chamado como separador entre os elementos.
        * `.startswith(prefix)`, `.endswith(suffix)`: Verifica se a string começa/termina com um determinado prefixo/sufixo, retornando `True` ou `False`.
        * `.find(substring)`: Retorna o índice da primeira ocorrência da substring, ou `-1` se a substring não for encontrada.
        * `.count(substring)`: Retorna o número de ocorrências de uma substring dentro da string.
        * `.isdigit()`, `.isalpha()`, `.isalnum()`, `.isspace()`: Métodos para verificar o conteúdo da string (contém apenas dígitos, apenas letras, apenas alfanuméricos, apenas espaços, etc.).

    **Por que são importantes?** A manipulação de texto é uma parte gigantesca da programação, desde o processamento de entrada do usuário até a análise de dados de arquivos, web scraping e geração de relatórios.
    """)
    st.code("""
texto_original = "   Python é PODEROSO e flexível!   "

print(f"Original: '{texto_original}'")
print(f"Tamanho (com espaços): {len(texto_original)}")

# Convertendo para minúsculas e maiúsculas
print(f"Minúscula: '{texto_original.lower()}'")
print(f"Maiúscula: '{texto_original.upper()}'")

# Removendo espaços em branco extras do início e fim
texto_limpo = texto_original.strip()
print(f"Sem espaços extras (strip): '{texto_limpo}'")
print(f"Tamanho (sem espaços): {len(texto_limpo)}")

# Substituindo partes da string - cria uma NOVA string
texto_substituido = texto_limpo.replace("PODEROSO", "MUITO ÚTIL")
print(f"Substituído: '{texto_substituido}'")
print(f"Original ainda é: '{texto_original}'") # Demonstrando imutabilidade

# Dividindo a string em uma lista de palavras
palavras = texto_limpo.split(" ") # Divide pelo espaço em branco
print(f"Palavras (lista): {palavras}")

# Unindo uma lista de strings em uma única string
nova_frase = "-".join(palavras) # Usa "-" como separador
print(f"Unindo com hífens: {nova_frase}")

# Verificando início e fim de uma string
print(f"Começa com 'Python'? {texto_limpo.startswith('Python')}")
print(f"Termina com 'flexível!'? {texto_limpo.endswith('flexível!')}")

# Encontrando a primeira ocorrência e contando ocorrências
print(f"Posição de 'PODEROSO': {texto_limpo.find('PODEROSO')}") # Retorna índice 9
print(f"Contagem de 'o' (case-insensitive): {texto_limpo.lower().count('o')}") # Converte para minúscula antes de contar

# Checando o tipo de conteúdo
string_numerica = "12345"
print(f"'{string_numerica}' é dígito? {string_numerica.isdigit()}") # True
string_alfabetica = "Python"
print(f"'{string_alfabetica}' é alfabética? {string_alfabetica.isalpha()}") # True
""")
    st.write("""
    **Melhores Práticas:**
    * Lembre-se da imutabilidade das strings: se você precisa de uma versão modificada, armazene o resultado do método em uma nova variável.
    * Use `strip()` ao lidar com entradas do usuário para remover espaços em branco indesejados.
    * Para validações simples de formato, os métodos `.is*()` são muito úteis.
    * Ao concatenar muitas strings, prefira `"".join(lista_de_strings)` em vez de repetidas operações `+`, pois `join` é muito mais eficiente.

    **Erro Comum:** Tentar modificar uma string no local, como `minha_string[0] = 'X'`, o que resultaria em um `TypeError`.
    """)
    st.write("---")

    st.subheader("4. Tratamento de Erros (`try`/`except`/`finally`)")
    st.write("""
    Quando seu código encontra um problema que o impede de continuar a execução normalmente, isso é chamado de **exceção** (ou erro). Exceções não tratadas fazem seu programa "quebrar" e parar. O **tratamento de erros** é crucial para criar programas robustos e "à prova de balas" que não travem inesperadamente diante de entradas inválidas, problemas de rede, arquivos ausentes, ou outras situações imprevistas.

    O bloco `try-except` permite que você "tente" executar um código que pode falhar, e se uma exceção ocorrer, "capture-a" e lide com ela de forma controlada, permitindo que o programa continue ou forneça feedback útil ao usuário.

    * **`try`**: Contém o código que *pode* gerar uma exceção. É o bloco onde você coloca as operações "arriscadas".
    * **`except ExceptionType as e`**: Captura um tipo específico de exceção. Se uma exceção do tipo `ExceptionType` (ou uma de suas subclasses) ocorrer no bloco `try`, o código dentro do `except` será executado. Você pode ter múltiplos `except` para lidar com diferentes tipos de erros de maneiras distintas. O `as e` é opcional e permite que você acesse o objeto da exceção, que muitas vezes contém uma mensagem de erro útil.
    * **`else` (opcional)**: Opcionalmente, pode-se usar um bloco `else` que é executado *apenas* se o código no `try` for executado **sem gerar nenhuma exceção**. É útil para colocar o código que só deve ser executado se o `try` for bem-sucedido.
    * **`finally` (opcional)**: Este bloco é **sempre** executado, ocorrendo uma exceção ou não. É ideal para tarefas de limpeza, como fechar arquivos abertos, liberar recursos de rede ou conexões de banco de dados, garantindo que essas operações importantes sempre aconteçam.

    **Por que são importantes?** O tratamento de erros melhora a resiliência do seu programa, a experiência do usuário (evitando que o programa trave), e ajuda na depuração, direcionando você para a causa raiz do problema.
    """)
    st.code("""
# Exemplo 1: Divisão por zero e tipos incompatíveis
st.write("### Exemplo 1: Tratamento de divisão por zero e tipo")
try:
    numerador = 10
    denominador = 0 # Isso causará um ZeroDivisionError
    # denominador = "abc" # Descomente para testar TypeError

    resultado = numerador / denominador
    print(f"Resultado da divisão: {resultado}") # Esta linha não será alcançada se houver erro
except ZeroDivisionError: # Captura apenas o erro de divisão por zero
    print("Erro: Não é possível dividir por zero!")
except TypeError: # Captura erro se os tipos forem incompatíveis (ex: '10' / 2)
    print("Erro: Tipos de dados incompatíveis para a operação. Verifique se os operandos são números.")
except Exception as e: # Captura qualquer outra exceção não especificada anteriormente
    print(f"Ocorreu um erro inesperado: {e}") # 'e' contém a mensagem de erro da exceção
finally:
    print("Este bloco 'finally' sempre será executado, com ou sem erro.")

print("\\n---")

# Exemplo 2: Conversão de tipo com else (sucesso vs. falha)
st.write("### Exemplo 2: Conversão de tipo com 'else'")
entrada_usuario = "123"
# entrada_usuario = "texto" # Descomente para testar o ValueError

try:
    numero = int(entrada_usuario) # Tenta converter a string para inteiro
except ValueError: # Se a conversão falhar (ex: "abc" para int)
    print(f"Erro: '{entrada_usuario}' não pode ser convertido para um número inteiro válido.")
else: # Este bloco é executado SOMENTE se NENHUM erro ocorrer no 'try'
    print(f"Número convertido com sucesso: {numero}")
    print(f"Tipo do número: {type(numero)}")
finally:
    print("Fim da tentativa de conversão.")

print("\\n---")

# Exemplo 3: Acessando um índice fora dos limites de uma lista
st.write("### Exemplo 3: Acessando lista com IndexError")
minha_lista = [10, 20, 30]
try:
    # print(minha_lista[1]) # Acesso válido
    print(minha_lista[5]) # Tentando acessar um índice que não existe
except IndexError:
    print("Erro: Índice da lista fora dos limites! Verifique o tamanho da lista.")
except Exception as e:
    print(f"Ocorreu um erro geral: {e}")
""")
    st.write("""
    **Melhores Práticas:**
    * Seja específico nos seus `except` blocos. Capture apenas as exceções que você sabe como tratar. Um `except Exception` genérico deve ser usado com cautela, geralmente no final da cadeia de `except`s.
    * Use o bloco `else` para código que só deve ser executado em caso de sucesso do `try`.
    * Use o bloco `finally` para limpeza de recursos, garantindo que eles sejam liberados mesmo que um erro ocorra.
    * Não use tratamento de erros para controle de fluxo normal (ou seja, não force um erro para controlar a lógica do programa). Prefira `if/else` quando possível.

    **Erro Comum:** Capturar `Exception` de forma genérica e assim "engolir" erros inesperados que deveriam ser investigados, tornando a depuração mais difícil.
    """)
    st.write("---")

    st.subheader("Exercício: Calculadora Simples com Tratamento de Erros Avançado")
    st.write("Crie sua própria calculadora! Digite dois números e uma operação (+, -, *, /). O programa lidará elegantemente com entradas inválidas (não numéricas) e o caso especial de divisão por zero.")
    num1_str = st.text_input("Primeiro número:", key="ex_calc_num1")
    num2_str = st.text_input("Segundo número:", key="ex_calc_num2")
    operacao = st.text_input("Operação (+, -, *, /):", key="ex_calc_op")

    if st.button("Calcular", key="btn_calcular"):
        try:
            # Tenta converter as entradas para float. Se falhar, um ValueError será levantado.
            num1 = float(num1_str)
            num2 = float(num2_str)

            resultado = None # Inicializa resultado para garantir que sempre tenha um valor
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    # Levantando uma exceção personalizada para ser capturada pelo 'except ZeroDivisionError'
                    raise ZeroDivisionError("Não é possível dividir por zero! Por favor, insira um divisor diferente de zero.")
                resultado = num1 / num2
            else:
                st.warning("Operação inválida. Por favor, use '+', '-', '*', ou '/'.")
                # Não definimos resultado aqui para não exibir uma mensagem de sucesso inválida
                
            if resultado is not None: # Verifica se a operação foi bem-sucedida e resultado foi atribuído
                st.success(f"Resultado: {resultado}")

        except ValueError:
            st.error("Erro: Por favor, insira números válidos para os operandos.")
        except ZeroDivisionError as e: # 'e' contém a mensagem personalizada que levantamos
            st.error(f"Erro de cálculo: {e}")
        except Exception as e: # Captura qualquer outro erro inesperado
            st.error(f"Ocorreu um erro inesperado durante o cálculo: {e}")
        finally:
            st.info("Cálculo encerrado. Tente novamente com outros valores.")

    st.write("---")

def modulo_avancado():
    st.header("Módulo Avançado: Tópicos Complexos em Python")
    st.write("Este módulo explora conceitos mais avançados e poderosos de Python, que são fundamentais para construir aplicações mais complexas, eficientes e bem estruturadas.")

    st.subheader("1. Programação Orientada a Objetos (POO)")
    st.write("""
    A **Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código em torno de "**objetos**" em vez de funções e lógica procedimental. Pense nos objetos como "entidades" do mundo real (ou conceitos abstratos) que possuem características (atributos) e comportamentos (métodos). A POO promove a modelagem do mundo real em seu código, tornando-o mais intuitivo, organizado, reutilizável e fácil de manter.

    Objetos são instâncias de **classes**, que são como "plantas", "moldes" ou "fábricas" para criar esses objetos. Uma classe define a estrutura e o comportamento que seus objetos terão.

    Os pilares da POO são:
    * **Classe**: Um modelo ou *blueprint* para criar objetos. Define um conjunto de atributos (dados) e métodos (funções que operam nesses dados) que todos os objetos dessa classe terão.
    * **Objeto (Instância)**: Uma ocorrência concreta de uma classe. Cada objeto é uma entidade independente com seus próprios valores para os atributos, mas compartilha os mesmos métodos definidos na classe.
    * **Atributos**: Variáveis que pertencem a uma classe ou objeto, representando suas características ou estado (ex: nome de um cachorro, cor de um carro).
    * **Métodos**: Funções que pertencem a uma classe ou objeto, representando seus comportamentos ou ações que podem ser realizadas (ex: latir para um cachorro, acelerar um carro).
    * **`self`**: O primeiro parâmetro de um método de instância, uma convenção em Python que se refere à própria instância do objeto que está chamando o método. É através de `self` que você acessa os atributos e outros métodos do objeto.
    * **`__init__` (Método Construtor)**: Um método especial (com dois underscores antes e depois) que é automaticamente chamado quando um novo objeto é criado a partir da classe. É usado para inicializar os atributos do objeto, recebendo os valores iniciais como parâmetros.
    * **Herança**: Permite que uma nova classe (chamada **subclasse** ou **classe filha**) herde atributos e métodos de uma classe existente (chamada **superclasse** ou **classe pai**). Isso promove a reutilização de código e estabelece uma relação "é um tipo de" (ex: um `CachorroGuia` *é um tipo de* `Cachorro`).
    * **Encapsulamento**: A prática de agrupar dados (atributos) e métodos que operam nesses dados dentro de uma unidade (a classe), e restringir o acesso direto a alguns dos componentes do objeto. Em Python, o encapsulamento é mais por convenção (prefixando atributos com um underscore `_` para indicar que são "protegidos" ou dois underscores `__` para "privados" - embora não sejam verdadeiramente privados como em outras linguagens). O objetivo é proteger a integridade dos dados, controlando como eles são acessados e modificados através dos métodos da classe.
    * **Polimorfismo**: Significa "muitas formas". Refere-se à capacidade de objetos de diferentes classes de responder ao mesmo método de maneira diferente. Por exemplo, se você tem uma classe `Animal` e subclasses `Cachorro` e `Gato`, ambos podem ter um método `fazer_som()`, mas o `Cachorro` latiria e o `Gato` miaria. Isso permite que você escreva código mais genérico e flexível.

    POO ajuda a modelar problemas do mundo real de forma mais intuitiva e a criar código mais organizado, manutenível e escalável.
    """)
    st.code("""
# Definindo uma Classe Simples: Cachorro
class Cachorro:
    # Atributo de classe (compartilhado por todas as instâncias da classe)
    especie = "Canis familiaris"

    # Método construtor: __init__ é chamado automaticamente ao criar um novo objeto
    # 'self' se refere à instância do objeto que está sendo criada/inicializada
    def __init__(self, nome, raca, idade_aprox):
        self.nome = nome # Atributos de instância (únicos para cada objeto)
        self.raca = raca
        self.idade_aprox = idade_aprox
        self.esta_latindo = False # Atributo padrão, pode ser alterado por métodos

    # Métodos: comportamentos do Cachorro
    def latir(self):
        if not self.esta_latindo:
            self.esta_latindo = True
            return f"{self.nome} ({self.raca}) está latindo: Au Au!"
        else:
            return f"{self.nome} já está latindo."

    def parar_de_latir(self):
        if self.esta_latindo:
            self.esta_latindo = False
            return f"{self.nome} parou de latir."
        else:
            return f"{self.nome} não estava latindo para parar."

    # Método para exibir informações, usando os atributos do próprio objeto (self)
    def exibir_info(self):
        return f"Nome: {self.nome}, Raça: {self.raca}, Idade: {self.idade_aprox} anos, Espécie: {Cachorro.especie}."

# Criando objetos (instâncias da classe Cachorro)
meu_cachorro = Cachorro("Buddy", "Labrador", 5)
outro_cachorro = Cachorro("Luna", "Poodle", 2)

st.write("--- Criando e interagindo com objetos ---")
st.write(meu_cachorro.exibir_info()) # Chamando um método no objeto meu_cachorro
st.write(meu_cachorro.latir())
st.write(meu_cachorro.latir()) # Tenta latir de novo, verifica o estado 'esta_latindo'
st.write(meu_cachorro.parar_de_latir())

st.write(outro_cachorro.exibir_info())
st.write(outro_cachorro.latir())
st.write(f"A raça de Buddy é: {meu_cachorro.raca}") # Acessando um atributo diretamente

# Herança: Criando uma subclasse CachorroGuia que herda de Cachorro
class CachorroGuia(Cachorro): # CachorroGuia herda de Cachorro
    # Construtor da subclasse
    def __init__(self, nome, raca, idade_aprox, licenca):
        # Chama o construtor da classe pai (Cachorro) para inicializar seus atributos
        super().__init__(nome, raca, idade_aprox)
        self.licenca = licenca # Atributo adicional específico de CachorroGuia
        self.esta_guiando = False

    # Novo método específico de CachorroGuia
    def guiar(self):
        if not self.esta_guiando:
            self.esta_guiando = True
            return f"{self.nome} está guiando com sua licença {self.licenca}."
        else:
            return f"{self.nome} já está em serviço."

    # Polimorfismo: Sobrescrevendo (Override) um método da classe pai
    # CachorroGuia tem sua própria versão do método latir()
    def latir(self):
        # Diferente do Cachorro normal, o CachorroGuia late de forma mais específica
        return f"{self.nome} (Cão guia) está dando um latido suave para chamar atenção."

st.write("--- Utilizando Herança e Polimorfismo ---")
rex = CachorroGuia("Rex", "Pastor Alemão", 7, "A123-GUIA")
st.write(rex.exibir_info()) # Método herdado da classe Cachorro
st.write(rex.guiar()) # Método específico de CachorroGuia
st.write(rex.latir()) # Método sobrescrito (polimorfismo em ação!)

# Exemplo de "encapsulamento" por convenção em Python
class ContaBancaria:
    def __init__(self, saldo_inicial):
        # Atributo "privado" por convenção (não deve ser acessado diretamente de fora)
        self.__saldo = saldo_inicial # __ indica um atributo "name mangling" para "quase privado"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}"
        return "Valor de depósito inválido."

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}"
        return "Saldo insuficiente ou valor de saque inválido."

    def get_saldo(self): # Método para acessar o saldo de forma controlada
        return f"Saldo atual: R${self.__saldo:.2f}"

st.write("--- Encapsulamento ---")
minha_conta = ContaBancaria(1000)
st.write(minha_conta.get_saldo())
st.write(minha_conta.depositar(200))
st.write(minha_conta.sacar(1500)) # Tenta sacar mais do que tem
st.write(minha_conta.sacar(50))
# st.write(minha_conta.__saldo) # Isso causaria um AttributeError (name mangling em ação)
""")
    st.write("""
    **Melhores Práticas:**
    * Modelar suas classes para refletir as entidades e seus relacionamentos no seu problema.
    * Siga o princípio da Responsabilidade Única também para classes: cada classe deve ter uma única responsabilidade clara.
    * Use herança quando houver uma relação "é um tipo de" (ex: `Carro` é um tipo de `Veiculo`). Prefira composição ("tem um") em vez de herança quando apropriado.
    * Utilize métodos para interagir com os atributos do objeto, em vez de acessar atributos diretamente, para garantir o encapsulamento e a validade dos dados.

    **Erro Comum:** `AttributeError` ao tentar acessar um atributo ou método que não existe no objeto/classe, ou confundir atributos de classe com atributos de instância.
    """)
    st.write("---")

    st.subheader("2. Manipulação de Arquivos")
    st.write("""
    Trabalhar com arquivos é uma habilidade essencial para qualquer programador, permitindo que seu programa leia dados de arquivos externos (como arquivos de configuração, logs, ou dados de texto) ou salve informações de forma persistente (para que os dados não se percam quando o programa é encerrado).

    O processo básico de manipulação de arquivos envolve:
    1.  **Abrir o arquivo**: Usando a função embutida `open()`, que retorna um objeto arquivo (também conhecido como "file handle"). Você precisa especificar o nome (ou caminho) do arquivo e o **modo** de abertura.
    2.  **Operar no arquivo**: Realizar operações de leitura ou escrita usando métodos do objeto arquivo.
    3.  **Fechar o arquivo**: Usando o método `.close()` no objeto arquivo. **Este passo é crucial** para liberar os recursos do sistema associados ao arquivo e garantir que todas as alterações gravadas em buffer sejam realmente salvas no disco.

    **Modos de Abertura Comuns:**
    * `'r'` (read): Modo de leitura (padrão). O arquivo deve existir. Se não existir, um `FileNotFoundError` será levantado. O ponteiro de leitura começa no início do arquivo.
    * `'w'` (write): Modo de escrita. **Cria um novo arquivo se ele não existir, ou TRUNCA (apaga todo o conteúdo) um arquivo existente.** O ponteiro de escrita começa no início. Use com cautela para não perder dados!
    * `'a'` (append): Modo de anexar. Adiciona conteúdo ao final de um arquivo existente. Se o arquivo não existir, um novo é criado. O ponteiro de escrita começa no final do arquivo.
    * `'x'` (exclusive creation): Cria um novo arquivo. Se o arquivo já existir, ocorre um `FileExistsError`. Útil para garantir que você está criando um arquivo novo e não sobrescrevendo um existente.
    * `'b'` (binary): Usado para abrir arquivos em modo binário (para dados não textuais como imagens, vídeos, executáveis). Deve ser combinado com outros modos (ex: `'rb'`, `'wb'`, `'ab'`).
    * `'t'` (text): Usado para abrir arquivos em modo texto (padrão se nenhum 'b' for especificado). O conteúdo é tratado como strings.

    **A Melhor Prática: A instrução `with open(...) as f:`**
    Esta é a forma recomendada de trabalhar com arquivos em Python. Ela é conhecida como um "context manager" e garante que o arquivo seja automaticamente fechado (o método `.close()` é chamado), mesmo que ocorra um erro durante as operações de leitura/escrita. Isso previne vazamentos de recursos e a corrupção de dados.
    """)
    st.code("""
# Define um nome de arquivo para os exemplos
nome_arquivo = "diario_de_bordo.txt"

# --- Escrita em arquivo (modo 'w': sobrescreve ou cria) ---
st.write("### Escrevendo em um arquivo (modo 'w')")
conteudo_para_escrever = "Dia 1: Aprendendo Python é divertido!\\n" # \\n para nova linha
conteudo_para_escrever += "Dia 2: Streamlit torna tudo mais fácil.\\n"

try:
    # 'with' garante que o arquivo será fechado automaticamente
    # encoding="utf-8" é importante para caracteres especiais (acentos, etc.)
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo_para_escrever) # Escreve a string no arquivo
    st.success(f"Arquivo '{nome_arquivo}' criado e escrito com sucesso (modo 'w').")
except Exception as e:
    st.error(f"Erro ao escrever no arquivo: {e}")

# --- Leitura de arquivo (modo 'r') ---
st.write("### Lendo de um arquivo (modo 'r')")
try:
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo_lido_inteiro = f.read() # Lê TODO o conteúdo do arquivo como uma única string
        st.info("Conteúdo completo do arquivo 'diario_de_bordo.txt' (f.read()):")
        st.code(conteudo_lido_inteiro)

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines() # Lê todas as linhas e retorna uma LISTA de strings, cada uma com '\n'
        st.info("Conteúdo do arquivo por linha (f.readlines()):")
        for i, linha in enumerate(linhas):
            st.code(f"Linha {i+1}: {linha.strip()}") # .strip() remove o \\n e outros espaços em branco

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        st.info("Lendo linha por linha com loop for (mais eficiente para arquivos grandes):")
        for linha in f: # Iterar sobre o objeto arquivo lê linha por linha de forma eficiente
            st.code(f"-> {linha.strip()}")

except FileNotFoundError:
    st.error(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado para leitura.")
except Exception as e:
    st.error(f"Erro ao ler o arquivo: {e}")

# --- Adicionar conteúdo (modo 'a': anexa) ---
st.write("### Adicionando conteúdo a um arquivo existente (modo 'a')")
conteudo_novo = "Dia 3: Dominando a manipulação de arquivos.\\n"
try:
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        f.write(conteudo_novo) # Adiciona ao final do arquivo
    st.success(f"Conteúdo adicionado ao arquivo '{nome_arquivo}' (modo 'a').")

    # Ler novamente para verificar o conteúdo atualizado
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo_atualizado = f.read()
    st.info("Conteúdo atualizado do arquivo 'diario_de_bordo.txt':")
    st.code(conteudo_atualizado)
except Exception as e:
    st.error(f"Erro ao adicionar conteúdo ao arquivo: {e}")

# Exemplo de escrita em modo binário (para ilustrar, sem um arquivo de imagem real)
st.write("### Exemplo de manipulação de arquivo binário")
# Não executaremos este bloco, mas a estrutura seria assim:
# try:
#     with open("imagem_fake.bin", "wb") as f_bin: # 'wb' para escrever em binário
#         f_bin.write(b"\\x42\\x4D\\x00\\x00\\x00\\x00") # Exemplo de bytes
#     st.success("Arquivo binário fake criado.")
# except Exception as e:
#     st.error(f"Erro ao criar arquivo binário: {e}")
""")
    st.write("""
    **Melhores Práticas:**
    * **Sempre use `with open(...) as f:`** para garantir que os arquivos sejam fechados corretamente.
    * Sempre especifique o `encoding` (geralmente `utf-8`) ao abrir arquivos de texto para evitar problemas com caracteres especiais.
    * Entenda a diferença entre `read()`, `readline()`, `readlines()` e iterar diretamente sobre o objeto arquivo (`for linha in f:`). Para arquivos muito grandes, iterar linha por linha é a forma mais eficiente em memória.
    * Tenha cuidado ao usar o modo `'w'`, pois ele apaga o conteúdo existente. Se precisar adicionar, use `'a'`.
    * Utilize o tratamento de erros (`try-except`) para lidar com `FileNotFoundError`, `PermissionError` e outros problemas que podem surgir ao manipular arquivos.

    **Erro Comum:** Esquecer de fechar um arquivo (o que pode levar a perda de dados ou arquivos corrompidos) ou tentar ler um arquivo que não existe sem tratamento de erro.
    """)
    st.write("---")

    st.subheader("3. Módulos e Pacotes")
    st.write("""
    À medida que seus programas crescem em complexidade e tamanho, é impraticável e ineficiente manter todo o código em um único arquivo. É aí que entram os **módulos** e **pacotes**, conceitos fundamentais para organizar, reutilizar e gerenciar seu código Python. Eles permitem que você divida seu programa em unidades lógicas menores e autocontidas.

    * **Módulo**: É simplesmente um arquivo Python (`.py`) que contém código Python. Um módulo pode definir funções, classes, variáveis e até mesmo outras declarações executáveis. Quando você importa um módulo, todas as definições dentro dele se tornam acessíveis no seu programa.
        * **Analogia**: Pense em um módulo como um livro em uma biblioteca. Cada livro aborda um tópico específico e contém informações relacionadas.
    * **Pacote**: É uma coleção de módulos relacionados. Ele é organizado como um diretório contendo outros módulos e (historicamente, em versões mais antigas do Python) um arquivo especial chamado `__init__.py` (que pode estar vazio, mas indica ao Python que o diretório é um pacote). A partir do Python 3.3, diretórios vazios sem `__init__.py` também são reconhecidos como pacotes (namespace packages), mas `__init__.py` ainda é útil para inicialização do pacote. Pacotes permitem organizar módulos relacionados em uma estrutura hierárquica, evitando conflitos de nomes (colisões de nomes) e melhorando a organização.
        * **Analogia**: Um pacote seria como uma seção da biblioteca (ex: "Ficção Científica", "História"), que contém vários livros (módulos) sobre aquele tema.

    Para usar o código de um módulo ou pacote em seu programa (ou script), você usa a palavra-chave `import`.

    **Formas de Importação:**
    * `import nome_do_modulo`: Importa o módulo inteiro. Você acessa seus conteúdos usando `nome_do_modulo.item` (ex: `math.sqrt(16)`). É a forma mais comum e recomendada, pois evita colisões de nomes e deixa claro de onde o `item` veio.
    * `import nome_do_modulo as alias`: Importa o módulo e dá a ele um apelido (alias) para facilitar o uso, especialmente para módulos com nomes longos ou que são comumente abreviados (ex: `import numpy as np`, `np.array([1,2,3])`).
    * `from nome_do_modulo import item_especifico`: Importa apenas um item (função, classe, variável) específico do módulo. Você pode usá-lo diretamente pelo nome, sem prefixo (ex: `from math import sqrt`, depois `sqrt(16)`). **Use com moderação** para evitar colisões de nomes se você importar muitos itens.
    * `from nome_do_pacote import nome_do_modulo`: Para importar um módulo de dentro de um pacote. Você ainda precisará usar `nome_do_modulo.item` para acessar o conteúdo.
    * `from nome_do_pacote.nome_do_submodulo import item`: Para importar um item específico de um submódulo dentro de um pacote.
    * `from nome_do_modulo import *`: **NÃO RECOMENDADO!** Importa *todos* os itens públicos de um módulo diretamente para o namespace atual. Isso pode causar colisões de nomes e tornar o código difícil de entender (não é óbvio de onde veio uma função específica).

    **Por que são importantes?** Módulos e pacotes são a base do ecossistema Python. Eles permitem que desenvolvedores compartilhem código (bibliotecas como NumPy, Pandas, Requests, Streamlit), promovem a reutilização e facilitam a colaboração em projetos grandes.
""")
    st.code("""
# Exemplo 1: Importando um módulo inteiro e usando suas funções
import math # Módulo embutido do Python para operações matemáticas

st.write("### Exemplo 1: Importando 'math'")
numero = 25
raiz_quadrada = math.sqrt(numero) # Acessa a função sqrt() do módulo math
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

pi_valor = math.pi # Acessa a constante pi do módulo math
print(f"O valor de Pi é: {pi_valor}")

# Exemplo 2: Importando com alias (apelido)
import datetime as dt # 'dt' é o alias para 'datetime'

st.write("\\n### Exemplo 2: Importando 'datetime' com alias 'dt'")
agora = dt.datetime.now() # Usa o alias para acessar o módulo e sua classe
print(f"Data e hora atual: {agora}")
print(f"Ano atual: {agora.year}")

# Exemplo 3: Importando itens específicos de um módulo
from random import randint, choice # Importa apenas as funções randint e choice do módulo random

st.write("\\n### Exemplo 3: Importando funções específicas de 'random'")
dado = randint(1, 6) # Usado diretamente, sem 'random.'
print(f"Resultado do lançamento do dado: {dado}")

frutas_disponiveis = ["maçã", "banana", "uva", "morango"]
fruta_sorteada = choice(frutas_disponiveis) # Usado diretamente
print(f"Fruta sorteada: {fruta_sorteada}")

# Exemplo 4: Estrutura de Pacotes (simulada)
# Imagine a seguinte estrutura de diretórios:
# meu_projeto/
# ├── main.py
# └── utilidades/
#     ├── __init__.py
#     ├── matematica.py
#     └── texto.py

# Conteúdo de utilidades/matematica.py:
# def somar(a, b):
#     return a + b
# def subtrair(a, b):
#     return a - b

# Conteúdo de utilidades/texto.py:
# def formatar_nome(nome_completo):
#     return nome_completo.upper()

# Em main.py, você faria:
# from utilidades import matematica
# from utilidades.texto import formatar_nome

# st.write("\\n### Exemplo 4: Importando de um pacote (simulado)")
# resultado_soma_pkg = matematica.somar(5, 3)
# print(f"Soma do pacote: {resultado_soma_pkg}")
# nome_formatado_pkg = formatar_nome("Maria Clara")
# print(f"Nome formatado do pacote: {nome_formatado_pkg}")

""")
    st.write("""
    **Melhores Práticas:**
    * Sempre use `import nome_do_modulo` (ou `import nome_do_modulo as alias`) como primeira opção. Isso torna o código mais legível e evita conflitos de nomes.
    * Evite `from modulo import *` a todo custo em código de produção, pois dificulta a identificação da origem das funções e pode levar a conflitos de nomes silenciosos.
    * Organize seu código em módulos e pacotes lógicos à medida que ele cresce.
    * Coloque as declarações `import` no topo do arquivo.

    **Erro Comum:** `ModuleNotFoundError` se o módulo ou pacote não puder ser encontrado (verifique o nome, o caminho e se está instalado), ou `NameError` se você usou `import modulo` mas tentou chamar `item_do_modulo` sem o prefixo `modulo.`.
    """)
    st.write("---")
