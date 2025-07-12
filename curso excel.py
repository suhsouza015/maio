import streamlit as st
import pandas as pd
import re # Para expressões regulares, útil na validação de fórmulas

def curso_excel():
    st.set_page_config(layout="wide", page_title="Curso de Excel: Do Zero ao Expert")
    st.title("🚀 Curso de Excel: Do Zero ao Expert")
    st.write("Seja bem-vindo(a)! Prepare-se para dominar o Excel com este curso interativo e prático. Vamos construir seu conhecimento passo a passo.")

    st.sidebar.header("Navegação do Curso")
    modulo_selecionado = st.sidebar.radio(
        "Escolha o módulo:",
        ("👋 Início Rápido e Interface",
         "🔢 Excel Básico: Cálculos e Lógica",
         "🔍 Excel Intermediário: Buscas e Condições Múltiplas",
         "📊 Excel Avançado: Análise e Automação",
         "💡 Dicas de Produtividade e Boas Práticas",
         "🚀 Desvendando o Power Query",
         "🏆 Projeto Final: Dashboard Interativo"
         )
    )

    # --- Funções para cada módulo ---
    if modulo_selecionado == "👋 Início Rápido e Interface":
        introducao_excel()
        quiz_introducao()
    elif modulo_selecionado == "🔢 Excel Básico: Cálculos e Lógica":
        excel_basico()
        quiz_basico()
    elif modulo_selecionado == "🔍 Excel Intermediário: Buscas e Condições Múltiplas":
        excel_intermediario()
        quiz_intermediario()
    elif modulo_selecionado == "📊 Excel Avançado: Análise e Automação":
        excel_avancado()
        quiz_avancado()
    elif modulo_selecionado == "💡 Dicas de Produtividade e Boas Práticas":
        dicas_produtividade() # Nova função
        quiz_dicas_produtividade()
    elif modulo_selecionado == "🚀 Desvendando o Power Query":
        power_query_modulo() # Nova função
        quiz_power_query()
    elif modulo_selecionado == "🏆 Projeto Final: Dashboard Interativo":
        projeto_final()

# --- Módulos de Conteúdo ---

def introducao_excel():
    st.header("1. 👋 Início Rápido e Interface do Excel")
    st.write("Vamos começar do básico, entendendo como o Excel funciona e como você pode interagir com ele de forma eficiente.")

    st.subheader("1.1. O que é o Excel e Por que Usá-lo?")
    st.markdown("""
    O **Excel** é muito mais que uma simples tabela. É uma **ferramenta de planilha eletrônica** da Microsoft, indispensável para:
    * **Organização de Dados**: Listas, cadastros, inventários.
    * **Cálculos e Análises Numéricas**: Orçamentos, finanças, estatísticas.
    * **Visualização de Dados**: Gráficos e dashboards.
    * **Automação de Tarefas**: Com fórmulas complexas, Power Query e VBA.

    É o coração de muitas operações empresariais e uma habilidade valorizada em qualquer carreira.
    """)

    st.subheader("1.2. Conhecendo a Interface do Usuário (UI)")
    st.write("A interface do Excel pode parecer complexa à primeira vista, mas entender suas partes te dará confiança.")
    st.info("""
    * **Faixa de Opções (Ribbon)**: A "central de comando" do Excel. Ela é dividida em guias (Página Inicial, Inserir, Desenvolvedor, etc.), e cada guia tem grupos de ferramentas.
    * **Barra de Fórmulas**: Fica logo acima das colunas. É aqui que você vê e edita o conteúdo da célula selecionada, seja texto, número ou uma fórmula.
    * **Células, Linhas e Colunas**: A malha principal da planilha.
        * **Célula**: A menor unidade, intersecção de uma linha e uma coluna (ex: `A1`, `C5`). Cada célula tem um **endereço único**.
        * **Linhas**: Numeradas (1, 2, 3...).
        * **Colunas**: Nomeadas por letras (A, B, C...).
    * **Planilhas (Sheets)**: Cada arquivo Excel (Pasta de Trabalho) pode ter várias planilhas. Você as vê nas abas na parte inferior.
    * **Barra de Status**: Na parte inferior, mostra informações úteis (média, soma, contagem) das células selecionadas.
    """)
    st.markdown("---")

    st.subheader("1.3. Inserindo, Selecionando e Formatando Dados")
    st.write("A base de tudo é saber como colocar e apresentar seus dados.")
    st.markdown("""
    * **Inserir Dados**: Clique em uma célula e digite. Pressione `Enter` para ir para a célula de baixo, `Tab` para ir para a direita.
    * **Selecionar Células/Intervalos**:
        * Clique e arraste para selecionar um intervalo.
        * `Ctrl + A`: Seleciona tudo.
        * `Ctrl + Shift + Seta`: Seleciona até o fim dos dados em uma direção.
        * `Ctrl + Espaço`: Seleciona a coluna inteira.
        * `Shift + Espaço`: Seleciona a linha inteira.
    * **Formatar Dados**: Mude a aparência para legibilidade e clareza. Use as opções na guia **Página Inicial**: Negrito, Itálico, Cores de Preenchimento/Fonte, Bordas, Formatos Numéricos (Moeda, Porcentagem, Data, etc.).
    """)

    st.subheader("Exercício 1: Familiarizando-se com a Interface")
    st.write("Abra uma nova pasta de trabalho no Excel e siga os passos:")
    st.markdown("""
    1.  Na célula **A1**, digite `Lista de Compras`. Deixe em **negrito** e **centralize** no intervalo A1:C1.
    2.  Nas células **A2**, **B2** e **C2**, digite `Item`, `Quantidade` e `Preço Unitário`, respectivamente. Coloque-os em **negrito** e **alinhe à esquerda**.
    3.  Preencha 3 linhas com itens, quantidades e preços (ex: `Maçã`, `5`, `3.50`).
    4.  Formate a coluna `Preço Unitário` para **Moeda (R$)**.
    5.  Altere a cor de preenchimento da célula `A1` para um **azul claro**.
    6.  **Renomeie** a Planilha1 para `Minhas Compras`.
    """)
    st.markdown("---")

