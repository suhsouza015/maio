import streamlit as st
import time

# --- Configurações da Página ---
st.set_page_config(
    page_title="Curso de Eletromecânica Automotiva",
    page_icon="🚗",
    layout="wide" # Layout mais amplo para conteúdo técnico
)

# --- Funções para Cada Módulo do Curso ---

def modulo_introducao():
    st.header("1. Introdução à Eletromecânica Automotiva 🛠️")
    st.write("""
    Bem-vindo(a) ao seu curso completo de Eletromecânica Automotiva! Este curso foi desenvolvido para te guiar desde os **princípios fundamentais** até os **sistemas mais avançados** dos veículos modernos.

    A eletromecânica automotiva é o coração dos carros de hoje, combinando conhecimentos de mecânica, elétrica e eletrônica. Entender como esses sistemas interagem é essencial para qualquer profissional ou entusiasta automotivo.

    **Neste curso, você vai aprender sobre:**
    * **Fundamentos:** Leis da eletricidade, componentes eletrônicos.
    * **Sistemas Essenciais:** Bateria, carga, partida, ignição, injeção.
    * **Eletrônica Embarcada:** Sensores, atuadores, módulos de controle (ECUs).
    * **Redes de Comunicação:** CAN Bus, LIN Bus.
    * **Sistemas Avançados:** ABS, Airbag, Direção Elétrica.
    * **Diagnóstico:** Utilização de multímetro, scanner automotivo e osciloscópio.

    Prepare-se para uma jornada de conhecimento que transformará sua compreensão sobre os veículos!
    """)
    st.image("https://images.unsplash.com/photo-1579899144865-ec12a14b3017?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80", caption="A complexidade e beleza da eletromecânica automotiva.", use_container_width=True)
    st.markdown("---")

