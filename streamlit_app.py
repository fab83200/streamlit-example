import streamlit as st
import pandas as pd

col1, buffer_column, col2 = st.columns([2, .5, 2])                    # sets up columns of standard width where sum is the total width

features_available = ['Option1', 'Option2', 'Option3']

next = st.button("Next Option")                                       # creates an on_click button with label "Next..." and named `next`

if next:                                                              # creates the rotary effect on the radio_button
  if st.session_state.radio_button == 'Option1':
    st.session_state.radio_button = 'Option2'
  elif st.session_state.radio_button == 'Option2':
    st.session_state.radio_button = 'Option3'
  else:
    st.session_state.radio_button = 'Option1'

radio_button = col1.radio("Pick an option:",                                # creates a Radio_Buttons widget labeled "Pick..." and named `radio_button`
                    features_available,                               # creates as buttons as features declared
                    key="radio_button")                               # names the radio button widget `radio_button`

if radio_button == 'Option1':
  col2.write("You picked `Option1` Conclusion1")
if radio_button == 'Option2':
  col2.write("You picked `Option2` Conclusion2")
if radio_button == 'Option3':
  col2.write("You picked `Option3` Conclusion3")

