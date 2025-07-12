import streamlit as st
import random
import time

# --- Configurações da Página ---
st.set_page_config(
    page_title="Curso de Violão Interativo 2.0",
    page_icon="🎸",
    layout="centered"
)

# --- Dados dos Acordes (Diagramas Simplificados) ---
ACORDES = {
    "C (Dó Maior)": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/C_Major_guitar_chord_diagram.svg/1200px-C_Major_guitar_chord_diagram.svg.png",
        "dedos": "3-2-0-1-0",
        "observacoes": "Um dos primeiros acordes, fundamental para muitas músicas.",
        "audio_url": "https://www.musicca.com/api/chords/C-major.mp3" # Exemplo de áudio online
    },
    "G (Sol Maior)": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/G_Major_guitar_chord_diagram.svg/1200px-G_Major_guitar_chord_diagram.svg.png",
        "dedos": "3-2-0-0-0-3",
        "observacoes": "Ótimo para começar a fazer a transição entre acordes. Use o dedo 3 na 6ª corda e o 4 na 1ª.",
        "audio_url": "https://www.musicca.com/api/chords/G-major.mp3"
    },
    "D (Ré Maior)": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/D_Major_guitar_chord_diagram.svg/1200px-D_Major_guitar_chord_diagram.svg.png",
        "dedos": "X-X-0-2-3-2",
        "observacoes": "Um acorde de sonoridade aberta, cuidado com as cordas X (não tocar).",
        "audio_url": "https://www.musicca.com/api/chords/D-major.mp3"
    },
    "Em (Mi Menor)": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/E_minor_guitar_chord_diagram.svg/1200px-E_minor_guitar_chord_diagram.svg.png",
        "dedos": "0-2-2-0-0-0",
        "observacoes": "Um acorde menor fácil de montar, use os dedos 2 e 3.",
        "audio_url": "https://www.musicca.com/api/chords/Em-minor.mp3"
    },
    "Am (Lá Menor)": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/A_minor_guitar_chord_diagram.svg/1200px-A_minor_guitar_chord_diagram.svg.png",
        "dedos": "X-0-2-2-1-0",
        "observacoes": "Outro acorde menor essencial, similar ao C, mas com a corda Ré (4ª) alterada.",
        "audio_url": "https://www.musicca.com/api/chords/Am-minor.mp3"
    },
    "E (Mi Maior)": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/E_Major_guitar_chord_diagram.svg/1200px-E_Major_guitar_chord_diagram.svg.png",
        "dedos": "0-2-2-1-0-0",
        "observacoes": "A partir do Em, basta adicionar o dedo 1 na 3ª corda (Sol).",
        "audio_url": "https://www.musicca.com/api/chords/E-major.mp3"
    },
    "Dm (Ré Menor)": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/D_minor_guitar_chord_diagram.svg/1200px-D_minor_guitar_chord_diagram.svg.png",
        "dedos": "X-X-0-2-3-1",
        "observacoes": "Um dos acordes menores mais importantes. Cuidado com o dedo 1 na 1ª corda.",
        "audio_url": "https://www.musicca.com/api/chords/Dm-minor.mp3"
    },
    "F (Fá Maior) - Simplificado": {
        "diagrama_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/F_Major_guitar_chord_diagram_barre_alternative.svg/1200px-F_Major_guitar_chord_diagram_barre_alternative.svg.png",
        "dedos": "X-X-3-2-1-1",
        "observacoes": "Versão simplificada sem pestana. Ótimo para introdução ao F.",
        "audio_url": "https://www.musicca.com/api/chords/F-major.mp3"
    }
}

# --- Funções do Curso ---

