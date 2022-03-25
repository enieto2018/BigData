import pandas as pd
import numpy as np
import streamlit as st 
from pymongo import MongoClient

st.title('#Datos PQR_Salud 2019')
st.write('#Datos PQR_Salud 2019')

client = MongoClient('localhost', 27017)
db = client.PQR_salud

col=db['datos_2019']

st.write('Ejemplo de Conexion')

#st.write(col.find_one())

df_canal=pd.DataFrame(list(col.find({},{'_id':0,'pqr_canal':1}).distinct('pqr_canal')))
st.write(df_canal)

df=pd.DataFrame(list(col.find({},{'_id':0,'pqr_canal':1}).limit(50)))

st.write( df )