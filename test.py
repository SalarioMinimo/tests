import streamlit as st
import sympy

x = sympy.symbols("x")
exp = "Sin(6 / 2) + 8 - x"
st.latex(exp)


st.title(sympy.solve(exp,x))
