# 30 Days of Streamlit - https://30days.streamlit.app


import streamlit as st

st.title("Rahul's Days of Streamlit App Challenge",help="https://rahuls-first-app.streamlit.app/")

st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)

st.header('Day 3 - st.button')

if st.button('Hit to Submit'):
    st.write("Button clicked!")
else:
    st.write("Button not clicked yet.")

st.markdown("<hr style='border:1px solid blue'>", unsafe_allow_html=True)

import numpy as np
import altair as alt
import pandas as pd


st.header('Day 5 - st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.markdown("<hr style='border:1px solid blue'>", unsafe_allow_html=True)

st.header('Day 8 - st.slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.markdown("<hr style='border:1px solid blue'>", unsafe_allow_html=True)


st.header('Day 10 - st.selectbox')

# option = st.selectbox(
#      'What is your favorite color?',
#      ('Blue', 'Red', 'Green'))

# st.write('Your favorite color is ', option)

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

# Apply color formatting based on the selected option
if option == 'Blue':
    color = 'blue'
elif option == 'Red':
    color = 'red'
elif option == 'Green':
    color = 'green'

st.markdown(f"Your favorite color is <span style='color:{color};'>{option}</span>", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid blue'>", unsafe_allow_html=True)


st.header('Day 11 - st.multiselect')
options = st.multiselect(
     'What are your favorite colors?',
     ['Green', 'Yellow', 'Red', 'Blue'])

for option in options:
     if option == 'Blue':
         color = 'blue'
     elif option == 'Red':
         color = 'red'
     elif option == 'Green':
         color = 'green'
     st.markdown(f"Your favorite color is <span style='color:{color};'>{option}</span>", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid blue'>", unsafe_allow_html=True)

st.header('Day 12 - st.checkbox')

st.write("what would you like to order today ?")

ic=st.checkbox('Ice Cream')
cc=st.checkbox('Coke')
if ic:
    st.write("Ice Cream is selected")
if cc:
    st.write("Coke is selected")
st.markdown("<hr style='border:1px solid blue'>", unsafe_allow_html=True)

