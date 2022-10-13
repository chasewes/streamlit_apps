import streamlit as st

st.header('st.button')

button1 = st.button('Say hello')
button2 = st.button('Say Kenobi')


if button1:
    st.write('Hello there!')
if button2:
    st.write('General !')
