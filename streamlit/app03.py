import streamlit as st
import pandas as ps 

st.title("ejemplo de tabla")

mascota=st.selectbox('Mascota', ['perro','gato','canario'])

if mascota=='perro':
    st.write('Saluda a firulais')
if mascota=='gato':
    st.write('Saluda a Karen')
if mascota=='canario':
    st.write('Canta!!')