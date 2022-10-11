import streamlit as st

st.session_state

if 'my_boolean' not in st.session_state:                                        # if the variable doesn't exist, it stores it
  st.session_state['my_boolean'] = True

if 'my_counter' not in st.session_state:                                        # if the variable doesn't exist, it stores it
  st.session_state['my_counter'] = 5

button = st.button("Update Values")

if button:
  "Before pressing Button:"
  st.write("  - The value of my counter is: ", st.session_state.my_counter)
  st.write("  - The value of my boolean is: ", st.session_state.my_boolean)

  st.session_state.my_counter += 1
  st.session_state.my_boolean = not st.session_state.my_boolean

  "After pressing Button:"
  st.write("  - The value of my counter is: ", st.session_state.my_counter)
  st.write("  - The value of my boolean is: ", st.session_state.my_boolean)

#for key in st.session_state.keys():
#  del st.session_state[key]

for items in st.session_state.items():                                          # to display all pairs (or .keys() or .values() for individual display)
  st.write(items)

