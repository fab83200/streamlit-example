import streamlit as st
import pandas as pd

'''
##########################
# Script for a SelectBox #
##########################
# "Text Intro: Select from a list"
features_available = ['Option1', 'Option2', 'Option3']
selected_choice = st.selectbox(label="What Feature doy ou want to analyze?",
                                options=features_available)
if selected_choice == 'Option1':
  "Conclusion1"
elif selected_choice == 'Option2':
  "Conclusion2"
else:
  "Conclusion3"
'''


#Will create a markdown:
#  '#' introduce a chapter mark.
#  '_' introduce an italic string.

st.markdown('''
'#' This is my lit Dashboard
Here is my first _tryout_.
''')


col1, buff, col2 = st.columns([1, .5, 3])

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs / 2.2046                 # calls `lbs` and stores it under `kg` after computation

def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg * 2.2046                 # calls `kg` and stores it under `lbs` after computation

with col1:
  pounds = st.number_input("Pounds", key='lbs', on_change= lbs_to_kg)

with col2:
  kilogram = st.number_input("Kilos", key='kg', on_change= kg_to_lbs)

'''
  on_change for input widgets like st.slider or st.number_input
  on_click for one-off widgets like st.button or st.form_submit_button
'''

st.write(app_train)
