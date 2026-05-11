import streamlit as st
from groq import Groq

st.title("Summarize")

#API

client = Groq(api_key=st.secrets["qroc_api_key"])   #طلب api من groq وخزنه في streamlit.screts


text = st.text_area("اكتب النص هنا", height = 2000)

if st.button("لخص الجمله"):
  if len(text.split()) < 10:
    st.warning("النص قصير جدا") 