def introducao():
    st.header("Seu Primeiro Contato com o Violão 🎸")
    st.write("""
    Bem-vindo(a) ao seu curso interativo de violão! Se você sempre quis tocar, mas não sabia por onde começar, este é o lugar certo. Vamos desmistificar o violão e te dar as ferramentas para tocar suas primeiras músicas.

    **O que você vai aprender aqui:**
    * **Estrutura do Violão:** Conhecer as partes do seu instrumento.
    * **Como Segurar e Afinar:** A postura correta e a importância da afinação.
    * **Entendendo os Acordes:** Como ler diagramas e montar acordes.
    * **Seus Primeiros Acordes:** Pratique os acordes essenciais para iniciantes.
    * **Ritmo Básico:** Comece a tocar seus primeiros ritmos.
    * **Metrônomo Interativo:** Para te ajudar a manter o tempo.
    * **Exercícios de Troca:** Para praticar a transição entre os acordes.

    Pegue seu violão, um afinador (aplicativo ou físico) e vamos lá!
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Classical_guitar_on_a_stand.jpg/1280px-Classical_guitar_on_a_stand.jpg", caption="Pronto para começar?", use_column_width=True)
    st.markdown("---")

def estrutura_afinacao():
    st.header("2. Conhecendo o Violão e Afinando 🧐")

    with st.expander("2.1. Partes do Violão", expanded=True):
        st.write("""
        Antes de tocar, é importante conhecer seu instrumento. O violão é dividido em três partes principais:
        * **Corpo:** A parte grande e oca que ressoa o som.
            * **Boca:** O buraco no corpo que amplifica o som.
            * **Cavalete (ponte):** Onde as cordas são presas no corpo.
        * **Braço:** A parte longa onde você posiciona os dedos para formar as notas e acordes.
            * **Trastes:** As barrinhas de metal que dividem o braço em seções.
            * **Casas:** As seções entre os trastes, onde você pressiona as cordas.
            * **Pestana:** A barrinha no início do braço, logo abaixo do cabeçote.
        * **Cabeçote (mão):** A ponta do violão onde ficam as tarraxas.
            * **Tarraxas:** As peças que você gira para apertar ou soltar as cordas, afinando o violão.

        As cordas são contadas de baixo para cima, sendo a mais fina a **1ª corda (Mi agudo)** e a mais grossa a **6ª corda (Mi grave)**.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Diagram_of_a_guitar_neck_showing_strings_and_frets.svg/1024px-Diagram_of_a_guitar_neck_showing_strings_and_frets.svg.png", caption="Partes do Braço e Cordas", use_column_width=True)

    with st.expander("2.2. Como Segurar o Violão", expanded=True):
        st.write("""
        A **postura correta** é fundamental para o conforto e para evitar lesões.
        * **Sente-se:** Use uma cadeira sem braços e sente-se ereto(a).
        * **Apoie:** Para destros, apoie o corpo do violão na coxa direita. Para canhotos, na coxa esquerda.
        * **Braço Esquerdo (Mão da digitação):** O cotovelo deve estar relaxado, e a mão deve ter liberdade para se mover pelo braço.
        * **Braço Direito (Mão da palhetada/batida):** O antebraço repousa sobre o corpo do violão, perto da boca. Mantenha o pulso flexível.
        """)
        st.info("💡 **Dica:** Procure vídeos online sobre 'postura correta violão' para visualizar melhor.")

    with st.expander("2.3. Afinamento do Violão", expanded=True):
        st.write("""
        Um violão desafinado soa mal, não importa o quão bem você toque. A afinação padrão do violão (de cima para baixo, da corda mais grossa para a mais fina) é **E-A-D-G-B-E** (Mi - Lá - Ré - Sol - Si - Mi).

        **Como afinar:**
        1.  **Use um Afinador:** Recomendo um aplicativo de afinador no seu celular (ex: 'GuitarTuna', 'Fender Play') ou um afinador clip-on.
        2.  **Toque uma corda:** Toque a 6ª corda (a mais grossa, Mi grave). O afinador mostrará se ela está muito aguda ou muito grave.
        3.  **Gire a tarraxa:** Gire a tarraxa correspondente à corda para apertar (som mais agudo) ou soltar (som mais grave) até o afinador indicar que a nota está no centro, verde.
        4.  **Repita:** Faça isso para todas as cordas:
            * **6ª corda:** E (Mi)
            * **5ª corda:** A (Lá)
            * **4ª corda:** D (Ré)
            * **3ª corda:** G (Sol)
            * **2ª corda:** B (Si)
            * **1ª corda:** E (Mi)

        É normal que o violão desafine um pouco no início, especialmente com cordas novas. Afine-o sempre antes de praticar!
        """)
        st.video("https://www.youtube.com/watch?v=gT8-F6aA9L8", help="Assista a um vídeo rápido sobre afinação de violão.") # Link real de afinação
    st.markdown("---")

def entendendo_acordes():
    st.header("3. Entendendo os Acordes e Diagramas 📖")
    st.write("""
    Um **acorde** é um conjunto de três ou mais notas tocadas simultaneamente que soam harmoniosas. Os **diagramas de acordes** são mapas visuais que mostram onde você deve posicionar seus dedos no braço do violão.

    ### **Como Ler um Diagrama de Acorde:**
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://www.guitartricks.com/img/chords/basic-chord-diagram.png", caption="Exemplo de Diagrama de Acorde", use_column_width=True)
    with col2:
        st.write("""
        1.  **Linhas Verticais:** Representam as **cordas** do violão.
            * A linha mais à esquerda é a 6ª corda (Mi grave).
            * A linha mais à direita é a 1ª corda (Mi agudo).
        2.  **Linhas Horizontais:** Representam os **trastes** do violão.
            * A linha superior (mais grossa) geralmente representa a pestana ou o primeiro traste.
            * Se houver um número ao lado do diagrama, ele indica qual traste o diagrama representa (ex: '3fr' significa 3º traste).
        3.  **Círculos Pretos (ou Bolinhas):** Indicam onde você deve **pressionar** a corda com a ponta dos dedos.
            * Se a bolinha estiver **vazia (branca)** no topo, a corda deve ser tocada **solta (0)**.
            * Se houver um **'X'** em cima da corda, ela **não deve ser tocada**.
        4.  **Números dentro dos Círculos ou Abaixo:** Indicam qual **dedo** você deve usar para pressionar aquela nota:
            * **1 = Indicador**
            * **2 = Médio**
            * **3 = Anelar**
            * **4 = Mínimo (Mindinho)**
        """)

    st.write("""
    ### **Dica de Ouro:**
    * Use a **ponta dos dedos** para pressionar as cordas, logo atrás do traste (mas não em cima do traste!), para evitar que o som fique abafado.
    * Pressione com **força suficiente** para que o som saia limpo.
    * Certifique-se de que nenhum dedo está "morto" (tocando acidentalmente uma corda adjacente e abafando-a).
    """)

    st.markdown("---")

def primeiros_acordes():
    st.header("4. Seus Primeiros Acordes Essenciais ✨")
    st.write("""
    Vamos aprender e praticar os acordes mais fundamentais. Eles são a base para milhares de músicas! Clique nos acordes abaixo para ver o diagrama, a posição dos dedos e **ouvir o som do acorde**.

    **Acordes que vamos aprender:**
    """)

    # Exibe os nomes dos acordes disponíveis em colunas
    num_cols = 4
    cols = st.columns(num_cols)
    acorde_names = list(ACORDES.keys())
    
    # Gerencia o estado do acorde selecionado
    if 'acorde_selecionado' not in st.session_state:
        st.session_state.acorde_selecionado = None

    for i, nome_acorde in enumerate(acorde_names):
        with cols[i % num_cols]:
            if st.button(nome_acorde, key=f"btn_acorde_{nome_acorde}"):
                st.session_state.acorde_selecionado = nome_acorde
    
    st.markdown("---")

    if st.session_state.acorde_selecionado:
        acorde_data = ACORDES[st.session_state.acorde_selecionado]
        st.subheader(f"Acorde de {st.session_state.acorde_selecionado}")
        
        col_img, col_info = st.columns(2)
        with col_img:
            st.image(acorde_data["diagrama_url"], caption=f"Diagrama de {st.session_state.acorde_selecionado}", width=300)
        with col_info:
            st.info(f"**Posição dos Dedos (da 6ª para a 1ª corda, X=não tocar, 0=solta):** `{acorde_data['dedos']}`")
            st.write(f"**Observações:** {acorde_data['observacoes']}")
            
            # Botão para tocar o áudio
            if acorde_data.get("audio_url"):
                st.audio(acorde_data["audio_url"], format="audio/mp3", start_time=0)
            else:
                st.warning("Áudio não disponível para este acorde.")

        st.markdown("---")
        st.write("### **Dica de Prática para o Acorde Atual:**")
        st.write("1.  **Toque corda por corda:** Pressione o acorde e toque cada corda individualmente para garantir que o som esteja limpo e alto.")
        st.write("2.  **Ajuste os dedos:** Se alguma corda estiver abafada, ajuste a posição e a força dos seus dedos. Certifique-se de que a ponta do dedo está firme na corda, e que os dedos estão curvos (não deitados).")
        st.write("3.  **Repita:** Toque o acorde inteiro, solte, monte novamente e toque. Faça isso várias vezes para memorizar a forma.")

    st.markdown("---")

def ritmo_basico():
    st.header("5. Seu Primeiro Ritmo: Batida Básica para Iniciantes 🎵")
    st.write("""
    Dominar a batida é tão importante quanto montar os acordes. Vamos aprender um ritmo super simples que serve para muitas músicas.

    ### **A Batida (4/4):**
    Imagine um balanço de "baixo-baixo-cima-cima-baixo".
    * **Baixo ( ↓ ):** Com a mão que palheta, bata as cordas para baixo.
    * **Cima ( ↑ ):** Com a mão que palheta, bata as cordas para cima.

    **Ritmo:** ↓ ↓ ↑ ↑ ↓

    Tente fazer este movimento enquanto conta: "UM (↓) DOIS (↓) E (↑) TRÊS (↑) QUATRO (↓)".
    """)

    st.warning("⚠️ **Importante:** Pratique este ritmo lentamente no começo. Use um metrônomo (aplicativos ou online) para manter o tempo constante.")

    st.write("### **Exemplo Visual do Padrão da Batida:**")
    st.markdown("""
    ```
    1    2    &    3    4
    ↓    ↓    ↑    ↑    ↓
    (sempre para baixo no 1)
    ```
    """)
    st.write("""
    1.  **Mão Livre:** Comece praticando o movimento da batida com a mão livre, sem segurar o violão. Sinta o movimento do pulso.
    2.  **Mão Silenciada:** Apoie a mão dos acordes levemente sobre as cordas para silenciá-las e pratique a batida.
    3.  **Com Acordes:** Escolha um acorde fácil (como Em ou C) e pratique a batida. Quando se sentir confortável, tente trocar de acorde durante a batida (ex: Em por duas vezes, depois C por duas vezes).

    **Vídeo de Apoio (Exemplo de Batida Básica):**
    """)
    st.video("https://www.youtube.com/watch?v=Jb7D0o-pA4Q", help="Vídeo com demonstração de batida básica para violão.")

    st.markdown("---")

def metronomo_interativo():
    st.header("6. Metrônomo Interativo ⏱️")
    st.write("""
    Um **metrônomo** é uma ferramenta essencial para qualquer músico. Ele ajuda a desenvolver o senso de ritmo e a manter o tempo constante. Use este metrônomo simples para praticar seus acordes e batidas!
    """)

    # Inicializa o estado do metrônomo
    if 'metronomo_rodando' not in st.session_state:
        st.session_state.metronomo_rodando = False
    if 'bpm' not in st.session_state:
        st.session_state.bpm = 60

    st.session_state.bpm = st.slider("Selecione o BPM (Batidas por Minuto):", min_value=40, max_value=180, value=st.session_state.bpm, step=5)
    
    col_start, col_stop = st.columns(2)
    with col_start:
        if st.button("Iniciar Metrônomo", key="start_metronomo"):
            st.session_state.metronomo_rodando = True
            st.experimental_rerun() # Reinicia para o loop do metrônomo

    with col_stop:
        if st.button("Parar Metrônomo", key="stop_metronomo"):
            st.session_state.metronomo_rodando = False
            st.experimental_rerun() # Reinicia para parar o loop

    if st.session_state.metronomo_rodando:
        intervalo = 60 / st.session_state.bpm # Tempo em segundos entre as batidas
        placeholder_batida = st.empty()
        
        st.warning(f"Metrônomo rodando a {st.session_state.bpm} BPM. Clique em 'Parar Metrônomo' para pausar.")
        
        # Loop do metrônomo (Streamlit não roda loops infinitos no servidor)
        # Este é um loop "hacky" para Streamlit. Em produção, um backend seria melhor.
        while st.session_state.metronomo_rodando:
            placeholder_batida.write(f"**BATE!** 🥁 (BPM: {st.session_state.bpm})")
            time.sleep(intervalo)
            placeholder_batida.write("") # Limpa a mensagem entre as batidas
            time.sleep(intervalo * 0.1) # Pequena pausa para a mensagem sumir antes de reaparecer
            if not st.session_state.metronomo_rodando: # Checa se foi parado no meio
                break
        placeholder_batida.write("Metrônomo parado.")
    else:
        st.info("Metrônomo pronto para ser iniciado.")

    st.markdown("---")

def exercicios_troca_acordes():
    st.header("7. Exercícios de Troca de Acordes 💪")
    st.write("""
    A maior dificuldade para iniciantes é a **troca fluida entre os acordes**. Vamos praticar algumas sequências comuns. O objetivo é fazer a transição de um acorde para o outro no tempo, com o mínimo de interrupção no som.
    """)

    sequencias = {
        "C para G": ["C (Dó Maior)", "G (Sol Maior)"],
        "Em para C": ["Em (Mi Menor)", "C (Dó Maior)"],
        "Am para Dm": ["Am (Lá Menor)", "Dm (Ré Menor)"],
        "G para D para Em para C (Prog. Pop)": ["G (Sol Maior)", "D (Ré Maior)", "Em (Mi Menor)", "C (Dó Maior)"]
    }

    st.subheader("Escolha uma sequência para praticar:")
    sequencia_selecionada = st.selectbox(
        "Qual sequência você quer praticar?",
        list(sequencias.keys()),
        key="sequencia_select"
    )

    if sequencia_selecionada:
        acordes_na_sequencia = sequencias[sequencia_selecionada]
        st.write(f"Você escolheu a sequência: **{' → '.join(acordes_na_sequencia)}**")
        st.write("---")
        
        st.subheader("Como Praticar:")
        st.write("1.  **Lentamente:** Comece muito devagar. Não se preocupe com a velocidade, mas sim com a clareza da transição.")
        st.write("2.  **Um por um:** Monte o primeiro acorde, toque-o. Depois, com a mão direita parada, monte o segundo acorde. Toque-o.")
        st.write("3.  **Movimento Mínimo:** Tente mover seus dedos o mínimo possível. Às vezes, um dedo pode servir de pivô ou deslizar para a próxima posição.")
        st.write("4.  **Use o Metrônomo:** Quando se sentir um pouco mais confortável, use o metrônomo (na seção anterior) para tentar trocar de acorde a cada 2 ou 4 batidas, por exemplo.")

        st.subheader("Diagramas da Sequência:")
        cols_diagramas = st.columns(len(acordes_na_sequencia))
        for i, acorde_nome in enumerate(acordes_na_sequencia):
            acorde_data = ACORDES.get(acorde_nome)
            if acorde_data:
                with cols_diagramas[i]:
                    st.image(acorde_data["diagrama_url"], caption=acorde_nome, width=150)
                    if acorde_data.get("audio_url"):
                         st.audio(acorde_data["audio_url"], format="audio/mp3", start_time=0)
            else:
                with cols_diagramas[i]:
                    st.warning(f"Diagrama não encontrado para {acorde_nome}")
        
        st.markdown("---")
        st.subheader("Dica para troca entre C e G (exemplo):")
        st.write("""
        Para ir de **C** para **G**, você notará que o dedo **3** (anelAR) do C (na 5ª corda) pode se mover para a **6ª corda** para formar o G. O dedo **1** (indicador) e **2** (médio) do C podem se mover para a 5ª e 6ª corda (respectivamente) no G. Tente visualizar e praticar esse movimento de "pivotar" e reposicionar.
        """)
        
        st.write("### **Exercício Guiado de Transição (Simulado)**")
        st.write("Pressione o botão para praticar a troca de acordes no tempo. Use o metrônomo da seção anterior para referência.")

        if 'acorde_idx' not in st.session_state:
            st.session_state.acorde_idx = 0
            st.session_state.exercicio_rodando = False

        if st.button("Iniciar Exercício de Troca", key="start_troca"):
            st.session_state.exercicio_rodando = True
            st.session_state.acorde_idx = 0
            # st.experimental_rerun()

        if st.session_state.exercicio_rodando:
            placeholder_exercicio = st.empty()
            
            # Simula a troca de acordes
            for _ in range(len(acordes_na_sequencia) * 2): # Repete a sequência duas vezes
                current_acorde_name = acordes_na_sequencia[st.session_state.acorde_idx % len(acordes_na_sequencia)]
                placeholder_exercicio.info(f"**Monte o acorde:** **{current_acorde_name}**")
                # Opcional: tocar o áudio do acorde atual
                if ACORDES.get(current_acorde_name, {}).get("audio_url"):
                    st.audio(ACORDES[current_acorde_name]["audio_url"], format="audio/mp3", start_time=0, loop=False)
                
                time.sleep(2) # Tempo para montar o acorde e tocar
                
                if not st.session_state.exercicio_rodando: # Permite parar no meio
                    break

                st.session_state.acorde_idx += 1
                if st.session_state.acorde_idx >= len(acordes_na_sequencia) * 2: # Para o loop após 2 repetições da sequência
                     st.session_state.exercicio_rodando = False

            if st.session_state.exercicio_rodando: # Se o loop terminou naturalmente
                st.session_state.exercicio_rodando = False
                placeholder_exercicio.success("Exercício de troca concluído para esta sequência!")
            
            if st.button("Parar Exercício", key="stop_troca"):
                st.session_state.exercicio_rodando = False
                st.experimental_rerun()
            
    st.markdown("---")

def quiz_de_violao():
    st.header("8. Quiz do Violão: Teste Seus Conhecimentos! 🧠")
    st.write("Responda às perguntas para fixar o que você aprendeu. Boa sorte!")

    questoes = [
        {
            "pergunta": "Qual corda é a mais fina do violão?",
            "opcoes": ["6ª corda (Mi grave)", "1ª corda (Mi agudo)", "3ª corda (Sol)", "5ª corda (Lá)"],
            "resposta_correta": "1ª corda (Mi agudo)"
        },
        {
            "pergunta": "O que um 'X' em cima de uma corda no diagrama de acorde significa?",
            "opcoes": ["Tocar a corda solta", "Pressionar a corda com o dedo mínimo", "Não tocar a corda", "Tocar a corda com a palheta"],
            "resposta_correta": "Não tocar a corda"
        },
        {
            "pergunta": "Qual dedo é representado pelo número '1' em um diagrama de acorde?",
            "opcoes": ["Mindinho", "Anelar", "Médio", "Indicador"],
            "resposta_correta": "Indicador"
        },
        {
            "pergunta": "A afinação padrão do violão (de cima para baixo) começa com qual nota?",
            "opcoes": ["Lá (A)", "Ré (D)", "Mi (E)", "Sol (G)"],
            "resposta_correta": "Mi (E)"
        },
        {
            "pergunta": "Qual é a principal vantagem de usar um metrônomo?",
            "opcoes": ["Fazer o violão soar mais alto", "Manter a afinação do violão", "Ajudar a desenvolver o senso de ritmo e tempo", "Limpar as cordas do violão"],
            "resposta_correta": "Ajudar a desenvolver o senso de ritmo e tempo"
        }
    ]

    if 'quiz_pontuacao' not in st.session_state:
        st.session_state.quiz_pontuacao = 0
    if 'quiz_respostas_usuario' not in st.session_state:
        st.session_state.quiz_respostas_usuario = {}
    if 'quiz_finalizado' not in st.session_state:
        st.session_state.quiz_finalizado = False

    if st.session_state.quiz_finalizado:
        st.subheader("Resultados do Quiz:")
        for i, q in enumerate(questoes):
            resposta_usuario = st.session_state.quiz_respostas_usuario.get(i)
            if resposta_usuario == q["resposta_correta"]:
                st.success(f"Questão {i+1}: Correta! ✅")
            else:
                st.error(f"Questão {i+1}: Incorreta. ❌ Sua resposta: '{resposta_usuario}'. Resposta correta: '{q['resposta_correta']}'.")
        
        st.markdown(f"### Sua Pontuação: {st.session_state.quiz_pontuacao} de {len(questoes)}")
        if st.session_state.quiz_pontuacao == len(questoes):
            st.balloons()
            st.success("Parabéns! Você acertou todas as questões!")
        elif st.session_state.quiz_pontuacao > len(questoes) / 2:
            st.info("Muito bom! Continue praticando!")
        else:
            st.warning("Continue estudando! Você está no caminho certo.")
        
        if st.button("Tentar Novamente", key="reset_quiz"):
            st.session_state.quiz_finalizado = False
            st.session_state.quiz_pontuacao = 0
            st.session_state.quiz_respostas_usuario = {}
            st.experimental_rerun()
    else:
        for i, q in enumerate(questoes):
            st.subheader(f"Questão {i+1}:")
            st.write(q["pergunta"])
            
            resposta_selecionada = st.radio(
                "Selecione sua resposta:",
                q["opcoes"],
                key=f"questao_{i}_quiz" # Usar key diferente para evitar conflitos
            )
            st.session_state.quiz_respostas_usuario[i] = resposta_selecionada

        if st.button("Finalizar Quiz", key="submit_quiz"):
            st.session_state.quiz_pontuacao = 0
            for i, q in enumerate(questoes):
                if st.session_state.quiz_respostas_usuario.get(i) == q["resposta_correta"]:
                    st.session_state.quiz_pontuacao += 1
            st.session_state.quiz_finalizado = True
            st.experimental_rerun()

    st.markdown("---")

def conclusao():
    st.header("Parabéns! Sua Jornada Começou! 🎉")
    st.write("""
    Você chegou ao final do nosso primeiro módulo! Ter passado por todos esses conceitos e praticado os primeiros acordes e ritmos já te coloca à frente de muitos iniciantes.
    
    **Lembre-se:**
    * **Consistência é Chave:** Pratique um pouco todos os dias, mesmo que seja por 15-20 minutos.
    * **Paciência:** É normal sentir dor nos dedos no início e ter dificuldade com as transições. Com o tempo, seus dedos se fortalecerão.
    * **Divirta-se!** Toque as músicas que você ama. Isso manterá sua motivação lá em cima.
    
    Sugestões de próximos passos:
    1.  **Aprenda mais acordes:** Explore outros acordes maiores e menores, pestanas, e acordes com sétima.
    2.  **Músicas Simplificadas:** Procure cifras de músicas "fáceis para iniciantes" na internet (ex: "Acordes Fáceis Cifra Club").
    3.  **Aulas Online:** Considere fazer aulas com um professor para feedback personalizado.
    4.  **Teoria Musical Básica:** Entender um pouco de teoria (escalas, formação de acordes) pode acelerar seu aprendizado.
    
    Continue explorando o mundo da música e do violão! O caminho é longo, mas recompensador.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Hands_Playing_Acoustic_Guitar.jpg", caption="Continue praticando!", use_column_width=True)


# --- Estrutura Principal do Aplicativo Streamlit ---
if __name__ == "__main__":
    st.title("🎼 Curso Prático de Violão para Iniciantes")
    st.markdown("Um guia interativo para você dar os primeiros passos com seu violão.")

    st.sidebar.title("Navegação do Curso")
    modulo_selecionado = st.sidebar.radio(
        "Selecione um tópico:",
        ("Introdução",
         "2. Conhecendo o Violão e Afinando",
         "3. Entendendo os Acordes e Diagramas",
         "4. Seus Primeiros Acordes Essenciais",
         "5. Seu Primeiro Ritmo: Batida Básica",
         "6. Metrônomo Interativo",
         "7. Exercícios de Troca de Acordes",
         "8. Quiz do Violão",
         "Conclusão e Próximos Passos"),
        key="violao_navigation"
    )

    st.markdown("---") # Linha divisória para separar a navegação do conteúdo

    # Renderiza a função do módulo selecionado
    if modulo_selecionado == "Introdução":
        introducao()
    elif modulo_selecionado == "2. Conhecendo o Violão e Afinando":
        estrutura_afinacao()
    elif modulo_selecionado == "3. Entendendo os Acordes e Diagramas":
        entendendo_acordes()
    elif modulo_selecionado == "4. Seus Primeiros Acordes Essenciais":
        primeiros_acordes()
    elif modulo_selecionado == "5. Seu Primeiro Ritmo: Batida Básica":
        ritmo_basico()
    elif modulo_selecionado == "6. Metrônomo Interativo":
        metronomo_interativo()
    elif modulo_selecionado == "7. Exercícios de Troca de Acordes":
        exercicios_troca_acordes()
    elif modulo_selecionado == "8. Quiz do Violão":
        quiz_de_violao()
    elif modulo_selecionado == "Conclusão e Próximos Passos":
        conclusao()

    # Mensagem de depuração no terminal
    print(f"Módulo '{modulo_selecionado}' selecionado e carregado.")
