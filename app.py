import streamlit as st
from datetime import datetime, timedelta

st.title("Saiba sua hora:")

horap = st.text_input("Que horas você entrou? (formato HH:MM)")

if horap:
    try:
        hora = datetime.strptime(horap, "%H:%M")
        ex = timedelta(hours=8, minutes=50)
        hora_final = hora + ex
        st.write("Horário de saída:", hora_final.strftime("%H:%M"))

        hora_maxima = timedelta(hours=2, minutes=0)
        hora_extra = hora_final + hora_maxima
        st.write("Seu horário máximo final com hora extra é:", hora_extra.strftime("%H:%M"))
    except ValueError:
        st.error("Por favor, insira o horário no formato correto HH:MM.")
else:
    st.info("Por favor, insira o horário para calcular a saída.")
