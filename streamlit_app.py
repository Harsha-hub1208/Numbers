
import streamlit as st
import pandas as pd
st.header('Get the highest of the three numbers')
n1=st.number_input('Enter the first number: ')
n2=st.number_input('Enter the second number: ')
n3=st.number_input('Enter the third number: ')

st.subheader('Result)
if (n1>n2):
  if (n1>n3):
    st.write(n1)
  else:
    st.write(n3)
elif(n2> n3):
  st.write(n2)
else:
  st.write(n3)
