import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.sidebar.checkbox('Click me')

st.button('Click')

st.markdown(':+1:')