def excel_basico():
    st.header("2. 🔢 Excel Básico: Cálculos e Lógica")
    st.write("Aqui você vai desvendar o poder das fórmulas e funções essenciais para realizar cálculos e tomar decisões simples nos seus dados.")

    st.subheader("2.1. O Poder das Fórmulas e Referências")
    st.markdown("""
    Uma **fórmula** no Excel sempre começa com um sinal de igual (`=`). Elas realizam cálculos ou ações.
    * **Operadores Aritméticos**: `+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão), `^` (potência).
        * Ex: `=10*5` (resultado 50)
    * **Referências de Célula**: Em vez de números fixos, use endereços de células. Isso torna suas fórmulas dinâmicas!
        * Ex: Se `A1` tem 10 e `B1` tem 5, `=A1*B1` (resultado 50). Se você mudar `A1` para 20, a fórmula se atualiza para 100 automaticamente.

    #### Tipos de Referências
    * **Relativas (A1)**: Mudam quando a fórmula é copiada. Padrão.
    * **Absolutas ($A$1)**: Permanecem fixas quando a fórmula é copiada. Use `F4` para alternar ao digitar a fórmula. Ideal para valores fixos (taxas, constantes).
    * **Mistas (A$1 ou $A1)**: Fixa apenas a linha ou a coluna.
    """)

    st.subheader("2.2. Funções Essenciais: SOMA, MÉDIA, MÍNIMO, MÁXIMO, CONT.NÚM, CONT.VALORES")
    st.write("As funções são fórmulas pré-definidas que simplificam cálculos complexos.")
    st.markdown("""
    * **SOMA**: Soma os valores de um intervalo.
        * **Sintaxe**: `=SOMA(intervalo)` ou `=SOMA(número1; [número2]; ...)`
        * **Exemplo**: `=SOMA(A1:A5)`
    * **MÉDIA**: Calcula a média aritmética.
        * **Sintaxe**: `=MÉDIA(intervalo)`
        * **Exemplo**: `=MÉDIA(B2:B10)`
    * **MÍNIMO / MÁXIMO**: Encontra o menor/maior valor.
        * **Sintaxe**: `=MÍNIMO(intervalo)`, `=MÁXIMO(intervalo)`
    * **CONT.NÚM**: Conta células que contêm **números**.
        * **Sintaxe**: `=CONT.NÚM(intervalo)`
    * **CONT.VALORES**: Conta células que **não estão vazias** (números, texto, erros).
        * **Sintaxe**: `=CONT.VALORES(intervalo)`
    """)

    st.subheader("2.3. Função SE (IF): Tomada de Decisão")
    st.write("A função `SE` é a base da lógica condicional no Excel. Ela permite que sua planilha 'tome decisões'.")
    st.markdown("""
    * **Sintaxe**: `=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)`
        * **`teste_lógico`**: Uma pergunta que resulta em VERDADEIRO ou FALSO (ex: `A1>100`, `B2="Ativo"`).
        * **`valor_se_verdadeiro`**: O que o Excel faz se o teste lógico for VERDADEIRO.
        * **`valor_se_falso`**: O que o Excel faz se o teste lógico for FALSO.
    """)
    st.subheader("Exemplo Prático: Status de Vendas")
    st.code("""
    | Vendedor | Vendas (B) | Meta (C) | Status (D) |
    |---|---|---|---|
    | Ana      | 12000      | 10000    |            |
    | Pedro    | 8000       | 10000    |            |
    """)
    st.write("Na célula **D2**, para verificar se a Ana atingiu a meta:")
    st.code(f"=SE(B2>=C2; 'Meta Atingida'; 'Abaixo da Meta')")
    st.write("Se arrastar para baixo, a referência `B2` e `C2` se tornará `B3` e `C3` automaticamente (referência relativa).")
    st.markdown("---")

    st.subheader("Exercício 2: Aplicando Funções Essenciais e Lógica")
    st.write("Crie a seguinte tabela no Excel:")
    st.code("""
    | Produto   | Quantidade Vendida | Preço Unitário |
    |-----------|--------------------|----------------|
    | Caneta    | 15                 | 2.50           |
    | Caderno   | 8                  | 12.00          |
    | Lápis     | 25                 | 1.50           |
    | Borracha  | 10                 | 0.75           |
    | Total     |                    |                |
    | Média     |                    |                |
    | Maior Venda|                    |                |
    """)
    st.markdown("""
    1.  Na coluna D (Vendas Totais), calcule o **`Valor Total`** para cada produto (`Quantidade Vendida * Preço Unitário`).
    2.  Na linha "Total", use a função **`SOMA`** para obter o total geral de `Quantidade Vendida` e `Vendas Totais`.
    3.  Na linha "Média", use a função **`MÉDIA`** para calcular a média de `Quantidade Vendida` e `Vendas Totais`.
    4.  Na linha "Maior Venda", use a função **`MÁXIMO`** para encontrar a maior `Vendas Totais`.
    5.  Adicione uma coluna E chamada "Desempenho". Use a função **`SE`** para classificar cada produto: se as `Vendas Totais` forem maiores que 50, o "Desempenho" será "Bom", caso contrário, "Regular".
    """)

    # Validação do exercício (simplificada)
    with st.expander("Verificar Respostas (Sugestão de Fórmulas)"):
        st.markdown("""
        * **Valor Total (D2)**: `=B2*C2` (e arraste para baixo)
        * **Total Quantidade Vendida (B6)**: `=SOMA(B2:B5)`
        * **Total Vendas Totais (D6)**: `=SOMA(D2:D5)`
        * **Média Quantidade Vendida (B7)**: `=MÉDIA(B2:B5)`
        * **Média Vendas Totais (D7)**: `=MÉDIA(D2:D5)`
        * **Maior Venda (D8)**: `=MÁXIMO(D2:D5)`
        * **Desempenho (E2)**: `=SE(D2>50; 'Bom'; 'Regular')` (e arraste para baixo)
        """)
    st.markdown("---")


def quiz_introducao():
    st.header("❓ Quiz: Início Rápido e Interface")
    st.write("Teste seus conhecimentos sobre os conceitos básicos do Excel!")

    st.subheader("Pergunta 1")
    q1_options = ["Faixa de Fórmulas", "Barra de Fórmulas", "Área de Trabalho", "Ribbon Principal"]
    q1_answer = st.radio("Qual é o nome da barra que mostra o conteúdo da célula selecionada e permite editar fórmulas?", q1_options, key="q1_intro")
    if st.button("Verificar Pergunta 1", key="btn_q1_intro"):
        if q1_answer == "Barra de Fórmulas":
            st.success("Correto! 🎉 A Barra de Fórmulas é onde você vê e edita o conteúdo das células.")
        else:
            st.error("Ops! Tente novamente. Lembre-se de onde você digita e edita as fórmulas.")
    st.markdown("---")

    st.subheader("Pergunta 2")
    q2_options = ["Um arquivo com várias pastas", "Uma intersecção de uma linha e uma coluna", "Um gráfico complexo", "Uma função de cálculo"]
    q2_answer = st.radio("No Excel, o que representa uma 'Célula'?", q2_options, key="q2_intro")
    if st.button("Verificar Pergunta 2", key="btn_q2_intro"):
        if q2_answer == "Uma intersecção de uma linha e uma coluna":
            st.success("Correto! Uma célula é a unidade básica para inserir dados no Excel.")
        else:
            st.error("Incorreto. Pense em como os dados são organizados em uma grade.")
    st.markdown("---")


def quiz_basico():
    st.header("❓ Quiz: Excel Básico")
    st.write("Verifique sua compreensão das funções essenciais!")

    st.subheader("Pergunta 1")
    q1_options = ["`=MEDIA(A1; A5)`", "`=MEDIANA(A1:A5)`", "`=MÉDIA(A1:A5)`", "`=AVERAGE(A1-A5)`"]
    q1_answer = st.radio("Qual fórmula calcularia a média dos valores nas células A1, A2, A3, A4 e A5?", q1_options, key="q1_basico")
    if st.button("Verificar Pergunta 1", key="btn_q1_basico"):
        if q1_answer == "`=MÉDIA(A1:A5)`":
            st.success("Correto! 🎉 A função MÉDIA com o intervalo correto.")
        else:
            st.error("Incorreto. Revise a sintaxe da função MÉDIA.")
    st.markdown("---")

    st.subheader("Pergunta 2")
    q2_options = ["`=SE(A1>10; 'Alto')`", "`=SE(A1>10; 'Alto'; 'Baixo')`", "`=SE(A1;'Alto';'Baixo')`", "`=SE(A1>10, 'Alto', 'Baixo')`"]
    q2_answer = st.radio("Você quer classificar um número na célula A1 como 'Alto' se for maior que 10, e 'Baixo' caso contrário. Qual a fórmula correta?", q2_options, key="q2_basico")
    if st.button("Verificar Pergunta 2", key="btn_q2_basico"):
        if q2_answer == "`=SE(A1>10; 'Alto'; 'Baixo')`":
            st.success("Correto! 🎉 Você usou a sintaxe completa da função SE.")
        else:
            st.error("Ops! A função SE precisa de três argumentos: teste lógico, valor se verdadeiro e valor se falso.")
    st.markdown("---")


