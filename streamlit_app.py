import streamlit as st

st.subheader("Numerical Slider")                                    # creates a sub header
slider = st.slider('Select a number to be squared:',                # creates a slider with Intro Line: 'Select...' and the variable `slider`
              1,                                                    # slider min value
              10,                                                   # slider max value
              key='my_slider',                                      # names the slider 
              value=[2, 4])                                         # initiates the min and max starting values of the slider 
st.write(slider[0], 'squared is', slider[0] * slider[0])            # when activated, writes the resulting computation
st.write(slider[1], 'squared is', slider[1] * slider[1])            # when activated, writes the resulting computation


st.subheader("Discrete Slider")                                     # creates a sub header
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', ]   # instanciates the discrete values
first_color, second_color = st.select_slider(label='Select 2 colors',       # creates a select_slider with Intro Line: 'Select...' and the variables `1st` and `2nd`
                                              options=rainbow_colors,       # sets the options available
                                              key='my_rainbow',             # unique key for the select_slider widget
                                              on_change=None,               # optional callback invoked when this select_slider's value changes
                                              help='Choose 2 colors',       # optional tooltip that gets displayed next to the select slider
                                              value=['orange', 'green'])    # initiates the starting values
st.write(f"Your choice goes from {first_color} to {second_color}")  # when activated, writes the resulting choices

st.session_state                                                    # store the state into a "key" then print it 

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

