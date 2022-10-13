import streamlit as st

st.header('st.button')

button1 = st.button('Button 1')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
