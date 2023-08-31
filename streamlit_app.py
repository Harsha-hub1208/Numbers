
import streamlit as st

st.header('Get the highest of the three numbers')
n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))
n3=int(input('Enter the third number: '))


if (n1>n2):
  if (n1>n3):
    print(n1)
  else:
    print(n3)
elif(n2> n3):
  print(n2)
else:
  print(n3)
