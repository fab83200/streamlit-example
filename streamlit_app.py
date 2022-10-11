import streamlit as st
import pandas as pd

#Will create a markdown:
#  '#' introduce a chapter mark.
#  '_' introduce an italic string.

# This is my lit Dashboard
Here is my first _tryout_.


col1, buff, col2 = st.columns([2, .5, 2])                             # sets up columns of standard width where sum is the total width

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs / 2.2046                 # calls `lbs` and stores it under `kg` after computation

def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg * 2.2046                 # calls `kg` and stores it under `lbs` after computation

with col1:
  pounds = st.number_input("Pounds",                                  # Name of the number_input
                           key='lbs',                                 # Name of the variable for the data
                           on_change= lbs_to_kg)                      # Name of the function to use `on_change`, it would be `on_click` for one-off widgets

with col2:
  kilogram = st.number_input("Kilos",                                 # Name of the number_input
                             key='kg',                                # Name of the variable for the data
                             on_change= kg_to_lbs)                    # Name of the function to use `on_change`, it would be `on_click` for one-off widgets