def excel_intermediario():
    st.header("3. 🔍 Excel Intermediário: Buscas e Condições Múltiplas")
    st.write("Agora, vamos avançar para funções que permitem buscar informações em grandes bases de dados e aplicar lógica com múltiplos critérios. Essencial para análises mais complexas!")

    st.subheader("3.1. Funções de Busca: PROCV (VLOOKUP) e PROCH (HLOOKUP)")
    st.write("Estas funções são o coração da integração de dados em planilhas diferentes ou dentro da mesma planilha. Elas buscam um valor e retornam outro relacionado.")
    st.markdown("""
    * **PROCV (VLOOKUP)**: Procura um valor na **primeira coluna** de um intervalo e retorna um valor correspondente de outra coluna na **mesma linha**. (O 'V' é de Vertical).
        * **Sintaxe**: `=PROCV(valor_procurado; matriz_tabela; núm_índice_coluna; [intervalo_pesquisa])`
            * **`valor_procurado`**: O que você quer procurar (ex: um ID de produto).
            * **`matriz_tabela`**: O intervalo de células onde o Excel vai procurar. **A primeira coluna deste intervalo DEVE conter o `valor_procurado`.**
            * **`núm_índice_coluna`**: O número da coluna na `matriz_tabela` de onde você quer retornar o valor (ex: se o preço está na 3ª coluna, use `3`).
            * **`[intervalo_pesquisa]`**: `VERDADEIRO` (busca aproximada, padrão) ou `FALSO` (busca exata). **Use SEMPRE `FALSO` para resultados precisos.**
    * **PROCH (HLOOKUP)**: Similar ao PROCV, mas procura o valor na **primeira LINHA** de um intervalo. (O 'H' é de Horizontal). Menos comum que o PROCV.
        * **Sintaxe**: `=PROCH(valor_procurado; matriz_tabela; núm_índice_linha; [intervalo_pesquisa])`
    """)

    st.subheader("Exemplo Prático: Automatizando Preços de Pedidos")
    st.code("""
    **Tabela de Produtos (Aba: Produtos)**
    | ID Produto (A) | Nome Produto (B) | Preço (C) |
    |----------------|------------------|-----------|
    | P001           | Caneta           | 2.50      |
    | P002           | Lápis            | 1.00      |
    | P003           | Caderno          | 15.00     |

    **Tabela de Pedidos (Aba: Pedidos)**
    | Pedido (A) | ID Produto (B) | Preço Unitário (C) |
    |------------|----------------|--------------------|
    | 101        | P001           |                    |
    | 102        | P003           |                    |
    """)
    st.write("Na **Tabela de Pedidos**, para buscar o 'Preço Unitário' a partir do 'ID Produto':")
    st.write(f"Na célula **C2** (para o Pedido 101), supondo que a Tabela de Produtos esteja na 'Produtos'!A1:C4:")
    st.code(f"='=PROCV(B2; Produtos!$A$1:$C$4; 3; FALSO)'")
    st.write("Perceba o uso de `$` (referência absoluta) na `matriz_tabela`. Isso é crucial para que, ao arrastar a fórmula, o intervalo de busca não mude!")
    st.markdown("---")

    st.subheader("3.2. Funções Condicionais Múltiplas: SOMASES (SUMIFS) e CONT.SES (COUNTIFS)")
    st.write("Enquanto `SOMASE` e `CONT.SE` usam um único critério, as versões com 'ES' permitem combinar **vários critérios** para somar ou contar.")
    st.markdown("""
    * **SOMASES (SUMIFS)**: Soma células que satisfazem **todos** os critérios especificados.
        * **Sintaxe**: `=SOMASES(intervalo_soma; intervalo_critério1; critério1; [intervalo_critério2; critério2]; ...)`
        * **Atenção!** Diferente do `SOMASE`, o `intervalo_soma` é o **primeiro argumento**.
        * **Exemplo**: Somar vendas do vendedor 'Carlos' na região 'Sudeste' com valor maior que 500.
    * **CONT.SES (COUNTIFS)**: Conta o número de células que satisfazem **todos** os critérios especificados.
        * **Sintaxe**: `=CONT.SES(intervalo_critério1; critério1; [intervalo_critério2; critério2]; ...)`
        * **Exemplo**: Contar quantos pedidos foram feitos por 'João' em '2024' e com status 'Concluído'.
    """)
    st.subheader("Exemplo Prático: Análise de Pedidos Detalhada")
    st.code("""
    | Vendedor | Mês      | Região  | Valor da Venda |
    |----------|----------|---------|----------------|
    | Carlos   | Janeiro  | Sul     | 1000           |
    | Ana      | Fevereiro| Norte   | 1500           |
    | Carlos   | Fevereiro| Sul     | 800            |
    | Maria    | Janeiro  | Norte   | 2000           |
    """)
    st.write("Para somar as vendas do 'Carlos' na 'Região Sul':")
    st.code(f"='=SOMASES(D2:D5; A2:A5; \"Carlos\"; C2:C5; \"Sul\")'")
    st.write(f"Resultado: **1800** (1000 de Janeiro + 800 de Fevereiro).")
    st.markdown("---")

    st.subheader("Exercício 3: Análise de Pedidos com Múltiplos Critérios")
    st.write("Considere as duas tabelas abaixo no Excel (idealmente em planilhas separadas: 'Clientes' e 'Pedidos'):")
    st.code("""
    **Tabela 1: Clientes (Aba: Clientes)**
    | ID Cliente | Nome Cliente | Cidade     |
    |------------|--------------|------------|
    | C001       | João Silva   | São Paulo  |
    | C002       | Maria Souza  | Rio de Janeiro |
    | C003       | Ana Lima     | São Paulo  |
    | C004       | Pedro Santos | Belo Horizonte |

    **Tabela 2: Pedidos (Aba: Pedidos)**
    | ID Pedido | ID Cliente | Data Pedido | Valor Pedido | Status     |
    |-----------|------------|-------------|--------------|------------|
    | P101      | C001       | 05/01/2024  | 250.00       | Entregue   |
    | P102      | C003       | 15/01/2024  | 150.00       | Pendente   |
    | P103      | C001       | 20/02/2024  | 300.00       | Entregue   |
    | P104      | C002       | 01/03/2024  | 500.00       | Entregue   |
    | P105      | C004       | 10/03/2024  | 200.00       | Pendente   |
    | P106      | C003       | 25/03/2024  | 100.00       | Entregue   |
    """)
    st.markdown("""
    1.  Na Tabela 2 (Pedidos), adicione uma coluna `F` chamada "**Nome Cliente**". Use **`PROCV`** para trazer o nome do cliente da Tabela 1 com base no `ID Cliente`.
    2.  Adicione uma coluna `G` chamada "**Cidade Cliente**" na Tabela 2. Use **`PROCV`** novamente para trazer a cidade do cliente da Tabela 1.
    3.  Calcule o **valor total de pedidos** feitos por clientes de "**São Paulo**" com status "**Entregue**".
    4.  Conte quantos pedidos foram feitos por "**João Silva**" com status "**Pendente**" OU com `Valor Pedido` superior a 200. (Dica: Pense em como você combinaria `CONT.SES` ou usaria `SE` aninhado com `OU`).
    5.  Qual o **valor médio** dos pedidos realizados em **Março de 2024**?
    """)
    with st.expander("Verificar Respostas (Sugestão de Fórmulas)"):
        st.markdown("""
        * **Nome Cliente (F2 na aba Pedidos)**: `=PROCV(B2; Clientes!$A$2:$C$5; 2; FALSO)`
        * **Cidade Cliente (G2 na aba Pedidos)**: `=PROCV(B2; Clientes!$A$2:$C$5; 3; FALSO)`
        * **Valor Total SP Entregue**: `=SOMASES(D2:D7; G2:G7; "São Paulo"; E2:E7; "Entregue")`
        * **Pedidos João Pendente ou >200**: Poderia ser `=CONT.SES(F2:F7; "João Silva"; E2:E7; "Pendente") + CONT.SES(F2:F7; "João Silva"; D2:D7; ">200")` (contando duplicidade) ou uma abordagem mais complexa com `MATRIZPROD` ou coluna auxiliar com `SE(E2="Pendente";OU(E2="Pendente";D2>200);...)`. Para simplificar, o `CONT.SES` direto é o mais esperado.
        * **Valor Médio Março 2024**: `=MÉDIASES(D2:D7; C2:C7; ">=01/03/2024"; C2:C7; "<=31/03/2024")`
        """)
    st.markdown("---")


def quiz_intermediario():
    st.header("❓ Quiz: Excel Intermediário")
    st.write("Verifique seu domínio das funções de busca e condicionais múltiplas!")

    st.subheader("Pergunta 1")
    q1_options = ["`=PROCV(B1; A1:C10; 2; VERDADEIRO)`", "`=PROCV(B1; A1:C10; 2; FALSO)`", "`=PROCH(B1; A1:C10; 2; FALSO)`", "`=PROCV(A1:C10; B1; 2; FALSO)`"]
    q1_answer = st.radio("Você tem um ID de produto na célula B1 e quer encontrar o nome desse produto que está na segunda coluna de uma tabela em A1:C10. Qual a fórmula PROCV correta para uma busca exata?", q1_options, key="q1_intermediario")
    if st.button("Verificar Pergunta 1", key="btn_q1_intermediario"):
        if q1_answer == "`=PROCV(B1; A1:C10; 2; FALSO)`":
            st.success("Correto! 🎉 O `FALSO` é crucial para busca exata.")
        else:
            st.error("Ops! Lembre-se da ordem dos argumentos no PROCV e da importância do último argumento para busca exata.")
    st.markdown("---")

    st.subheader("Pergunta 2")
    q2_options = ["`=SOMA(D1:D10; A1:A10; 'Vendas'; B1:B10; '2024')`", "`=SOMASES(D1:D10; A1:A10; 'Vendas'; B1:B10; '2024')`", "`=SOMASE(D1:D10; 'Vendas', '2024')`", "`=CONT.SES(D1:D10; A1:A10; 'Vendas'; B1:B10; '2024')`"]
    q2_answer = st.radio("Qual fórmula usaria para somar o 'Valor Total' (coluna D) de vendas do 'Departamento' (coluna A) 'Vendas' no 'Ano' (coluna B) '2024'?", q2_options, key="q2_intermediario")
    if st.button("Verificar Pergunta 2", key="btn_q2_intermediario"):
        if q2_answer == "`=SOMASES(D1:D10; A1:A10; 'Vendas'; B1:B10; '2024')`":
            st.success("Correto! 🎉 SOMASES é a função para múltiplos critérios, e a coluna de soma vem primeiro.")
        else:
            st.error("Incorreto. A função SOMASES é para múltiplos critérios e tem uma ordem específica de argumentos.")
    st.markdown("---")

