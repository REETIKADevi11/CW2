from auth import validate_password
from auth import validate_username
import streamlit as st
from PIL import Image

def registration():
  with st.form("Register: "):
    img = Image.open('registration.png')
    st.image(img, width = 100)
    username = st.text_input("Enter the Username: ")
    password = st.text_input("Enter your password: ", type = 'password')
    confirm_password = st.text_input("Confirm password: ",type = 'password')
    submit_button = st.form_submit_button("Register")
    if submit_button:
      if validate_password(password):
        if validate_username(username):
          if confirm_password == password:
             st.success("You have been registered.")
      if not username:
        st.error("Please enter a username")
        st.stop()

      if not confirm_password:
        st.error("Enter the password correctly")
        st.stop
      
    





