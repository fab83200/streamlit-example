import streamlit as st

st.subheader("Numerical Slider")
x = st.slider('Select a number to be squared:', 1, 10, key='my_slider', value=[2, 4])
st.write(x[0], 'squared is', x[0] * x[0])
st.write(x[1], 'squared is', x[1] * x[1])

st.subheader("Discrete Slider")
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', ]
first_color, second_color = st.select_slider(label='Select 2 colors',
                                      options=rainbow_colors,
                                      value=['orange', 'green'])
st.write(f"Your choice goes from {first_color} to {second_color}")

"st.session_state object:", st.session_state # store the state into a "key" then print it 

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

for key in st.session_state.keys():
  del st.session_state[key]

for items in st.session_state.items():                                          # to display all pairs (or .keys() or .values() for individual display)
  st.write(items)