def excel_avancado():
    st.header("4. 📊 Excel Avançado: Análise e Automação")
    st.write("Bem-vindo ao nível onde o Excel se torna uma ferramenta de inteligência de negócios. Aqui, você aprenderá a resumir grandes volumes de dados, criar visualizações dinâmicas e otimizar tarefas.")

    st.subheader("4.1. Tabelas Dinâmicas (Pivot Tables): O Resumidor Mágico")
    st.write("As **Tabelas Dinâmicas** são uma das funcionalidades mais poderosas do Excel. Elas transformam bases de dados gigantes em resumos concisos e interativos, permitindo analisar dados de várias perspectivas.")
    st.markdown("""
    **Para que servem?**
    * **Resumir**: Agrupar dados por categorias (ex: vendas por produto, total de funcionários por departamento).
    * **Analisar**: Encontrar padrões, tendências e exceções.
    * **Explorar**: Reorganizar os dados rapidamente com um "arrasta e solta".
    * **Apresentar**: Criar relatórios e dashboards.

    **Como Criar (Passos Essenciais):**
    1.  Selecione sua base de dados completa (incluindo cabeçalhos).
    2.  Vá na guia **Inserir** > **Tabela Dinâmica**.
    3.  Escolha onde quer colocar a Tabela Dinâmica (geralmente em uma Nova Planilha). Clique em OK.
    4.  No painel **Campos da Tabela Dinâmica** (à direita), arraste os campos para as áreas:
        * **Linhas**: Categorias que você quer ver nas linhas do seu resumo (ex: `Vendedor`, `Mês`).
        * **Colunas**: Categorias que você quer ver nas colunas (menos comum, mas útil para comparações rápidas, ex: `Ano`).
        * **Valores**: Os campos numéricos que você quer somar, contar, obter a média, etc. (ex: `Valor Venda`, `Quantidade`). Por padrão, ele soma, mas você pode mudar para Contagem, Média, Máximo, Mínimo, etc. clicando na setinha ao lado do campo na área de Valores.
        * **Filtros**: Permitem filtrar todo o relatório dinâmico por um ou mais campos (ex: `Região`, `Status`).

    **Dica**: Use o botão direito do mouse sobre os campos na área de "Valores" para escolher o tipo de cálculo (Soma, Contagem, Média, etc.).
    """)

    st.subheader("Exemplo: Analisando Vendas por Região e Categoria")
    st.code("""
    | Região  | Categoria | Vendedor | Valor Venda | Data Venda |
    |---------|-----------|----------|-------------|------------|
    | Sudeste | Eletrônicos| Ana      | 1500        | 01/01/2024 |
    | Sul     | Livros    | Pedro    | 500         | 05/01/2024 |
    | Sudeste | Livros    | Ana      | 800         | 10/01/2024 |
    | Norte   | Eletrônicos| Carlos   | 2500        | 15/01/2024 |
    """)
    st.write("""
    Para ver o total de vendas por **Região** e **Categoria**:
    * Arraste **Região** para `Linhas`.
    * Arraste **Categoria** para `Colunas`.
    * Arraste **Valor Venda** para `Valores`.

    Isso vai te dar um resumo cruzado das vendas. Experimente arrastar **Vendedor** para `Filtros` para ver as vendas de um vendedor específico!
    """)
    st.markdown("---")

    st.subheader("4.2. Gráficos Dinâmicos e Dashboards: Visualizando seus Dados")
    st.write("Um **Gráfico Dinâmico** é um gráfico interativo que está diretamente conectado a uma Tabela Dinâmica. Ele se atualiza automaticamente quando você filtra ou altera sua Tabela Dinâmica.")
    st.markdown("""
    **Como Criar:**
    1.  Selecione **qualquer célula** dentro da sua Tabela Dinâmica.
    2.  Vá na guia **Analisar Tabela Dinâmica** > **Gráfico Dinâmico**.
    3.  Escolha o tipo de gráfico (colunas, barras, pizza, linha, etc.) e clique em OK.

    **Dashboards (Painéis de Controle):**
    Um dashboard é uma coleção de gráficos, tabelas e indicadores-chave de desempenho (KPIs) em uma única planilha, projetado para fornecer uma visão rápida e completa de um conjunto de dados.
    * Use **Segmentação de Dados (Slicers)**: Botões interativos que filtram Tabelas e Gráficos Dinâmicos com um clique. Vá em **Analisar Tabela Dinâmica** > **Inserir Segmentação de Dados**.
    * Use **Linhas do Tempo (Timelines)**: Para filtrar dados por período de tempo. Vá em **Analisar Tabela Dinâmica** > **Inserir Linha do Tempo**.

    Combine esses elementos para criar relatórios visuais impressionantes e interativos!
    """)
    st.markdown("---")

    st.subheader("4.3. Funções Avançadas de Busca: ÍNDICE, CORRESP e DESLOC")
    st.write("Essas funções, especialmente `ÍNDICE` com `CORRESP`, oferecem uma flexibilidade superior ao `PROCV` para cenários complexos.")
    st.markdown("""
    * **ÍNDICE (INDEX)**: Retorna o valor de uma célula na intersecção de uma linha e coluna específicas dentro de um intervalo.
        * **Sintaxe**: `=ÍNDICE(matriz; núm_linha; [núm_coluna])`
        * **Exemplo**: `=ÍNDICE(A1:C10; 3; 2)` retorna o valor da célula `B3`.
    * **CORRESP (MATCH)**: Retorna a **posição relativa** de um item em um intervalo (uma única linha ou coluna) que corresponde a um valor especificado.
        * **Sintaxe**: `=CORRESP(valor_procurado; matriz_procurada; [tipo_correspondência])`
        * **`tipo_correspondência`**: `0` para exata (mais comum), `1` para menor que, `-1` para maior que.
        * **Exemplo**: `=CORRESP("Maçã"; A1:A10; 0)` retorna `5` se "Maçã" estiver na 5ª posição do intervalo.
    * **ÍNDICE + CORRESP**: A combinação perfeita! Você usa `CORRESP` para descobrir a posição da linha e/ou coluna, e `ÍNDICE` para buscar o valor nessa posição. Isso elimina a restrição do `PROCV` de buscar apenas à direita.
        * **Exemplo**: Para buscar o `Preço` de um `Produto` (`valor_procurado` na célula `E1`) numa tabela onde `Produto` está na coluna `B` e `Preço` na coluna `D`:
            `=ÍNDICE(D:D; CORRESP(E1; B:B; 0))`
            * `D:D`: É a coluna de onde você quer o resultado (Preço).
            * `CORRESP(E1; B:B; 0)`: Encontra a linha onde o produto de `E1` está na coluna `B`.
    * **DESLOC (OFFSET)**: Retorna uma referência a um intervalo que é deslocado um número especificado de linhas e colunas de uma referência inicial.
        * **Sintaxe**: `=DESLOC(referência; linhas; colunas; [altura]; [largura])`
        * **Uso Avançado**: Pode criar intervalos dinâmicos, mas é volátil (recalcula a cada mudança na planilha, pode deixar lento).

    **Quando usar ÍNDICE/CORRESP vs PROCV?**
    * **PROCV**: Mais simples para buscas diretas (valor na 1ª coluna, resultado à direita).
    * **ÍNDICE/CORRESP**: Mais flexível. Pode buscar para a esquerda, para cima, ou em tabelas mais complexas. **É a escolha profissional para buscas mais robustas.**
    """)
    st.markdown("---")

    st.subheader("Exercício 4: Construindo uma Base de Dados e Análise Avançada")
    st.write("Vamos criar uma base de dados mais complexa e aplicar as ferramentas avançadas. Crie uma planilha chamada 'Dados Vendas' no Excel com as colunas:")
    st.code("""
    | ID Venda | Data | Vendedor | Região  | Produto | Categoria | Quantidade | Preço Unitário |
    |----------|------|----------|---------|---------|-----------|------------|----------------|
    | V001     | 01/01/2024 | Ana      | Sudeste | Caneta  | Papelaria | 10         | 2.50           |
    | V002     | 02/01/2024 | Pedro    | Sul     | Caderno | Papelaria | 5          | 12.00          |
    | V003     | 05/01/2024 | Ana      | Sudeste | Mouse   | Eletrônicos| 2          | 50.00          |
    | V004     | 10/01/2024 | Carlos   | Norte   | Teclado | Eletrônicos| 1          | 120.00         |
    | V005     | 15/01/2024 | Pedro    | Sul     | Borracha| Papelaria | 20         | 0.75           |
    | V006     | 20/01/2024 | Ana      | Sudeste | Monitor | Eletrônicos| 1          | 350.00         |
    | V007     | 25/01/2024 | Carlos   | Norte   | Livro   | Livros    | 3          | 30.00          |
    """)
    st.markdown("""
    1.  **Coluna `Valor Total`**: Adicione uma coluna **`Valor Total`** (`Quantidade` * `Preço Unitário`).
    2.  **Tabela Dinâmica**: Crie uma **Tabela Dinâmica** para resumir o `Valor Total` por `Região` e `Categoria`.
        * Coloque `Região` nas **Linhas**.
        * Coloque `Categoria` nas **Colunas**.
        * Coloque `Valor Total` nos **Valores** (como Soma).
    3.  **Gráfico Dinâmico**: Crie um **Gráfico de Colunas Agrupadas** a partir da Tabela Dinâmica.
    4.  **Segmentação de Dados**: Insira uma **Segmentação de Dados** para `Vendedor` e `Data` (use `Linha do Tempo` para a data). Conecte-as à sua Tabela Dinâmica.
    5.  **Combinação ÍNDICE/CORRESP**: Crie uma área de "Pesquisa de Venda" em outra aba.
        * Na célula `A1`, coloque `ID Venda para Pesquisa:`.
        * Na célula `B1`, insira um ID de venda (ex: `V003`).
        * Na célula `A2`, coloque `Produto:`.
        * Na célula `B2`, use `ÍNDICE` e `CORRESP` para trazer o `Produto` (coluna `E` da tabela `Dados Vendas`) com base no `ID Venda` (coluna `A` da tabela `Dados Vendas`).
        * Repita para trazer o `Vendedor` e o `Valor Total`.
    """)
    with st.expander("Verificar Respostas (Sugestão de Fórmulas)"):
        st.markdown("""
        * **Valor Total (I2 em 'Dados Vendas')**: `=G2*H2` (e arraste)
        * **Pesquisa de Produto (B2 em nova aba)**: `=ÍNDICE('Dados Vendas'!E:E; CORRESP(B$1; 'Dados Vendas'!A:A; 0))`
        * **Pesquisa de Vendedor (B3 em nova aba)**: `=ÍNDICE('Dados Vendas'!C:C; CORRESP(B$1; 'Dados Vendas'!A:A; 0))`
        * **Pesquisa de Valor Total (B4 em nova aba)**: `=ÍNDICE('Dados Vendas'!I:I; CORRESP(B$1; 'Dados Vendas'!A:A; 0))`
        """)
    st.markdown("---")


