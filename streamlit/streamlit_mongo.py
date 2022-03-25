import pandas as pd
import numpy as np
import streamlit as st 
from pymongo import MongoClient

st.title('#Datos PQR_Salud 2019')
st.write('#Datos PQR_Salud 2019')

client = MongoClient('localhost', 27017)
db = client.PQR_salud

col=db['Quejas_enero']

st.write('Ejemplo de Conexion')
#list 
#st.write(col.find_one())

df=pd.DataFrame(list(col.find({},{'_id':0}).limit(50)))

st.write( df )