import streamlit as st

class side_bar:
  
  

  
  def __init__(self):
    with st.sidebar:
      st.title("Manual de uso")
      st.subheader("Bienvenido a mi calculadora, aquí está toda la información que debes de saber para usarla.")
      
      
      col1, col2, col3 = st.columns(3)

      with col1:
        st.button(label = "¿Por qué una calculadora de texto?", on_click = self.comandos)
      with col2:
        st.button("¿Qué puedo llegar a hacer?")
      with col3:
        st.button("¿Cómo puedo usarla?")
        
  def comandos(self):
      st.sidebar.st.button("Funcionará¿")
      
Documentacion = side_bar()
