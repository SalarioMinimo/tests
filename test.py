import streamlit as st

class side_bar:
  
  

  
  def __init__(self):
    with st.sidebar:
      st.title("Documentación")
      st.subheader("Todo lo que necesitas saber")
      
      
      l1, col2, col3 = st.columns([1,1,1])

      with col1:
        st.button('1')
      with col2:
        st.button('2')
      with col3:
        st.button('3')
      
Documentacion = side_bar()
