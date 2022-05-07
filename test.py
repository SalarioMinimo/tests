import streamlit as st

class side_bar:
  
  

  
  def __init__(self):
    with st.sidebar:
      st.title("Documentación")
      st.subheader("Bienvenido a mi calculadora, aquí está toda la información que debes de saber para usarla.")
      
      
      col1, col2, col3 = st.columns([1,1,1])

      with col1:
        st.button("¿Por qué una calculadora de texto?")
      with col2:
        st.button("¿Qué puedo llegar a hacer?")
      with col3:
        st.button("¿Cómo puedo usarla?")
      
Documentacion = side_bar()
