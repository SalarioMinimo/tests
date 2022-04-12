import streamlit as st
import sympy

x = sympy.symbols("x")
exp = 2 * 6 - x


st.title(sympy.solve(exp,x))
