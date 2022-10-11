import streamlit as st
import pandas as pd

st.title("Fabrice Dashboard 1.0")

st.markdown('This is my lit Dashboard')

evening_options = ['Rim', 'Baby Making', 'Private Garden']

"Selectbox from a list"

selected_choice = st.selectbox(label="What do you want to do tonight?",
                                options=evening_options)

if selected_choice == 'Rim':
  "I need to take a shower first"
elif selected_choice == 'Baby Making':
  "You won't be able to walk for an hour"
else:
  "I go get the KY, prepare yourself for a strong pounding"
