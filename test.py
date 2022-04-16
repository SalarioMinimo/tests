import streamlit as st
from sympy import *
import nltk
from nltk import word_tokenize

nltk.download('punkt')
esta = word_tokenize({"vamos a matar unos perros."})

esta
x = symbols("x")
exp = sqrt(6 / 2) + 8 - x
st.latex(exp)


st.title(solve(exp,x))
