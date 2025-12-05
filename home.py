import streamlit as st
from app.data.schema import create_user_table, create_cyber_incident_table, create_it_tickets_table, create_datasets_metadata_table



create_user_table()
create_cyber_incident_table()
create_it_tickets_table()
create_datasets_metadata_table()



home_page = st.Page(page = "stream/homePage.py",
                    title = "Home Page")

register_page = st.Page(page = "stream/registerPage.py",
                     title = "Register"
                     )

login_page = st.Page(page = "stream/LoginPage.py",
                     title = "Login")

api_page = st.Page(page = "stream/gemini_api_streamlit.py",
                   title = "AI assistant")



pg = st.navigation({"Info":[home_page, register_page, login_page, api_page]})
pg.run()
