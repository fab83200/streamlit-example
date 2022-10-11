import streamlit as st
import pandas as pd

col1, buffer_column, col2 = st.columns([2, .5, 2])                    # sets up columns of standard width where sum is the total width

features_available = ['Option1', 'Option2', 'Option3']

next = st.button("Next Option")

if next:
  if st.session_state.my_option == 'Option1':
    st.session_state.my_option = 'Option2'
  elif st.session_state.my_option == 'Option2':
    st.session_state.my_option = 'Option3'
  else:
    st.session_state.my_option = 'Option1'

option = col1.radio("Pick an option:", features_available, key="my_option")        # display a radio button widget

if option == 'Option1':
  col2.write("You picked `Option1` Conclusion1")
if option == 'Option2':
  col2.write("You picked `Option2` Conclusion2")
if option == 'Option3':
  col2.write("You picked `Option3` Conclusion3")

st.session_state
