import streamlit as st
import math as *
import sympy

x = sympy.symbols("x")
exp = sin(6 / 2) + 8 - x
st.latex(exp)


st.title(sympy.solve(exp,x))
