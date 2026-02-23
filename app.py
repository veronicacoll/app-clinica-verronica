import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Historias Clínicas", layout="wide")

st.title("Sistema de Historias Clínicas")

menu = st.sidebar.selectbox("Menú", ["Agregar paciente", "Ver pacientes"])

if "pacientes" not in st.session_state:
    st.session_state.pacientes = []

if menu == "Agregar paciente":
    st.subheader("Nuevo paciente")

    nombre = st.text_input("Nombre y Apellido")
    dni = st.text_input("DNI")
    nacimiento = st.date_input("Fecha de nacimiento")
    escuela = st.text_input("Escuela")
    grado = st.text_input("Grado")
    motivo = st.text_area("Motivo de consulta")
    recorrido = st.text_area("Recorrido terapéutico")

    if st.button("Guardar"):
        st.session_state.pacientes.append({
            "Nombre": nombre,
            "DNI": dni,
            "Nacimiento": nacimiento,
            "Escuela": escuela,
            "Grado": grado,
            "Motivo": motivo,
            "Recorrido": recorrido
        })
        st.success("Paciente guardado")

if menu == "Ver pacientes":
    st.subheader("Listado de pacientes")
    if st.session_state.pacientes:
        df = pd.DataFrame(st.session_state.pacientes)
        st.dataframe(df)
    else:
        st.info("No hay pacientes cargados")
