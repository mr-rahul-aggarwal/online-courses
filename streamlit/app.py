import streamlit as st

st.title("Rahul's Streamlit App")
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
