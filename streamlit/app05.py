import pandas as pd
import numpy as np
import streamlit as st 


st.title('#Barra lateral')

selectbox =st.sidebar.selectbox(
    "continuar",
    ["Si", "No"]
)

st.write(selectbox)