def modulo_fundamentos():
    st.header("2. Fundamentos da Eletricidade e Eletrônica Automotiva ⚡")
    st.write("""
    Antes de mergulharmos nos sistemas automotivos, é crucial entender os **conceitos básicos de eletricidade e eletrônica**. Sem essa base, a compreensão dos circuitos e falhas será limitada.
    """)

    with st.expander("2.1. Conceitos Básicos: Tensão, Corrente e Resistência", expanded=True):
        st.write("""
        * **Tensão (Voltagem - V):** É a "pressão" ou força que empurra os elétrons através de um circuito. No automotivo, a maioria dos sistemas opera com **12V** (bateria).
        * **Corrente (Amperagem - A):** É o fluxo de elétrons em um circuito. Uma corrente alta indica muitos elétrons passando por segundo.
        * **Resistência (Ohms - Ω):** É a oposição ao fluxo de corrente. Materiais com alta resistência dificultam a passagem dos elétrons.
        """)
        st.info("💡 **Lei de Ohm:** $V = I \\times R$ (Tensão = Corrente x Resistência). Essa lei é a base para a análise de circuitos elétricos.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Ohm%27s_Law_triangle.svg/1200px-Ohm%27s_Law_triangle.svg.png", caption="Triângulo da Lei de Ohm", width=300)

    with st.expander("2.2. Tipos de Corrente: Contínua (CC) e Alternada (CA)", expanded=True):
        st.write("""
        * **Corrente Contínua (CC/DC):** Os elétrons fluem em uma única direção. É a corrente fornecida pela **bateria** do veículo e a utilizada pela maioria dos componentes eletrônicos.
        * **Corrente Alternada (CA/AC):** Os elétrons mudam de direção periodicamente. É gerada pelo **alternador** e depois retificada para CC para carregar a bateria e alimentar o sistema.
        """)
        st.markdown("---")

    with st.expander("2.3. Componentes Eletrônicos Básicos no Automotivo", expanded=True):
        st.write("""
        * **Fusiveis:** Dispositivos de segurança que se queimam e interrompem o circuito em caso de sobrecarga, protegendo os componentes.
        * **Relés:** Interruptores eletromagnéticos que permitem que uma pequena corrente controle uma corrente muito maior. Essenciais em diversos sistemas (faróis, partida, etc.).
        * **Diodos:** Permitem que a corrente flua em apenas uma direção. Usados em retificadores, proteção contra polaridade invertida.
        * **Transistores:** Atuam como chaves eletrônicas ou amplificadores de sinal. Fundamentais nas ECUs (Unidades de Controle Eletrônico).
        * **Capacitores:** Armazenam energia elétrica temporariamente. Usados para filtrar ruídos e estabilizar tensões.
        * **Resistores:** Componentes que limitam o fluxo de corrente.
        """)
        st.video("https://www.youtube.com/watch?v=b0mS1X6gW-8", help="Vídeo sobre o funcionamento de relés automotivos.", use_container_width=True)
    
    with st.expander("2.4. Ferramentas Essenciais do Eletromecânico", expanded=True):
        st.write("""
        * **Multímetro:** Mede tensão, corrente e resistência. Indispensável para o diagnóstico.
        * **Alicate Amperímetro:** Mede corrente sem a necessidade de cortar o circuito.
        * **Pontas de Prova / Sonda Lógica:** Para testar a presença de tensão e pulsos.
        * **Osciloscópio Automotivo:** Visualiza sinais elétricos ao longo do tempo, revelando padrões e anomalias que um multímetro não detecta (pulsos de injetores, sinais de sensores). **Ferramenta de nível profissional.**
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Multimeter_and_leads.jpg/1280px-Multimeter_and_leads.jpg", caption="Multímetro digital: sua primeira ferramenta.", use_container_width=True)
    st.markdown("---")

def modulo_bateria_carga():
    st.header("3. Bateria e Sistema de Carga 🔋")
    st.write("""
    A bateria é o coração elétrico do veículo, fornecendo a energia inicial para a partida e estabilizando o sistema. O sistema de carga garante que a bateria seja recarregada e que haja energia suficiente para todos os componentes enquanto o motor está funcionando.
    """)

    with st.expander("3.1. Bateria Automotiva: Função e Tipos", expanded=True):
        st.write("""
        * **Função:** Fornece energia elétrica para o motor de partida e os sistemas eletrônicos quando o motor está desligado ou em baixas rotações. Atua como um "filtro" para o sistema elétrico, estabilizando a tensão.
        * **Tipos Comuns:**
            * **Chumbo-Ácido (convencional e selada):** Mais comuns, usam solução de ácido sulfúrico e placas de chumbo. As seladas não requerem manutenção.
            * **AGM (Absorbent Glass Mat):** Mais duráveis, melhor desempenho em baixas temperaturas e mais resistentes a vibrações. Usadas em veículos com Start-Stop.
            * **EFB (Enhanced Flooded Battery):** Melhoradas para Start-Stop, mas menos avançadas que AGM.
        * **Parâmetros:**
            * **Voltagem (V):** Nominalmente 12V (com 6 células de 2V). Uma bateria carregada deve ter ~12.6V.
            * **Amperes-Hora (Ah):** Capacidade de armazenamento de energia (ex: 60 Ah significa que ela pode fornecer 60A por 1 hora, ou 1A por 60 horas).
            * **CCA (Cold Cranking Amps):** Capacidade de fornecer corrente de partida a frio.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Car_battery_with_labels.svg/1200px-Car_battery_with_labels.svg.png", caption="Bateria Automotiva", width=400)

    with st.expander("3.2. Alternador: Geração de Energia", expanded=True):
        st.write("""
        * **Função:** Converte energia mecânica (do motor) em energia elétrica (CA), que é então retificada para CC para carregar a bateria e alimentar os sistemas do veículo.
        * **Componentes Internos:**
            * **Estator:** Bobinas fixas que geram CA.
            * **Rotor:** Bobina giratória (induzido) que gera campo magnético.
            * **Escovas:** Fazem contato com o rotor para fornecer corrente.
            * **Regulador de Tensão:** Mantém a tensão de saída do alternador constante (geralmente entre 13.8V e 14.8V).
            * **Retificador (Diodos):** Converte a CA gerada pelo estator em CC.
        """)
        st.video("https://www.youtube.com/watch?v=FqY-6F_R4K0", help="Como funciona o alternador do carro.", use_container_width=True)

    with st.expander("3.3. Diagnóstico Comum do Sistema de Carga", expanded=True):
        st.write("""
        * **Teste de Tensão da Bateria (Motor Desligado):** Com multímetro, deve estar acima de 12.4V.
        * **Teste de Tensão de Carga (Motor Ligado):** Com multímetro nos terminais da bateria, o alternador deve estar carregando entre 13.8V e 14.8V. Fora dessa faixa indica problema no alternador ou regulador.
        * **Teste de Queda de Tensão (Cabo Terra/Positivo):** Medir a diferença de potencial entre o terminal da bateria e o ponto de conexão no chassi/motor. Quedas elevadas indicam resistência nos cabos.
        """)
    st.markdown("---")

def modulo_partida():
    st.header("4. Sistema de Partida 🚀")
    st.write("""
    O sistema de partida é responsável por girar o motor até que ele inicie seu próprio ciclo de combustão. É um dos sistemas que mais consome corrente elétrica no veículo.
    """)

    with st.expander("4.1. Componentes do Sistema de Partida", expanded=True):
        st.write("""
        * **Bateria:** Fornece a alta corrente necessária.
        * **Motor de Partida (Arranque):** Um motor elétrico de CC, de alta potência, projetado para girar o volante do motor.
            * **Bendix (Pinhão):** Engrenagem que se projeta para engrenar com o volante do motor e, após a partida, recua.
            * **Solenóide de Partida:** Atua como um relé de alta corrente e, mecanicamente, empurra o Bendix para fora.
        * **Chave de Ignição / Botão Start-Stop:** Aciona o circuito de partida.
        * **Cabos de Bateria:** Grossos, para suportar a alta corrente.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Starter_motor_diagram.png/1200px-Starter_motor_diagram.png", caption="Esquema do Motor de Partida", use_container_width=True)

    with st.expander("4.2. Funcionamento do Sistema", expanded=True):
        st.write("""
        1.  Ao girar a chave de ignição para "START" (ou pressionar o botão Start/Stop), uma pequena corrente é enviada ao **solenóide de partida**.
        2.  O solenóide então executa duas ações:
            * Fecha um circuito de alta corrente, permitindo que a energia da bateria flua diretamente para o motor de partida.
            * Mecanicamente, empurra o **Bendix** para engrenar com a cremalheira do volante do motor.
        3.  O motor de partida gira o volante do motor, dando início ao ciclo de combustão.
        4.  Assim que o motor pega, o Bendix se desengata para evitar danos por excesso de rotação.
        """)
        st.video("https://www.youtube.com/watch?v=R9jUaE2CjS0", help="Animação do funcionamento do motor de partida.", use_container_width=True)

    with st.expander("4.3. Diagnóstico Comum do Sistema de Partida", expanded=True):
        st.write("""
        * **O motor não gira / gira lentamente:**
            * **Bateria fraca/descarregada:** Verificar tensão da bateria.
            * **Conexões frouxas/corroídas:** Inspecionar e limpar terminais.
            * **Motor de partida com defeito:** Testar a corrente de partida (com alicate amperímetro), verificar o acionamento do solenóide.
            * **Falha no interruptor de ignição/relé de partida.**
        * **Estalo (clique) e nada acontece:** Geralmente indica solenóide funcionando, mas o motor de partida não recebe corrente suficiente (bateria fraca ou conexões ruins) ou o próprio motor de partida está travado.
        """)
    st.markdown("---")

def modulo_ignicao():
    st.header("5. Sistema de Ignição 🔥")
    st.write("""
    O sistema de ignição é responsável por gerar uma **centelha de alta tensão** nas velas de ignição no momento exato, para inflamar a mistura ar-combustível dentro dos cilindros do motor a gasolina.
    """)

    with st.expander("5.1. Componentes Principais (Ignição Eletrônica)", expanded=True):
        st.write("""
        * **Bateria:** Fonte de energia.
        * **Bobina de Ignição:** Transforma a baixa tensão da bateria (12V) em alta tensão (milhares de Volts) através de um princípio de indutância eletromagnética (transformador). Pode ser uma bobina para todos os cilindros, uma para cada dois cilindros (centelha perdida) ou uma bobina por cilindro (COP - Coil-on-Plug).
        * **Velas de Ignição:** Criam a centelha no interior da câmara de combustão.
        * **Cabos de Vela (em alguns sistemas):** Transportam a alta tensão da bobina para as velas.
        * **Módulo de Ignição / ECU:** Controla o momento exato em que a bobina deve gerar a centelha (ponto de ignição). Recebe informações de sensores como o sensor de rotação.
        * **Sensor de Rotação (CKP):** Informa à ECU a posição do virabrequim e a rotação do motor, fundamental para determinar o ponto de ignição.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Spark_plug.jpg/1200px-Spark_plug.jpg", caption="Vela de Ignição", width=300)

    with st.expander("5.2. Funcionamento Simplificado", expanded=True):
        st.write("""
        1.  A **ECU** (ou módulo de ignição) recebe o sinal do **sensor de rotação**, calculando o momento ideal para a centelha.
        2.  Nesse momento, a ECU interrompe o fluxo de corrente primária na **bobina de ignição**.
        3.  A interrupção rápida da corrente no enrolamento primário da bobina induz uma tensão muito alta no enrolamento secundário.
        4.  Essa alta tensão viaja pelos cabos de vela (ou diretamente pela bobina COP) até a **vela de ignição**.
        5.  Na vela, a tensão salta a folga entre os eletrodos, criando uma **centelha** que inflama a mistura ar-combustível.
        """)
        st.video("https://www.youtube.com/watch?v=S0T0jCjU5rI", help="Explicação detalhada do sistema de ignição.", use_container_width=True)

    with st.expander("5.3. Diagnóstico Comum do Sistema de Ignição", expanded=True):
        st.write("""
        * **Falhas de Ignição (Engine Misfire):** Motor falhando, perda de potência, luz da injeção acesa.
            * **Velas sujas/gastas:** Inspecionar e substituir.
            * **Cabos de vela com fuga de corrente:** Inspecionar no escuro, medir resistência.
            * **Bobina de ignição com defeito:** Testar resistência, verificar pulsos de comando com osciloscópio.
            * **Problemas no sensor de rotação:** Verificar sinal com osciloscópio, códigos de falha.
        * **Sem Centelha:**
            * Verificar alimentação da bobina.
            * Verificar sinal de pulso da ECU para a bobina (com osciloscópio).
            * Testar a própria bobina.
        """)
    st.markdown("---")

def modulo_injecao_eletronica():
    st.header("6. Sistema de Injeção Eletrônica ⛽")
    st.write("""
    A injeção eletrônica é um sistema complexo que gerencia a quantidade de combustível injetada e o tempo de ignição para otimizar o desempenho do motor, economia de combustível e reduzir emissões poluentes. É controlada pela **ECU (Unidade de Controle Eletrônico)**, o "cérebro" do veículo.
    """)

    with st.expander("6.1. Componentes Principais do Sistema", expanded=True):
        st.write("""
        * **ECU (Engine Control Unit):** O módulo principal que processa as informações dos sensores e comanda os atuadores.
        * **Bomba de Combustível:** Leva o combustível do tanque sob pressão para os injetores.
        * **Regulador de Pressão de Combustível:** Mantém a pressão constante na linha dos injetores.
        * **Injetores de Combustível:** Válvulas controladas eletronicamente que pulverizam o combustível diretamente no coletor de admissão (injeção multiponto) ou na câmara de combustão (injeção direta).
        * **Corpo de Borboleta Eletrônico (Drive-by-Wire):** Controla o fluxo de ar para o motor.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Fuel_Injector.jpg/1200px-Fuel_Injector.jpg", caption="Injetor de Combustível", width=400)

    with st.expander("6.2. Sensores Chave (Entradas para a ECU)", expanded=True):
        st.write("""
        * **Sensor de Posição da Borboleta (TPS):** Informa a abertura da borboleta (demanda do motorista).
        * **Sensor de Fluxo de Ar (MAF) / Sensor de Pressão do Coletor (MAP):** Medem a quantidade de ar que entra no motor.
        * **Sensor de Oxigênio (Sonda Lambda):** Mede a quantidade de oxigênio nos gases de escape, indicando se a mistura ar-combustível está rica ou pobre. Fundamental para o controle do motor de ciclo fechado.
        * **Sensor de Temperatura do Líquido de Arrefecimento (ECT):** Informa a temperatura do motor.
        * **Sensor de Rotação (CKP) e Posição do Comando (CMP):** Informam à ECU a rotação e a posição exata do motor para o cálculo do tempo de injeção e ignição.
        * **Sensor de Velocidade do Veículo (VSS):** Informa a velocidade do carro.
        """)
    
    with st.expander("6.3. Atuadores Chave (Saídas da ECU)", expanded=True):
        st.write("""
        * **Injetores de Combustível:** A ECU controla o tempo de abertura (pulso) para dosar a quantidade de combustível.
        * **Bobinas de Ignição:** A ECU comanda a geração da centelha.
        * **Válvula de Controle de Marcha Lenta (IACV) / Motor de Passo do Corpo de Borboleta:** Controla a entrada de ar para manter a marcha lenta estável.
        * **Ventoinha do Radiador:** Acionada para controle de temperatura.
        * **Bomba de Combustível:** A ECU pode controlar seu acionamento e, em alguns casos, sua velocidade.
        """)

    with st.expander("6.4. Princípio de Funcionamento (Ciclo Fechado)", expanded=True):
        st.write("""
        1.  Os **sensores** monitoram constantemente as condições de operação do motor (quantidade de ar, temperatura, rotação, posição da borboleta, teor de oxigênio nos gases de escape).
        2.  A **ECU** recebe todos esses dados, processa-os em milissegundos usando mapas pré-programados e cálculos complexos.
        3.  Com base nesses cálculos, a ECU decide a **quantidade ideal de combustível a ser injetada** (tempo de injeção dos injetores) e o **momento exato da ignição**.
        4.  A ECU envia comandos para os **atuadores** (injetores, bobinas, etc.) para implementar suas decisões.
        5.  O **sensor de oxigênio (sonda lambda)** monitora os resultados da combustão, fornecendo um feedback à ECU para que ela possa fazer ajustes finos (ciclo fechado), garantindo a mistura ar-combustível ideal (estequiométrica).
        """)
        st.video("https://www.youtube.com/watch?v=jWn7qK8KzI0", help="Como funciona a injeção eletrônica.", use_container_width=True)
    st.markdown("---")

def modulo_sensores_atuadores():
    st.header("7. Sensores e Atuadores: A Interface do Veículo 📡")
    st.write("""
    Sensores e atuadores são os componentes que permitem que a ECU "leia" as condições do veículo (sensores) e "aja" sobre elas (atuadores). São essenciais para o funcionamento de todos os sistemas eletrônicos modernos.
    """)

    with st.expander("7.1. Sensores: Os 'Olhos' e 'Ouvidos' da ECU", expanded=True):
        st.write("""
        Sensores convertem uma grandeza física (temperatura, pressão, velocidade, posição) em um **sinal elétrico** que a ECU pode interpretar.

        * **Sensor MAP (Manifold Absolute Pressure):** Mede a pressão absoluta dentro do coletor de admissão. Variação da pressão indica carga do motor.
        * **Sensor MAF (Mass Air Flow):** Mede a massa de ar que entra no motor. Mais preciso que o MAP em algumas aplicações.
        * **Sensor de Posição da Borboleta (TPS):** Um potenciômetro que informa a posição do pedal do acelerador (em sistemas drive-by-wire) ou da borboleta mecânica.
        * **Sensor de Oxigênio (Sonda Lambda):** O mais famoso. Gera uma tensão que varia de acordo com o teor de oxigênio nos gases de escape. Indica se a mistura está rica (pouco O2) ou pobre (muito O2).
        * **Sensor de Temperatura do Líquido de Arrefecimento (ECT):** Termistor que varia sua resistência com a temperatura.
        * **Sensor de Temperatura do Ar de Admissão (IAT):** Similar ao ECT, mas mede a temperatura do ar de admissão.
        * **Sensor de Rotação (CKP - Crankshaft Position Sensor):** Gera pulsos elétricos conforme o virabrequim gira, informando a rotação e a posição do motor. Geralmente indutivo ou de Efeito Hall.
        * **Sensor de Posição do Comando de Válvulas (CMP - Camshaft Position Sensor):** Informa a posição das válvulas e ajuda a ECU a sincronizar injeção e ignição.
        * **Sensor de Detonação (Knock Sensor):** Detecta vibrações anormais causadas por detonação (pré-ignição), permitindo que a ECU ajuste o ponto de ignição.
        """)
        st.info("💡 **Dica de Diagnóstico:** Muitos problemas de performance do motor estão relacionados a falhas de sensores. O scanner automotivo é fundamental para ler seus valores em tempo real e identificar anomalias.")

    with st.expander("7.2. Atuadores: Os 'Músculos' do Sistema", expanded=True):
        st.write("""
        Atuadores recebem sinais elétricos da ECU e os convertem em uma ação mecânica ou outra forma de energia.

        * **Injetores de Combustível:** Recebem pulsos elétricos da ECU para abrir e fechar, controlando a quantidade de combustível.
        * **Bobinas de Ignição:** Recebem pulsos da ECU para gerar a alta tensão.
        * **Válvula de Controle de Marcha Lenta (IACV):** Controla o fluxo de ar para manter a marcha lenta estável. Em veículos mais novos, essa função é integrada ao corpo de borboleta eletrônico.
        * **Válvula Canister (Purge Valve):** Controla a purga de vapores de combustível do cânister para o coletor de admissão.
        * **Válvula Solenóide VVT/VVT-i (Variável Valve Timing):** Em motores com comando de válvulas variável, controlam a pressão de óleo que ajusta o ângulo do comando.
        * **Atuadores do Sistema de Freios (ABS/ESC):** Solenóides que controlam a pressão do fluido de freio em cada roda.
        * **Atuadores do Airbag:** Acionadores pirotécnicos que inflam as bolsas em caso de colisão.
        """)
        st.video("https://www.youtube.com/watch?v=FjI1B3M1f9k", help="Vídeo sobre o funcionamento de sensores e atuadores.", use_container_width=True)
    st.markdown("---")

def modulo_redes_automotivas():
    st.header("8. Redes Automotivas (CAN, LIN) 🌐")
    st.write("""
    Com a crescente quantidade de módulos eletrônicos (ECUs) nos veículos, a comunicação ponto a ponto tornou-se inviável. As **redes automotivas** permitem que vários módulos troquem informações de forma rápida e eficiente, reduzindo a complexidade da fiação.
    """)

    with st.expander("8.1. CAN Bus (Controller Area Network)", expanded=True):
        st.write("""
        * **Propósito:** É a rede de comunicação mais comum e robusta em veículos modernos. Permite que as ECUs compartilhem dados críticos (velocidade da roda, rotação do motor, temperatura, etc.) em tempo real.
        * **Funcionamento:** Os dados são transmitidos em "mensagens" que todos os módulos na rede podem "ouvir". Cada mensagem tem um identificador que determina sua prioridade. Se dois módulos tentarem transmitir ao mesmo tempo, a mensagem de maior prioridade "vence" (arbitragem).
        * **Velocidade:** Opera em alta velocidade (500 kbit/s a 1 Mbit/s para CAN de alta velocidade) e baixa velocidade (125 kbit/s para CAN de baixa velocidade).
        * **Fiação:** Geralmente consiste em dois fios trançados (CAN High e CAN Low) para reduzir interferências.
        * **Terminadores:** Resistores nas extremidades da rede para evitar reflexões de sinal.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/CANbus_Network.svg/1200px-CANbus_Network.svg.png", caption="Exemplo de Rede CAN Bus", use_container_width=True)
        st.info("💡 **Aplicações:** Injeção eletrônica, ABS, transmissão automática, painel de instrumentos, sistemas de segurança.")

    with st.expander("8.2. LIN Bus (Local Interconnect Network)", expanded=True):
        st.write("""
        * **Propósito:** Uma rede mais simples e de menor custo, usada para comunicação de módulos menos críticos, como controles de janelas, espelhos, rádio, etc.
        * **Funcionamento:** É uma rede mestre-escravo, onde um módulo mestre controla a comunicação de vários módulos escravos.
        * **Velocidade:** Mais lenta que a CAN (até 20 kbit/s).
        * **Fiação:** Usa apenas um fio (single-wire).
        """)
        st.info("💡 **Aplicações:** Portas, espelhos, assentos, sistemas de iluminação interna, sensores de estacionamento simples.")

    with st.expander("8.3. Diagnóstico de Redes Automotivas", expanded=True):
        st.write("""
        * **Scanner Automotivo:** Pode identificar códigos de falha de comunicação (DTCs) relacionados à rede (ex: U-Codes).
        * **Osciloscópio:** Ferramenta essencial para analisar os sinais de comunicação da rede CAN e LIN. Permite verificar a integridade dos sinais, a presença de ruído e falhas de transmissão de dados.
        * **Multímetro:** Medir resistência nos terminadores CAN e verificar a continuidade dos fios da rede.
        """)
    st.markdown("---")

def modulo_sistemas_conforto_seguranca():
    st.header("9. Sistemas de Conforto e Segurança Avançados 🧠")
    st.write("""
    Os veículos modernos estão repletos de sistemas eletrônicos que aumentam significativamente o conforto, a segurança e a assistência ao motorista.
    """)

    with st.expander("9.1. Sistema de Freios ABS (Anti-lock Braking System)", expanded=True):
        st.write("""
        * **Função:** Impede o travamento das rodas durante frenagens bruscas, permitindo que o motorista mantenha o controle da direção e reduza a distância de frenagem.
        * **Componentes:**
            * **Módulo de Controle ABS (ECU ABS):** O cérebro do sistema.
            * **Sensores de Velocidade da Roda:** Monitoram a rotação individual de cada roda.
            * **Unidade Hidráulica do ABS (HPU):** Contém válvulas solenoides e uma bomba que modulam a pressão do fluido de freio para cada roda.
        * **Funcionamento:** Se um sensor de roda detecta que uma roda está prestes a travar (desacelerando muito rapidamente), a ECU ABS comanda a HPU para liberar e aplicar a pressão do freio naquela roda rapidamente, pulsando a frenagem.
        """)
        st.video("https://www.youtube.com/watch?v=QhQ0sI-n-6M", help="Como funciona o sistema ABS.", use_container_width=True)

    with st.expander("9.2. Sistema de Airbag (SRS - Supplemental Restraint System)", expanded=True):
        st.write("""
        * **Função:** Infla rapidamente bolsas de ar em caso de colisão severa para proteger os ocupantes do veículo.
        * **Componentes:**
            * **Módulo de Controle do Airbag (ACU):** Contém acelerômetros internos e processa informações de outros sensores de colisão.
            * **Sensores de Colisão:** Localizados em pontos estratégicos do veículo para detectar a desaceleração de impacto.
            * **Bolsas de Airbag:** Onde o gás é gerado para inflar.
            * **Acionadores Pirotécnicos:** Geram gás nitrogênio rapidamente para inflar as bolsas.
            * **Luz de Advertência do Airbag (SRS Light):** Acende no painel se houver uma falha no sistema.
        * **Funcionamento:** Quando os sensores de colisão detectam um impacto severo que excede um certo limite, o ACU envia um sinal elétrico para o acionador pirotécnico, que infla a bolsa em milissegundos.
        """)
        st.warning("⚠️ **ATENÇÃO:** O sistema de Airbag é extremamente sensível. Qualquer manipulação deve ser feita por profissionais treinados, seguindo procedimentos de segurança rigorosos para evitar acionamentos acidentais ou falhas críticas.")

    with st.expander("9.3. Outros Sistemas Eletrônicos Avançados", expanded=True):
        st.write("""
        * **Controle de Estabilidade (ESC/ESP):** Usa sensores de guinada e aceleração lateral para aplicar freios individualmente e/ou reduzir a potência do motor para corrigir a trajetória do veículo em situações de perda de controle.
        * **Controle de Tração (TCS):** Impede que as rodas motrizes patinem durante a aceleração.
        * **Direção Assistida Elétrica (EPS):** Substitui a bomba hidráulica por um motor elétrico, tornando a direção mais leve e eficiente.
        * **Sistemas ADAS (Advanced Driver-Assistance Systems):** Frenagem autônoma de emergência, controle de cruzeiro adaptativo, assistente de permanência em faixa, monitoramento de ponto cego, etc. Todos dependem de múltiplos sensores (radar, câmera, ultrassom) e ECUs complexas.
        """)
    st.markdown("---")

def modulo_diagnostico():
    st.header("10. Diagnóstico e Solução de Problemas 🔍")
    st.write("""
    O diagnóstico preciso é a habilidade mais valiosa de um eletromecânico automotivo. Envolve a combinação de conhecimento teórico, uso correto de ferramentas e raciocínio lógico.
    """)

    with st.expander("10.1. A Lógica do Diagnóstico", expanded=True):
        st.write("""
        1.  **Entenda o Problema:** Ouça atentamente a descrição do cliente. Faça perguntas detalhadas sobre quando e como o problema ocorre.
        2.  **Verificação Básica:**
            * Inspecione visualmente (fiação solta, fusíveis queimados, conectores corroídos).
            * Verifique a bateria e o sistema de carga.
            * Verifique os fluidos.
        3.  **Leitura de Códigos de Falha (DTCs):** Use um **scanner automotivo** para ler os códigos de falha armazenados na ECU. Os DTCs apontam para um sistema ou componente com problema, mas não necessariamente para a peça exata.
        4.  **Análise de Dados em Tempo Real (Parâmetros):** O scanner também permite visualizar os valores dos sensores e atuadores em tempo real. Compare esses valores com os esperados (especificações do fabricante). Isso ajuda a identificar sensores com leituras erradas ou atuadores que não respondem.
        5.  **Testes Guiados / Testes de Atuadores:** Muitos scanners permitem acionar atuadores (ex: ligar ventoinha, injetor) ou realizar testes específicos (ex: teste de compressão relativa).
        6.  **Testes com Multímetro:** Meça tensão, corrente e resistência em circuitos específicos.
            * **Teste de Continuidade:** Verificar se há interrupção em um fio.
            * **Teste de Queda de Tensão:** Identificar alta resistência em um circuito (problema de cabo, conector, etc.).
            * **Teste de Consumo de Corrente:** Verificar se há um "vazamento" de corrente que descarrega a bateria.
        7.  **Uso do Osciloscópio:** Para sinais pulsados, complexos ou de tempo, o osciloscópio é indispensável (ex: sinais de sensor de rotação, injetor, CAN Bus). Permite ver a forma de onda do sinal e identificar problemas que um multímetro não consegue.
        8.  **Diagramas Elétricos:** Consulte sempre os diagramas elétricos do veículo. Eles são o "mapa" do sistema e mostram a localização dos componentes, cores dos fios e interconexões.
        9.  **Isolamento do Problema:** Através da análise e testes, isole o problema até o componente defeituoso.
        10. **Verificação da Reparação:** Após a troca da peça, verifique se o problema foi resolvido e se não há novos códigos de falha. Realize um teste de rodagem.
        """)
        st.image("https://www.fluke.com/content/dam/community/fluke/articles/image/Troubleshooting-Auto-Electrical-System.jpg", caption="O diagnóstico requer multímetro e scanner.", use_container_width=True)

    with st.expander("10.2. Ferramentas de Diagnóstico Essenciais", expanded=True):
        st.write("""
        * **Scanner Automotivo (OBD-II):** Ferramenta principal para ler códigos de falha, dados em tempo real e realizar testes. Existem scanners simples (para entusiastas) e scanners profissionais (multimarcas ou dedicados).
        * **Multímetro Digital:** Para medir tensão, corrente e resistência.
        * **Osciloscópio Automotivo:** Essencial para analisar sinais complexos de sensores e redes de comunicação.
        * **Pontas de Prova / Sonda Lógica:** Para testar a presença de sinais.
        * **Ferramentas Manuais Básicas:** Chaves, alicates, testadores de fusíveis.
        * **Software de Reparação e Diagramas Elétricos (ex: Alldata, Mitchell OnDemand, GDS, Techstream):** Acesso à documentação técnica do fabricante é fundamental.
        """)
    st.markdown("---")

def modulo_conclusao():
    st.header("11. Conclusão e Próximos Passos na Carreira 🎓")
    st.write("""
    Parabéns! Você concluiu este curso introdutório e avançado em Eletromecânica Automotiva. Você agora tem uma base sólida nos principais sistemas elétricos e eletrônicos de um veículo.

    ### **Pontos Chave para o Sucesso:**
    * **Atualização Constante:** A tecnologia automotiva evolui rapidamente (veículos elétricos/híbridos, condução autônoma). Mantenha-se atualizado com cursos, seminários e publicações.
    * **Prática:** O conhecimento só se consolida com a prática. Comece com veículos mais simples e avance gradualmente. Trabalhe em oficinas, laboratórios ou em seus próprios projetos.
    * **Ferramentas:** Invista em boas ferramentas de diagnóstico. Um bom scanner e um osciloscópio são diferenciais.
    * **Segurança:** Sempre priorize a segurança. Desconecte a bateria ao trabalhar em componentes elétricos e siga as normas de segurança da oficina.

    ### **Caminhos de Carreira em Eletromecânica Automotiva:**
    * **Mecânico Automotivo / Eletricista Automotivo:** Trabalhar em oficinas independentes ou concessionárias.
    * **Técnico de Diagnóstico:** Especialista em identificar e resolver problemas complexos usando scanners e osciloscópios.
    * **Instalador de Acessórios Automotivos:** Especialista em som, alarmes, rastreadores, etc.
    * **Instrutor Técnico:** Compartilhar seu conhecimento com a próxima geração.
    * **Engenheiro Automotivo / Pesquisa e Desenvolvimento:** Para aqueles que buscam aprofundar a nível de engenharia e inovação.

    A área de eletromecânica automotiva é dinâmica e cheia de oportunidades. Continue aprendendo, praticando e se apaixonando por essa tecnologia fascinante!
    """)
    st.image("https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80", caption="O futuro da mobilidade está na eletromecânica.", use_container_width=True)
    st.markdown("---")


# --- Estrutura Principal do Aplicativo Streamlit ---
if __name__ == "__main__":
    st.title("📚 Curso de Eletromecânica Automotiva")
    st.markdown("Do Básico ao Profissional: Domine a Eletrônica e Mecânica dos Veículos Modernos.")

    st.sidebar.title("Navegação do Curso")
    modulos = {
        "1. Introdução": modulo_introducao,
        "2. Fundamentos da Eletricidade e Eletrônica": modulo_fundamentos,
        "3. Bateria e Sistema de Carga": modulo_bateria_carga,
        "4. Sistema de Partida": modulo_partida,
        "5. Sistema de Ignição": modulo_ignicao,
        "6. Sistema de Injeção Eletrônica": modulo_injecao_eletronica,
        "7. Sensores e Atuadores": modulo_sensores_atuadores,
        "8. Redes Automotivas (CAN, LIN)": modulo_redes_automotivas,
        "9. Sistemas de Conforto e Segurança": modulo_sistemas_conforto_seguranca,
        "10. Diagnóstico e Solução de Problemas": modulo_diagnostico,
        "11. Conclusão e Próximos Passos": modulo_conclusao,
    }

    modulo_selecionado = st.sidebar.radio(
        "Selecione um Módulo:",
        list(modulos.keys()),
        key="eletromecanica_navigation"
    )

    st.markdown("---") # Linha divisória para separar a navegação do conteúdo

    # Renderiza a função do módulo selecionado
    modulos[modulo_selecionado]()

    # Mensagem de depuração no terminal (visível apenas para quem executa o script)
    print(f"Módulo '{modulo_selecionado}' selecionado e carregado.")
