import streamlit as st
import requests

st.title("Previsão do Tempo")

cidade = st.text_input("Digite o nome da cidade: ")

if st.button("Buscar Previsão"):
    resposta = requests.get(f"http://127.0.0.1:8000/weather?cidade={cidade}")
    if resposta.status_code == 200:
        clima_dados = resposta.json()
        st.write(f"Cidade: {clima_dados['cidade']}")
        st.write(f"Temperatura: {clima_dados['temperatura']}ºC")
        st.write(f"Condição do tempo: {clima_dados['clima']}")

    else:
        st.write("Cidade não encontrada.")