import streamlit as st

class side_bar:
  
  

  
  def __init__(self):
    with st.sidebar:
      selection = {"Justificación":self.Justificación,"Comandos":self.Comandos,"Ejemplos":self.Ejemplos}
      st.title("Manual de uso")
      st.subheader("Bienvenido a mi calculadora, aquí está toda la información que debes de saber para usarla.")
      
      genre = st.radio("Selecciona un apartado",("Justificación", "Comandos", "Ejemplos"))
      selection[genre]()

  def Justificación(self):
    st.sidebar.text("Quizás funciona")
    
  def Comandos(self):
    st.sidebar.text("Funcionará¿")
    
  def Ejemplos(self):
    st.sidebar.text("Esta funcionando")
      
      
      
Documentacion = side_bar()