def quiz_avancado():
    st.header("❓ Quiz: Excel Avançado")
    st.write("Teste seus conhecimentos em ferramentas de análise complexas!")

    st.subheader("Pergunta 1")
    q1_options = ["Serve apenas para somar dados.", "É uma ferramenta para resumir, analisar e apresentar dados de forma interativa.", "Cria gráficos estáticos.", "Organiza dados em linhas e colunas fixas."]
    q1_answer = st.radio("Qual a principal utilidade de uma Tabela Dinâmica (Pivot Table)?", q1_options, key="q1_avancado")
    if st.button("Verificar Pergunta 1", key="btn_q1_avancado"):
        if q1_answer == "É uma ferramenta para resumir, analisar e apresentar dados de forma interativa.":
            st.success("Correto! 🎉 Tabelas Dinâmicas são incrivelmente versáteis para análise.")
        else:
            st.error("Incorreto. Lembre-se que as Tabelas Dinâmicas são dinâmicas e interativas.")
    st.markdown("---")

    st.subheader("Pergunta 2")
    q2_options = ["`PROCV` e `PROCH` não funcionam com busca exata.", "`ÍNDICE` e `CORRESP` são mais flexíveis, permitindo buscar em qualquer direção.", "`ÍNDICE` e `CORRESP` são mais lentas que `PROCV`.", "`PROCV` sempre retorna múltiplos valores."]
    q2_answer = st.radio("Qual a principal vantagem de usar a combinação ÍNDICE e CORRESP em vez de PROCV ou PROCH?", q2_options, key="q2_avancado")
    if st.button("Verificar Pergunta 2", key="btn_q2_avancado"):
        if q2_answer == "`ÍNDICE` e `CORRESP` são mais flexíveis, permitindo buscar em qualquer direção.":
            st.success("Correto! 🎉 Essa combinação é mais poderosa por sua flexibilidade direcional.")
        else:
            st.error("Ops! Pense nas limitações do PROCV/PROCH e como ÍNDICE/CORRESP as superam.")
    st.markdown("---")


