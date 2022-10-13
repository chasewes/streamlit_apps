import streamlit as st

st.header('st.button')

button1 = st.button('Say hello')

if button1:
    st.write('Why hello there')
else:
    st.write('Goodbye')
