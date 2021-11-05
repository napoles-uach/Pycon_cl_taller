import streamlit as st
from transformers import pipeline
st.title('Ejemplo en Hugging Face')
pipe = pipeline('sentiment-analysis')
text = st.text_area('enter some text')
if text:
    out = pipe(text)
    st.json(out)
