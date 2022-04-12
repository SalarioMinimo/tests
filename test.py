import streamlit as st

input=st.text_area(label="Text in latex")
st.latex(input)
