import streamlit as st
from math import *
import sympy

x = sympy.symbols("x")
exp = sin(6 / 2) + 8 - x
st.latex(exp)


st.title(sympy.solve(exp,x))
