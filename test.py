import streamlit as st

class side_bar:
  
  

  
  def __init__(self):
    with st.sidebar:
      st.title("Manual de uso")
      st.subheader("Bienvenido a mi calculadora, aquí está toda la información que debes de saber para usarla.")
      
      genre = st.radio("Selecciona un apartado",("Justificacion", "Comandos", "Ejemplos"))

        
  def comandos(self):
      st.sidebar.button("Funcionará¿")
      
Documentacion = side_bar()
