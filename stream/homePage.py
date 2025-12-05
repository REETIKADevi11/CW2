import streamlit as st
from PIL import Image




st.title("MULTI-DOMAIN PLATFORM")
col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")
with col1:
    img = Image.open("main.png")
    st.image(img, width = 450)
with col2:
    st.write("Welcome to MULTI-DOMAIN PLATFORM")
    st.write("This platform allow you to analyse the data through chart")
    
st.write(">_If you are a new user - REGISTER_")
st.subheader("Steps to register yourself: ")
st.write("1. Go on the sidebar and click on register\n" 
             "2. Enter a valid username\n" 
             "3. Enter a strong password and confirm the password\n" 
             "4. Click on submit\n "
             "5. The Dashboard option will appear, then you choose which one you want to access.")


st.divider()

st.write(">_If you are an existing user - LOGIN_")
st.subheader("Steps for login: ")
st.write("1. Go on the sidebar and select login\n"
         "2. Enter the username name you enter for registration and the password\n"
         "3. Click on Login")



       









  
