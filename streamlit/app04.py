import pandas as pd
import numpy as np
import streamlit as st 


st.title('#Grafica')

gr_datos=pd.DataFrame(np.random.randn(10,2), columns=[f'Col{i+1}' for i in range(2)])
st.write(gr_datos)
st.line_chart(gr_datos)