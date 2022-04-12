import streamlit as st
import sympy

x = sympy.symbols("x")
exp = 2 * (5 + 8) - x
st.latex(exp)


st.title(sympy.solve(exp,x))
