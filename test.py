import streamlit as st
from sympy import *
import nltk

nltk.download('punkt')
esta = nltk.word_tokenize("(64) entre seno de 23,")

esta
x = symbols("x")
exp = sqrt(6 / 2) + 8 - x
st.latex(exp)


st.title(solve(exp,x))
