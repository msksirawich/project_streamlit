import streamlit as st
import random
 
st.set_page_config(layout='wide')
st.title('Test Streamlit')
st.write('Hello World!')
 
if st.button('Generate Random Number'):
    random_number = random.randint(1, 200)
    st.write(f'Random Number: {random_number}')
