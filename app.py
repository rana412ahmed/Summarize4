import streamlit as st
from groq import Groq

st.title("Summarize")

client = Groq(api_key=st.secrets["qroc_api_key"])   #طلب api من groq وخزنه في streamlit.screts

text = st.text_area("اكتب النص هنا", height = 2000)

if st.button("لخص الجمله"):
  if len(text.split()) < 10: 
    st.warning("النص قصير جدا") 
  else:
    with st.spinner("جاري التلخيص"):

      #تحديد اللغه هل عربي ام انجليزي
      arabic_letters = 0
      for c in text:   # بنعد عدد الحروف العربي في الجمله
        if '\u0600' <= c <= '\u06FF' : 
          arabic_letters += 1 
          
      if arabic_letters > 10: 
        language = "العربية"
      else:
        language = "English"
        
      response = client.chat.completions.create(    #بنطلب اننا نكلم المودل
        model="llama-3.3-70b.versatile",
        messages = [
          {"role" : "system", "content" : f"You are a helpful assistant for kid. Summarize the text in 3-4 sentences. You MUST respond in {language} only"},
          {"role" : "user", "content" : text}
        ]
      )
      st.success(response.choices[0].massage.content) 
  
  
  







