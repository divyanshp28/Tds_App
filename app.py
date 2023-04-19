#Importing streamlit
import streamlit as st

# defined a function to find the largest among three numbers

def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

# Setting the page title
st.set_page_config(page_title="Find the largest number")

# Title
st.title("Find the largest number")

# Taking thtree numbers as input
a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")

# Button to find the largest number
if st.button("Find the largest number"):
    largest = find_largest(a, b, c)
    st.success(f"The largest number is {largest}")
