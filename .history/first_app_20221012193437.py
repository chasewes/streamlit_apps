import streamlit as st

st.header('st.button')

button1 = st.button('Say hello')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
