import streamlit as st
import pandas as ps 

st.title("ejemplo de tabla")

st.write(ps.DataFrame({'A':[2,4,5,6], 'B':[1,2,3,4]}))