from auth import login_user
import streamlit as st
from PIL import Image


def Login():
  with st.form("Register: "):
    img = Image.open('login.png')
    st.image(img, width = 100)
    username = st.text_input("Enter the Username: ")
    password = st.text_input("Enter your password: ", type = 'password')
    submit_button = st.form_submit_button("Login")
    if submit_button:
          if login_user(username, password):
             st.success("You are login.")
      

