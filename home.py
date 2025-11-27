import streamlit as st



home_page = st.Page(page = "stream/homePage.py",
                    title = "Home Page")

register_page = st.Page(page = "stream/registerPage.py",
                     title = "Register"
                     )

login_page = st.Page(page = "stream/LoginPage.py",
                     title = "Login")





pg = st.navigation({"Info":[home_page, register_page, login_page]})
pg.run()
