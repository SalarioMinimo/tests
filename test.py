import streamlit as st
import sympy

x = sympy.symbols("x")


st.title(sympy.solve("6^2=x",x))
