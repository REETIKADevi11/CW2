from auth import login_user
import streamlit as st
from PIL import Image
from stream.dashboard import Dash, metaDash, ticketDash

# This is the Login pase
if "login" not in st.session_state:
    st.session_state.login = False 

if not st.session_state.login:
    with st.form("Login form"):
        st.header("Login form")
        img = Image.open("login.png")
        col1 , col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, width = 200)
        username = st.text_input("Enter username: ")
        password = st.text_input("Enter password: ", type = "password")
        submit_button = st.form_submit_button("Submit", type="primary")
        if submit_button:
            if not login_user(username, password):
                st.error("Username does not exist.")
                st.stop()
            if not username:
                st.error("Enter a username")
                st.stop()
    
            else: 
                st.success("you have succesfully login")
                st.session_state.login = True
 # the selection box will allow user to access which ever domain they want after login               
if st.session_state.login == True:
   option = ["Cyber Dashboard", "IT ticket", "Dataset dashboard"]
   st.header ("Select dashboard: ")
   dash_select = st.selectbox("## Which dashboard would you like to access ##", options = option)
   if dash_select == "Cyber Dashboard":
       Dash()
    
   elif dash_select == "IT ticket":
       ticketDash()
   elif dash_select == "Dataset dashboard":
       metaDash()

