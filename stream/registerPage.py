import streamlit as st
from auth import validate_password, validate_username
from stream.dashboard import Dash, metaDash, ticketDash
from PIL import Image
from auth import register_user
from app.data.schema import create_user_table, create_cyber_incident_table, create_it_tickets_table

create_user_table()
create_cyber_incident_table()
create_it_tickets_table()

if "registering" not in st.session_state:
    st.session_state.registering = False 

if not st.session_state.registering:
    with st.form("Registration form"):
        st.header("Registration form")
        img = Image.open("registration.png")
        st.image(img, width = 100)
        username = st.text_input("Enter username: ")
        password = st.text_input("Enter password: ", type = "password")
        confirm_password = st.text_input("Re-enter password: ", type = "password")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if not validate_password(password):
                st.error("Enter a strong password.")
                st.stop()
            if not validate_username(username):
                st.error("Enter a valid username.")
                st.stop()
            if confirm_password != password:
                st.error("Password does not match.")
                st.stop()
            if not username:
                st.error("Enter a username")
                st.stop()
            if not confirm_password:
                st.error("confirm your password")
                st.stop()
            if not register_user(username, password):
                st.error("user already exist")
                st.stop()
    
            else: 
                st.success("you have been registered")
                st.session_state.registering = True
    

if st.session_state.registering == True:
    option = ["Cyber Dashboard","Dataset dashboard", "IT ticket"]
    st.header ("Select dashboard: ")
    dash_select = st.selectbox("Which dashboard would you like to access", options = option)
    if dash_select == "Cyber Dashboard":
       Dash()
    elif dash_select == "Dataset dashboard":
       metaDash()
    elif dash_select == "IT ticket":
       ticketDash()

    

           








