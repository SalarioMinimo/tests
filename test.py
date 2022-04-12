import streamlit as st
import math
import sympy

x = sympy.symbols("x")
exp = math.sin(6 / 2) + 8 - x
st.latex(exp)


st.title(sympy.solve(exp,x))
