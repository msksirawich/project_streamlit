
import streamlit as st
import random

st.set_page_config(layout="wide")
st.title('Test Streamlit')

col1_1, col1_2 = st.columns(2)
with col1_1:
    st.header("AAAAAA")
with col1_2:
    st.header("BBBBBB")

col2_1, col2_2 = st.columns([3, 1], border=True)
col2_1.header("CCCCCC")
col2_2.header("DDDDDD")