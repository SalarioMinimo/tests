import streamlit as st

def uwu():
  st.title("nos mataran a todos")
input=st.text_area(label="Text in latex",on_change=uwu)
st.latex(input)
