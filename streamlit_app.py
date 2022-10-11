import streamlit as st
import pandas as pd


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
