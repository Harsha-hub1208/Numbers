
import streamlit as st

st.set_page_config(page_title="Get the highest of the three numbers", page_icon":tada:")
st.header('User Input Parameters')
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