def dicas_produtividade():
    st.header("5. 💡 Dicas de Produtividade e Boas Práticas")
    st.write("Neste módulo, você aprenderá técnicas e ferramentas que farão você trabalhar mais rápido e criar planilhas mais robustas e profissionais.")

    st.subheader("5.1. Validação de Dados: Garantindo a Qualidade")
    st.write("A **Validação de Dados** é uma ferramenta poderosa para controlar o que os usuários podem digitar em uma célula, prevenindo erros e garantindo a consistência dos seus dados.")
    st.markdown("""
    **Como Usar (Dados > Validação de Dados):**
    * **Qualquer Valor**: Permite qualquer entrada.
    * **Número Inteiro/Decimal**: Restringe a números dentro de um intervalo.
    * **Lista**: Cria uma lista suspensa de opções pré-definidas (a mais comum e útil!).
        * Ex: Para uma coluna 'Departamento', crie uma lista com "Vendas", "Marketing", "TI". Isso evita erros de digitação.
    * **Data/Hora**: Restringe a datas ou horas dentro de um período.
    * **Comprimento do Texto**: Limita o número de caracteres.
    * **Personalizado**: Use uma fórmula para definir regras complexas.
    * **Mensagem de Entrada**: Ajuda o usuário a saber o que digitar.
    * **Alerta de Erro**: Mensagem que aparece se a entrada for inválida (parar, aviso, informações).

    **Por que é Importante?** Evita erros de digitação, padroniza entradas, melhora a integridade dos dados para análises futuras.
    """)
    st.markdown("---")

    st.subheader("5.2. Formatação Condicional: Destaque Inteligente")
    st.write("A **Formatação Condicional** não é apenas estética; é uma ferramenta de análise visual. Ela aplica formatos específicos (cores, fontes, ícones) a células que atendem a critérios que você define, destacando padrões, tendências e exceções instantaneamente.")
    st.markdown("""
    **Principais Usos (Página Inicial > Formatação Condicional):**
    * **Realçar Regras das Células**: Maior que, Menor que, Entre, Igual a, Texto que Contém, Data Ocorrendo, Valores Duplicados.
    * **Regras de Primeiros/Últimos**: Top 10 itens/%, Últimos 10 itens/%.
    * **Barras de Dados**: Visualiza o valor da célula em relação a outras com uma barra colorida.
    * **Escalas de Cores**: Aplica um gradiente de cores com base nos valores (ex: verde para alto, vermelho para baixo).
    * **Conjuntos de Ícones**: Adiciona ícones (setas, semáforos) para indicar tendências ou estados.

    **Exemplo**: Destacar em verde vendas acima da meta e em vermelho as abaixo.
    """)
    st.markdown("---")

    st.subheader("5.3. Funções de Texto: Manipulando Strings")
    st.write("Trabalhar com dados de texto é comum, e o Excel tem funções poderosas para limpar, extrair e manipular strings.")
    st.markdown("""
    * **CONCATENAR / CONCAT / &**: Une textos de diferentes células.
        * `=CONCATENAR(A1; " - "; B1)` ou `=A1 & " - " & B1`
    * **ESQUERDA / DIREITA / EXT.TEXTO**: Extrai parte de um texto.
        * `=ESQUERDA(A1; 3)` (os 3 primeiros caracteres)
        * `=DIREITA(A1; 4)` (os 4 últimos caracteres)
        * `=EXT.TEXTO(A1; 5; 2)` (2 caracteres a partir da posição 5)
    * **LOCALIZAR / PROCURAR**: Encontra a posição de um texto dentro de outro. `PROCURAR` não diferencia maiúsculas/minúsculas.
        * `=LOCALIZAR(" "; A1)` (encontra a posição do primeiro espaço)
    * **ARRUMAR**: Remove espaços extras (múltiplos espaços entre palavras, espaços no início/fim). Essencial para limpeza de dados!
        * `=ARRUMAR(A1)`
    * **MAIÚSCULA / MINÚSCULA / PRI.MAIÚSCULA**: Altera a caixa do texto.
        * `=MAIÚSCULA(A1)` (TODO EM MAIÚSCULAS)
        * `=MINÚSCULA(A1)` (todo em minúsculas)
        * `=PRI.MAIÚSCULA(A1)` (Primeira Letra De Cada Palavra Em Maiúscula)
    """)
    st.markdown("---")

    st.subheader("5.4. Funções de Data e Hora: Análise Temporal")
    st.write("Datas e horas são tipos de dados cruciais. Entender como manipulá-las abre portas para análises temporais.")
    st.markdown("""
    * **HOJE() / AGORA()**: Retornam a data atual e a data/hora atual, respectivamente.
        * `=HOJE()`
        * `=AGORA()`
    * **DIA / MÊS / ANO**: Extraem partes de uma data.
        * `=DIA(A1)`, `=MÊS(A1)`, `=ANO(A1)`
    * **DATA / HORA**: Criam uma data ou hora a partir de seus componentes.
        * `=DATA(2024; 7; 11)`
    * **DATADIF**: Calcula a diferença entre duas datas.
        * `=DATADIF(data_inicial; data_final; "unidade")`
        * **Unidades**: `"y"` (anos), `"m"` (meses), `"d"` (dias), `"ym"` (meses desconsiderando anos), etc.
    * **DIA.DA.SEMANA**: Retorna o dia da semana (1-7).
        * `=DIA.DA.SEMANA(A1; 2)` (2 faz a semana começar na segunda-feira = 1)
    * **DIATRABALHO.INTL**: Calcula a data após um número de dias úteis, especificando feriados e dias de fim de semana.
        * Muito útil para cronogramas.
    """)
    st.markdown("---")

    st.subheader("5.5. Atalhos de Teclado e Dicas de Produtividade")
    st.markdown("""
    * `Ctrl + C / Ctrl + V`: Copiar / Colar
    * `Ctrl + Z / Ctrl + Y`: Desfazer / Refazer
    * `Ctrl + S`: Salvar
    * `Ctrl + B`: Negrito
    * `Ctrl + 1`: Abrir Formatar Células
    * `Ctrl + Setas`: Navegar rapidamente para o fim/início de um bloco de dados.
    * `Ctrl + Shift + Setas`: Selecionar rapidamente blocos de dados.
    * `F2`: Entrar em modo de edição de célula.
    * `F4`: Alternar referências de célula (A1, $A$1, A$1, $A1$) ao digitar a fórmula.
    * **Preenchimento Relâmpago (Flash Fill)**: Comece a digitar um padrão (ex: separar nome e sobrenome), e o Excel pode preencher automaticamente o resto da coluna. (Dados > Preenchimento Relâmpago ou `Ctrl + E`).
    * **Textos para Colunas**: Separe dados em uma célula em várias colunas (Dados > Textos para Colunas). Ótimo para dados importados.
    """)
    st.markdown("---")

    st.subheader("Exercício 5: Limpeza e Análise com Funções Avançadas")
    st.write("Considere a seguinte tabela de RH no Excel. Digite-a exatamente como está:")
    st.code("""
    | ID Func.  | Nome Completo Original | Data Nasc.  | Contato               | Salário | Departamento  |
    |-----------|------------------------|-------------|-----------------------|---------|---------------|
    | F001      |  joao silva            | 15/07/1990  | joao.s@email.com      | 4500    |   Vendas      |
    | F002      | MARIA.COSTA            | 22/02/1985  | (11) 98765-4321       | 6000    |   marketing   |
    | F003      | Pedro G. LIMA          | 03/09/1992  | pedroglima@email.com  | 3800    |  TI           |
    | F004      |   ANA_ROCHA            | 28/04/1998  | anaroch@email.com     | 5200    |  vendas       |
    """)
    st.markdown("""
    1.  **Limpeza de Nomes**: Crie uma coluna "Nome Limpo". Use `ARRUMAR` e `PRI.MAIÚSCULA` para corrigir o "Nome Completo Original".
        * Dica: Para `ANA_ROCHA`, pode ser preciso usar `SUBSTITUIR("_"; " ")` antes de `PRI.MAIÚSCULA`.
    2.  **Validação de Dados**:
        * Na coluna "Salário", aplique uma **Validação de Dados** para permitir apenas valores entre `1000` e `10000`.
        * Na coluna "Departamento", crie uma **Lista Suspensa** com as opções: "Vendas", "Marketing", "TI", "RH". (Atenção para os dados existentes que podem não bater).
    3.  **Formatação Condicional**:
        * Na coluna "Salário", aplique uma **Barra de Dados** para uma visualização rápida.
        * Destaque em **negrito e cor azul** todos os funcionários do departamento "Vendas" (use "Regras de Realce de Células" > "Mais Regras" > "Usar uma fórmula para determinar quais células devem ser formatadas" e a fórmula).
    4.  **Cálculo de Idade**: Crie uma coluna "Idade (Anos)". Use **`DATADIF`** para calcular a idade de cada funcionário com base na "Data Nasc." e a data de hoje (`HOJE()`).
    5.  **Dica**: Congele os painéis na primeira linha e na primeira coluna (`ID Func.`) para facilitar a visualização ao rolar.
    """)
    with st.expander("Verificar Respostas (Sugestão de Fórmulas)"):
        st.markdown("""
        * **Nome Limpo (C2)**: `=PRI.MAIÚSCULA(ARRUMAR(SUBSTITUIR(B2;"_";" ")))`
        * **Validação Salário**: Selecione a coluna Salário. Dados > Validação de Dados > Permitir: Número Inteiro > Dados: entre > Mínimo: 1000, Máximo: 10000.
        * **Validação Departamento**: Selecione a coluna Departamento. Dados > Validação de Dados > Permitir: Lista > Fonte: "Vendas;Marketing;TI;RH".
        * **Formatação Condicional Departamento**: Selecione o intervalo dos dados de nome completo (ex: C2:C5). Página Inicial > Formatação Condicional > Nova Regra > Usar uma fórmula... > Fórmula: `=C2="Vendas"` (ou use `=$F2="Vendas"` se a coluna de Departamento for F). Formate como desejar.
        * **Idade (Anos) (H2)**: `=DATADIF(C2; HOJE(); "y")`
        """)
    st.markdown("---")


def quiz_dicas_produtividade():
    st.header("❓ Quiz: Dicas de Produtividade e Boas Práticas")
    st.write("Verifique seu conhecimento sobre aprimoramento e integridade dos dados!")

    st.subheader("Pergunta 1")
    q1_options = ["Somente altera a cor da fonte.", "Define a formatação da célula para negrito.", "Aplica formatos automaticamente com base em regras definidas.", "Exclui células que não atendem a um critério."]
    q1_answer = st.radio("Qual a principal função da Formatação Condicional?", q1_options, key="q1_dicas")
    if st.button("Verificar Pergunta 1", key="btn_q1_dicas"):
        if q1_answer == "Aplica formatos automaticamente com base em regras definidas.":
            st.success("Correto! 🎉 É uma ferramenta visual poderosa para análise.")
        else:
            st.error("Incorreto. A formatação condicional é dinâmica e baseada em regras.")
    st.markdown("---")

    st.subheader("Pergunta 2")
    q2_options = ["`=HOJE(ANO())`", "`=AGORA()`", "`=DIA(HOJE())`", "`=DATADIF(A1; HOJE(); 'm')`"]
    q2_answer = st.radio("Você quer calcular o número de meses entre uma data de início (em A1) e a data atual. Qual a fórmula mais adequada?", q2_options, key="q2_dicas")
    if st.button("Verificar Pergunta 2", key="btn_q2_dicas"):
        if q2_answer == "`=DATADIF(A1; HOJE(); 'm')`":
            st.success("Correto! 🎉 `DATADIF` é a função ideal para calcular diferenças entre datas.")
        else:
            st.error("Ops! Lembre-se da função específica para calcular a diferença entre datas.")
    st.markdown("---")

    st.subheader("Pergunta 3")
    q3_options = ["`=MAIÚSCULA(A1)`", "`=ARRUMAR(A1)`", "`=PRI.MAIÚSCULA(A1)`", "`=LIMPAR(A1)`"]
    q3_answer = st.radio("Qual função é mais adequada para remover espaços extras no início, fim ou entre palavras de uma célula (A1)?", q3_options, key="q3_dicas")
    if st.button("Verificar Pergunta 3", key="btn_q3_dicas"):
        if q3_answer == "`=ARRUMAR(A1)`":
            st.success("Correto! 🎉 `ARRUMAR` é essencial para a limpeza de dados de texto.")
        else:
            st.error("Incorreto. As outras funções não lidam especificamente com espaços extras.")
    st.markdown("---")


