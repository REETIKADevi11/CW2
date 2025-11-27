import streamlit as st
import pandas as pd
st.set_page_config(page_title = "Cyber Threat dashboard")

def Dash():
    st.title("Welcome to cyber Incident domain")
    st.subheader("_Cyber_incident Table_")
  
    df = pd.read_csv("DATA/cyber_incidents.csv")
    st.dataframe(df)
    st.sidebar.header("Filters")
    category = st.sidebar.multiselect(
       "Select the category:",
       options= df["category"].unique(),
       default= df["category"].unique())
    
    df_incidents = df[df["category"].isin(category)]

    st.title("Filtered Table")
    st.dataframe(df_incidents)

    st.title("BAR CHART: Incident Dashboard")
    st.markdown("##")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("High", df_incidents[df_incidents["severity"]=="High"].shape[0])
    with col2:
        st.metric(" Total Incidents", df_incidents["severity"].count(), "1")
        st.write("Incident Categories:")
        st.write(", ".join(df_incidents["category"].astype(str).unique()))

    severity_counts = df_incidents["severity"].value_counts().reset_index()
    severity_counts.columns = ["severity", "count"]
    st.bar_chart(severity_counts.set_index("severity"))

def metaDash():
    st.title("Welcome to dataset_metadata domain")
    st.subheader("_Datasets_metadata Table_")
  
    df = pd.read_csv("DATA/datasets_metadata.csv")
    st.dataframe(df)
    name = st.sidebar.multiselect("Select the name",
        options = df["name"].unique(),
                                  default = df["name"].unique())
    df_dataset =df.query("name == @name")
    st.dataframe(df_dataset)

    
    
def ticketDash():
    st.title("Welcome to IT ticket domain")
    st.subheader("_IT Ticket Table_")
  
    df = pd.read_csv("DATA/it_tickets.csv")
    st.dataframe(df)
    assigned_to = st.sidebar.multiselect("Select the department",
        options = df["assigned_to"].unique(),
                                  default = df["assigned_to"].unique())
    df_ticket =df.query("assigned_to == @assigned_to")
    st.dataframe(df_ticket)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("High", df_ticket[df_ticket["priority"]=="High"].shape[0])
        st.metric("Low", df_ticket[df_ticket["priority"]=="Low"].shape[0])
        st.metric("Medium", df_ticket[df_ticket["priority"]=="Medium"].shape[0])
        st.metric("Critical", df_ticket[df_ticket["priority"]=="Critical"].shape[0])
    with col2:
        st.metric(" Total: ", df_ticket["priority"].count(), "1")
        st.write("Department:")
        st.write(", ".join(df_ticket["assigned_to"].astype(str).unique()))

    priority_counts = df_ticket["priority"].value_counts().reset_index()
    priority_counts.columns = ["priority", "count"]
    st.bar_chart(priority_counts.set_index("priority"))

    

   
    
    