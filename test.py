import streamlit as st
from sympy import *

x = symbols("x")
exp = sin(6 / 2) + 8 - x
st.latex(exp)


st.title(solve(exp,x))