def power_query_modulo():
    st.header("6. 🚀 Desvendando o Power Query: Transformação de Dados")
    st.write("O **Power Query** (também conhecido como **Obter e Transformar Dados**) é uma ferramenta revolucionária do Excel que permite importar, limpar e transformar dados de diversas fontes sem precisar de fórmulas complexas. É um divisor de águas na análise de dados!")

    st.subheader("6.1. O que é e Por que Usar o Power Query?")
    st.markdown("""
    O Power Query é um **motor de ETL (Extract, Transform, Load)** embutido no Excel e em outras ferramentas da Microsoft (como Power BI). Ele automatiza o processo de:
    * **Extrair**: Conectar-se a diversas fontes de dados (arquivos CSV, TXT, Excel, Pastas, Bancos de Dados, Web, etc.).
    * **Transformar**: Limpar, remodelar, combinar e enriquecer os dados (remover duplicatas, renomear colunas, dividir colunas, mesclar tabelas, dinamizar/desdinamizar, etc.).
    * **Carregar**: Levar os dados transformados para uma planilha do Excel ou para o Modelo de Dados.

    **Vantagens:**
    * **Automação**: Uma vez criada a transformação, ela pode ser atualizada com um clique.
    * **Limpeza de Dados**: Padroniza e organiza dados "sujos".
    * **Combinar Dados**: Mescla e anexa tabelas de diferentes fontes facilmente.
    * **Não Destrutivo**: As transformações não alteram a fonte original dos dados.
    * **Curva de Aprendizagem Visual**: Muitas operações são feitas clicando e arrastando, sem necessidade de código complexo (embora ele use a linguagem M por trás).
    """)

    st.subheader("6.2. Conectando e Transformando Dados (Exemplos Práticos)")
    st.write("Vamos ver alguns exemplos de como o Power Query pode facilitar sua vida. Você encontrará as opções do Power Query na guia **Dados** > grupo **Obter e Transformar Dados**.")

    st.markdown("""
    **Exemplo 1: Importar Dados de uma Pasta (Combine Arquivos)**
    Imagine que você recebe relatórios de vendas mensais em arquivos CSV separados, todos na mesma pasta.
    1.  Vá em **Dados** > **Obter Dados** > **De Arquivo** > **De Pasta**.
    2.  Navegue até a pasta que contém seus arquivos CSV.
    3.  Clique em **Combinar e Transformar Dados**.
    4.  O Power Query analisa um dos arquivos como "amostra" e aplica as transformações aos demais. Ele criará uma única tabela combinada.
        * **Transformações Comuns**: Remover colunas desnecessárias, renomear colunas, alterar tipo de dados (Texto para Número, etc.).

    **Exemplo 2: Limpar e Remodelar Dados (Editor do Power Query)**
    Você tem uma lista de produtos onde o `Nome do Produto` e o `Código do Produto` estão na mesma coluna, separados por um hífen.
    1.  Importe seus dados (ex: de uma planilha Excel). Clique na tabela > **Dados** > **Da Tabela/Intervalo**.
    2.  No **Editor do Power Query**:
        * Selecione a coluna.
        * Vá na guia **Transformar** > **Dividir Coluna** > **Por Delimitador** (escolha o hífen).
        * Renomeie as novas colunas.
        * Você também pode usar "Remover Linhas" (duplicatas, vazias), "Preencher" (para dados em hierarquia), "Dinamizar Coluna" (para transformar linhas em colunas e vice-versa).

    **Exemplo 3: Mesclar Tabelas (VLOOKUP do Power Query)**
    Você tem uma tabela de Vendas (com `ID Produto`) e uma tabela de Produtos (com `ID Produto` e `Preço Unitário`). Quer adicionar o `Preço Unitário` na tabela de Vendas.
    1.  Importe ambas as tabelas para o Power Query.
    2.  Na guia **Página Inicial** > **Combinar** > **Mesclar Consultas**.
    3.  Escolha sua tabela principal (Vendas) e a tabela a ser mesclada (Produtos).
    4.  Selecione a coluna comum (`ID Produto`) em ambas as tabelas.
    5.  Escolha o tipo de união (geralmente "Externa Esquerda").
    6.  Uma nova coluna aparecerá. Clique no botão de expansão no cabeçalho dessa nova coluna e selecione `Preço Unitário`.

    Cada passo que você faz no Power Query é gravado como um "Passo Aplicado" (à direita). Você pode editá-los ou excluí-los a qualquer momento.
    """)
    st.markdown("---")

    st.subheader("Exercício 6: Importando e Transformando Dados com Power Query")
    st.write("Este exercício é um pouco diferente, pois você precisa *executá-lo diretamente no Excel* para entender o Power Query. Crie os seguintes arquivos e simule os passos:")

    st.markdown("""
    **Parte A: Consolidar Múltiplos Arquivos CSV**
    1.  Crie uma pasta no seu computador chamada `RelatoriosVendas`.
    2.  Dentro dela, crie 2 arquivos de texto (`.txt`) e salve-os como `.csv` (Salvar como > Tipo: Todos os Arquivos > Nome: `Vendas_Janeiro.csv`, `Vendas_Fevereiro.csv`).
        * **`Vendas_Janeiro.csv`**:
            ```csv
            Data,Produto,Valor
            05/01/2024,Caneta,10.50
            10/01/2024,Lapis,5.20
            ```
        * **`Vendas_Fevereiro.csv`**:
            ```csv
            Data,Produto,Valor
            03/02/2024,Caderno,20.00
            15/02/2024,Caneta,10.50
            ```
    3.  No Excel, vá em **Dados** > **Obter Dados** > **De Arquivo** > **De Pasta**.
    4.  Navegue até a pasta `RelatoriosVendas` e clique em Abrir.
    5.  Na janela que aparece, clique em **Combinar e Transformar Dados**.
    6.  No Editor do Power Query, observe como as duas tabelas foram combinadas.
    7.  Altere o tipo de dados da coluna `Valor` para "Número Decimal" (se não estiver já).
    8.  Clique em **Página Inicial** > **Fechar e Carregar Para...** > **Somente Criar Conexão**. (Isso é importante para a Parte B).

    **Parte B: Mesclando Informações de Produtos**
    1.  No mesmo arquivo Excel, em uma nova planilha, crie a tabela `Produtos` (dados manualmente):
        ```
        | Produto | Categoria | Preço Unitário |
        |---------|-----------|----------------|
        | Caneta  | Papelaria | 2.50           |
        | Lapis   | Papelaria | 1.00           |
        | Caderno | Escolar   | 15.00          |
        ```
    2.  Selecione esta tabela `Produtos`. Vá em **Dados** > **Da Tabela/Intervalo**. O Editor do Power Query abrirá com a tabela `Produtos`. Clique em **Fechar e Carregar Para...** > **Somente Criar Conexão**.
    3.  Agora, volte para o Editor do Power Query (Dados > Obter Dados > Iniciar Editor do Power Query...).
    4.  Selecione a consulta que você criou na Parte A (deve ter um nome como `Vendas_Combinado`).
    5.  Vá em **Página Inicial** > **Combinar** > **Mesclar Consultas**.
    6.  Na caixa de diálogo 'Mesclar':
        * Escolha sua consulta `Vendas_Combinado` como a primeira tabela.
        * Escolha a consulta `Produtos` como a segunda tabela.
        * Selecione a coluna `Produto` em ambas as tabelas (ela será a chave para a união).
        * Deixe o Tipo de Junção como "Externa Esquerda (Todas da primeira, correspondentes da segunda)". Clique em OK.
    7.  Uma nova coluna com o nome da segunda tabela aparecerá. Clique no ícone de duas setas no cabeçalho dela e desmarque "Usar nome da coluna original como prefixo", selecione apenas as colunas `Categoria` e `Preço Unitário`.
    8.  Clique em **Fechar e Carregar**.

    Você terá uma única tabela no Excel com as vendas combinadas de Janeiro e Fevereiro, e agora, com a Categoria e o Preço Unitário de cada produto! Isso é o Power Query em ação!
    """)
    st.markdown("---")


