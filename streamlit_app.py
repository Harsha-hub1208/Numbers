
import streamlit as st
import pandas as pd
st.header('Get the highest of the three numbers')
n1=st.number_input('Enter the first number: ')
n2=st.number_input('Enter the second number: ')
n3=st.number_input('Enter the third number: ')
return(max(n1,n2,n3))

if (n1>n2):
  if (n1>n3):
    print(n1)
  else:
    print(n3)
elif(n2> n3):
  print(n2)
else:
  print(n3)
