import streamlit as st

st.set_page_config(page_title="App Clínica", layout="centered")

st.title("🧠 Historia Clínica")

st.subheader("Datos del Paciente")

nombre = st.text_input("Nombre y Apellido")
dni = st.text_input("DNI")
fecha_nac = st.date_input("Fecha de Nacimiento")
edad = st.number_input("Edad", min_value=0, max_value=120)
escuela = st.text_input("Escuela")
grado = st.text_input("Grado")

st.subheader("Datos de los Padres")

nombre_padre = st.text_input("Nombre del Padre")
edad_padre = st.number_input("Edad del Padre", min_value=0, max_value=120)
trabajo_padre = st.text_input("Actividad Laboral del Padre")

nombre_madre = st.text_input("Nombre de la Madre")
edad_madre = st.number_input("Edad de la Madre", min_value=0, max_value=120)
trabajo_madre = st.text_input("Actividad Laboral de la Madre")

st.subheader("Motivo de Consulta")
motivo = st.text_area("Escribir aquí")

st.subheader("Recorrido Terapéutico")
recorrido = st.text_area("Escribir aquí")

if st.button("Guardar"):
    st.success("Datos cargados correctamente (modo demostración)")
