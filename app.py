import streamlit as st

# Title of the app
st.title("Welcome to Streamlit")

# Add some text
st.write("This is a simple web app with Streamlit.")

# Create an input box
name = st.text_input("Enter your name:")

# Display the input data
if st.button("Submit"):
    st.write(f"Hello, {name}!")
