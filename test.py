import streamlit as st
import sympy

x = sympy.symbol("x")


st.title(sympy.solve("6^2",x))
