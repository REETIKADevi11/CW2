
from stream.registerPage import registration
from stream.LoginPage import Login
import streamlit as st
from PIL import Image

st.header("_Welcome to MULTI-DOMAIN PLATFORM_")
img = Image.open("main.png")
st.image(img, width = 300)

def show_register_page():
    registration()
st.write(">_If you are a new user register yourself first._")
if st.button("Register"):
    show_register_page()

st.divider()

def show_log():
    Login()

st.write(" >_If you are a registered user - login_")
if st.button("Login"):
    show_log()





  
