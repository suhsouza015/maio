import streamlit as st 

st.title("Perfil do Jogador")

nome = st.text_input("Digite seu nome")
whatsapp = st.text_input("Digite seu whatsapp")
lane = st.selectbox("Selecione sua lane", ["Top", "Jungle", "Mid", "ADC", "Support"])

cadastro = st.button("Cadastrar")
if cadastro:
    with open("players.csv", "a") as arquivo:
        arquivo.write(f"{nome},{whatsapp},{lane}\n")
        st.success("Cadastro realizado com sucesso!")