def quiz_power_query():
    st.header("❓ Quiz: Desvendando o Power Query")
    st.write("Vamos ver o que você aprendeu sobre essa ferramenta poderosa!")

    st.subheader("Pergunta 1")
    q1_options = ["É uma ferramenta para criar gráficos.", "É uma linguagem de programação VBA.", "É um motor de ETL para importar, limpar e transformar dados.", "Serve apenas para renomear colunas."]
    q1_answer = st.radio("Qual a principal função do Power Query no Excel?", q1_options, key="q1_pq")
    if st.button("Verificar Pergunta 1", key="btn_q1_pq"):
        if q1_answer == "É um motor de ETL para importar, limpar e transformar dados.":
            st.success("Correto! 🎉 O Power Query simplifica o trabalho com dados brutos.")
        else:
            st.error("Incorreto. Lembre-se do foco principal do Power Query: extração, transformação e carregamento.")
    st.markdown("---")

    st.subheader("Pergunta 2")
    q2_options = ["O `PROCV` é melhor para combinar dados grandes.", "O Power Query automatiza o processo, enquanto o `PROCV` precisa ser arrastado.", "O Power Query só funciona com arquivos CSV.", "O `PROCV` não permite limpeza de dados."]
    q2_answer = st.radio("Qual a principal vantagem de usar o Power Query para combinar dados (mesclar tabelas) em vez de múltiplos `PROCV`?", q2_options, key="q2_pq")
    if st.button("Verificar Pergunta 2", key="btn_q2_pq"):
        if q2_answer == "O Power Query automatiza o processo, enquanto o `PROCV` precisa ser arrastado.":
            st.success("Correto! 🎉 A automação e a capacidade de lidar com grandes volumes de dados são grandes vantagens.")
        else:
            st.error("Ops! Pense na escalabilidade e repetição de tarefas. O Power Query brilha aí.")
    st.markdown("---")


def projeto_final():
    st.header("7. 🏆 Projeto Final: Construindo um Dashboard Interativo de Vendas")
    st.write("Chegou a hora de colocar todo o seu conhecimento em prática! Neste projeto, você vai construir um dashboard de vendas completo, usando todas as ferramentas e técnicas que aprendeu.")

    st.subheader("7.1. Cenário e Dados")
    st.markdown("""
    Imagine que você é o analista de vendas de uma empresa e precisa criar um painel que mostre o desempenho de vendas por produto, vendedor e região ao longo do tempo.

    **Baixe ou crie a seguinte base de dados de vendas (idealmente em uma planilha chamada 'DadosBrutos'):**

    **`dados_vendas.xlsx`** (Exemplo de estrutura, preencha com ~50-100 linhas de dados variados)

    | ID Venda | Data Venda | Vendedor | Região | Produto | Categoria | Quantidade | Preço Unitário |
    |----------|------------|----------|--------|---------|-----------|------------|----------------|
    | V001     | 01/01/2024 | Ana Silva| Sudeste| Caneta  | Papelaria | 10         | 2.50           |
    | V002     | 05/01/2024 | João Fdez| Norte  | Caderno | Papelaria | 5          | 12.00          |
    | V003     | 10/01/2024 | Ana Silva| Sudeste| Mouse   | Eletrônicos| 2          | 50.00          |
    | ... (mais dados variados) ...                                                                   |
    """)

    st.subheader("7.2. Passos para o Dashboard")
    st.markdown("""
    Siga estes passos para construir seu dashboard:

    1.  **Preparação dos Dados (Limpeza e Colunas Calculadas):**
        * Na planilha `DadosBrutos`, adicione uma coluna **`Valor Total`** (`Quantidade` * `Preço Unitário`).
        * Adicione uma coluna **`Mês da Venda`** (`=MÊS(Data Venda)`).
        * Adicione uma coluna **`Ano da Venda`** (`=ANO(Data Venda)`).
        * **Opcional/Avançado**: Use o **Power Query** para importar esses dados, fazer as colunas calculadas e garantir a limpeza (ex: `ARRUMAR` nomes, `MAIÚSCULA` em categorias, etc.). Carregue para uma **conexão apenas**.

    2.  **Criação das Tabelas Dinâmicas:**
        * Crie uma **Nova Planilha** e chame-a de `Dashboard`.
        * Na planilha `DadosBrutos`, selecione seus dados (incluindo as novas colunas).
        * Vá em **Inserir** > **Tabela Dinâmica**. Coloque-a na planilha `Dashboard`.
        * Crie as seguintes Tabelas Dinâmicas nesta aba `Dashboard` (pode ser uma do lado da outra):
            * **TD1: Vendas por Categoria**: `Categoria` em Linhas, `Soma de Valor Total` em Valores.
            * **TD2: Vendas por Vendedor**: `Vendedor` em Linhas, `Soma de Valor Total` em Valores.
            * **TD3: Vendas por Região e Mês**: `Região` em Linhas, `Mês da Venda` em Colunas, `Soma de Valor Total` em Valores.
            * **TD4: Total Geral de Vendas**: Apenas `Soma de Valor Total` em Valores (resultado único).

    3.  **Criação dos Gráficos Dinâmicos:**
        * A partir de cada Tabela Dinâmica, crie um **Gráfico Dinâmico** apropriado:
            * TD1: **Gráfico de Pizza** (Vendas por Categoria)
            * TD2: **Gráfico de Barras** (Vendas por Vendedor)
            * TD3: **Gráfico de Linhas** (Vendas por Região ao longo dos meses - ou Colunas Agrupadas)
        * Posicione os gráficos de forma organizada no seu `Dashboard`.

    4.  **Adicionando Interatividade:**
        * Insira **Segmentações de Dados (Slicers)** para `Região`, `Vendedor` e `Categoria`.
        * Insira uma **Linha do Tempo (Timeline)** para `Data Venda`.
        * **Conecte todos os Slicers e a Linha do Tempo a TODAS as Tabelas Dinâmicas** (clique no Slicer > **Opções** > **Conexões de Relatório...**). Isso fará com que um filtro em um slicer atualize tudo.

    5.  **Design e Formatação:**
        * Remova os botões de campo dos gráficos (clique no gráfico > **Analisar Gráfico Dinâmico** > **Botões de Campo** > **Ocultar Todos**).
        * Ajuste tamanhos e posições dos gráficos e slicers.
        * Adicione um título claro ao dashboard.
        * Oculte as linhas de grade da planilha `Dashboard` (Exibir > Linhas de Grade).
        * Formate os valores nos gráficos e tabelas para moeda.

    **O Resultado:** Você terá um dashboard interativo que permite filtrar as vendas por vendedor, região, categoria e período de tempo, visualizando os resultados instantaneamente nos gráficos!
    """)
    st.subheader("7.3. Desafios Adicionais (Para Experts!)")
    st.markdown("""
    * **KPIs no Dashboard**: Crie células que mostram KPIs (Key Performance Indicators) como:
        * **Total de Vendas no Período Selecionado** (conectado aos slicers).
        * **Número de Vendas Realizadas**.
        * **Média de Vendas por Transação**.
        * *Dica*: Use as funções `GETPIVOTDATA` ou simplesmente referencie as células das Tabelas Dinâmicas ou faça novas TDs ocultas para os KPIs.
    * **Formatação Condicional Avançada**: Use formatação condicional nos KPIs para indicar se estão acima/abaixo de uma meta com cores.
    * **Validação de Dados para Parâmetros**: Se você tiver metas fixas, use validação de dados para criar listas de metas.
    * **Proteção da Planilha**: Proteja sua planilha `Dashboard` para evitar alterações acidentais nas fórmulas e objetos (Revisar > Proteger Planilha).
    """)
    st.info("Parabéns! Você chegou ao final do curso. A prática leva à perfeição. Continue explorando e aplicando esses conhecimentos!")
    st.markdown("---")


if __name__ == "__main__":
    curso_excel()
