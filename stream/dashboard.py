import streamlit as st
import pandas as pd



st.title("Welcome to cyber Incident domain")
st.subheader("_Cyber_incident Table_")
st.set_page_config(page_title = "Cyber threat dashboard",
                   page_icon = ":bar_chart",
                   layout = "wide"
)

df = pd.read_csv("cyber_incidents.csv")


st.dataframe(df)
    

