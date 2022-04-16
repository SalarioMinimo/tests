import streamlit as st
from sympy import *
from nltk import word_tokenize

x = symbols("x")
exp = sqrt(6 / 2) + 8 - x
st.latex(exp)


st.title(solve(exp,x))
