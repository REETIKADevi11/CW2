import streamlit as st
import pandas as pd
from app.data.db import connect_database
from app.data.schema import create_cyber_incident_table, create_user_table, create_it_tickets_table, create_datasets_metadata_table
from app.data.incidents import insert_incident, delete_incident, get_all_incidents, update_incident_status
from app.data.tickets import get_all_ticket, insert_tickets, delete_ticket, update_ticket_status
from app.data.datasets import get_all_dataset, insert_datasets, delete_dataset
from PIL import Image
create_user_table()
create_cyber_incident_table()
create_it_tickets_table()
create_datasets_metadata_table()

def Dash():
        st.set_page_config(page_title = "Cyber Threat dashboard", page_icon=":bar_chart:",layout="wide")
    
        
        st.title("Welcome to cyber Incident domain")
        img = Image.open("cyber incident .png")
        st.image(img, width = 250)
        st.markdown("This is the CSV file")
        #implementing the csv in order to do the analysis of the table"
        st.subheader("_Cyber_incident Table_")
        df = pd.read_csv("DATA/cyber_incidents.csv")
        st.dataframe(df)
        
        st.title("BAR CHART: Incident Dashboard")
        st.markdown("##")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("High", df[df["severity"]=="High"].shape[0])
            st.metric("Low", df[df["severity"]=="Low"].shape[0])
            st.metric("Medium", df[df["severity"]=="Medium"].shape[0])
            st.metric("Critical", df[df["severity"]=="Critical"].shape[0])
        with col2:
           st.metric(" Total Incidents", df["severity"].count(), "1")
           st.write("Incident Categories:")
           st.write(", ".join(df["category"].astype(str).unique()))

        severity_counts = df["severity"].value_counts().reset_index()
        severity_counts.columns = ["severity", "count"]
        st.title(" :bar_chart: Bar chart")
        #implementation of bar chart and line chart 
        st.bar_chart(severity_counts.set_index("severity"))

        st.title(" :chart_with_upwards_trend: Line chart")
        st.line_chart(severity_counts.set_index("severity"))
   
        st.markdown("Turning the CRUB operation into interactive table")
        #the created table in the schema.py is called when implementing the function get_all_incident()
        df = get_all_incidents()
        st.dataframe(df)
       
        st.sidebar.header("Filters")
        category = st.sidebar.multiselect("Select the category:",
                                          options= df["category"].unique(),
                                          default= df["category"].unique())
        df_incidents = df[df["category"].isin(category)]

        st.title("Filtered Table")
        
        st.dataframe(df_incidents)

        st.title("BAR CHART: Incident Dashboard")
    # implementation of filters, this allow user to analyse the table 
        st.markdown("## Modified table ##")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("High", df_incidents[df_incidents["severity"]=="High"].shape[0])
            st.metric("Low", df_incidents[df_incidents["severity"]=="Low"].shape[0])
            st.metric("Medium", df_incidents[df_incidents["severity"]=="Medium"].shape[0])
            st.metric("Critical", df_incidents[df_incidents["severity"]=="Critical"].shape[0])
        with col2:
           st.metric(" Total Incidents", df_incidents["severity"].count(), "1")
           st.write("Incident Categories:")
           st.write(", ".join(df_incidents["category"].astype(str).unique()))

        severity_counts = df_incidents["severity"].value_counts().reset_index()
        severity_counts.columns = ["severity", "count"]
        st.title(" :bar_chart: Bar chart")
        st.bar_chart(severity_counts.set_index("severity"))

        st.markdown("## Line chart ##")    
        
        st.title(" :chart_with_upwards_trend: Line chart")
        st.line_chart(severity_counts.set_index("severity"))

        
#performing crud operation: insert, delete and update
        st.markdown("## Add Incident ##")

     
        with st.form ("Add new incident"):
           
            category = st.selectbox("Incident Type", ["Malware", "Phishing", "DDos","Misconfiguration", "Unauthorised access" ])
            severity = st.selectbox("severity", ["Low", "Medium", "High", "Critical"])
            status = st.selectbox("Status",["Open", "Closed", "In  progress", "Resolved"])
            description = st.text_input("Description")
            submitted = st.form_submit_button("submit")
        if submitted:
            insert_incident(category, severity,status, description )
            st.success("Incident added")
            st.rerun()

        st.markdown("## Delete Incident ##")
        with st.form ("Delete incident"):
            incident_id = st.text_input("Incident ID to delete")

       
            submitted = st.form_submit_button("submit")
        if submitted:
             delete_incident(int(incident_id))
             st.success("Incident deleted")
             st.rerun()
        

        st.markdown("## Update Incident ##")
        with st.form ("update incident"):
            incident_id = st.text_input("Incident ID to update")
            new_status = st.selectbox("Status",["Open", "Closed", "In  progress", "Resolved"])
            submitted = st.form_submit_button("submit")

        if submitted:
            update_incident_status( incident_id, new_status)
            st.success("table updated")
            st.rerun()

            


                


def metaDash():
    st.title("Welcome to dataset_metadata domain")
    st.subheader("_Datasets_metadata Table_")
    img = Image.open("metadata.png")
    st.image(img, width = 250)
  
    df = get_all_dataset()
    st.dataframe(df)
    st.markdown("## Metadata Problem ##")

    with st.form ("Add new metadata problem"):
        name = st.text_input("Enter new metadata problem ")
        rows = st.number_input("Rows number: ")
        columns = st.number_input("Columns number: ")
        uploaded_by = st.selectbox("Uploaded by",["it_admin", "data_scientist", "cyber_admin"])
        upload_date = st.date_input("upload Date")
        submitted = st.form_submit_button("submit")
    if submitted:
        dataset_id = insert_datasets(name, rows, columns, uploaded_by, upload_date)
        st.success(f"Metadata {dataset_id} inserted successfully!")
        st.rerun()

    st.markdown("## Delete Incident ##")
    with st.form ("Delete incident"):
        dataset_id = st.text_input("dataset ID to delete")
        submitted = st.form_submit_button("submit")
    if submitted:
        delete_dataset(int(dataset_id))
        st.success("Ticket problem deleted")
        st.rerun()

    
    
def ticketDash():
    st.set_page_config(page_title = "IT ticket dashboard", page_icon=":bar_chart:",layout="wide")
    st.title("Welcome to IT ticket domain")
    st.subheader("_IT Ticket Table_")
    img = Image.open("ticket.png")
    st.image(img, width = 250)
    st.markdown("This is the CSV file")
    st.subheader("_IT Ticket Table_")
    df = pd.read_csv("DATA/it_tickets.csv")
    st.dataframe(df)
    st.divider()
        
    st.sidebar.header("Filter csv table: ")
    assigned_to = st.sidebar.multiselect("Select the department",
        options = df["assigned_to"].unique(),
        default = df["assigned_to"].unique())
    df_ticket =df.query("assigned_to == @assigned_to")
    st.write("Filter table:")
    st.dataframe(df_ticket)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("High", df_ticket[df_ticket["priority"]=="High"].shape[0])
        st.metric("Low", df_ticket[df_ticket["priority"]=="Low"].shape[0])
        st.metric("Medium", df_ticket[df_ticket["priority"]=="Medium"].shape[0])
        st.metric("Critical", df_ticket[df_ticket["priority"]=="Critical"].shape[0])
    with col2:
        st.metric(" Total: ", df_ticket["priority"].count(), "1")
        st.write("Department:")
        st.write(", ".join(df_ticket["assigned_to"].astype(str).unique()))
    with col3:
        total_resolution = df_ticket["resolution_time_hours"].sum()
        st.metric("Total Resolution hours", total_resolution)

        

    priority_counts = df_ticket["priority"].value_counts().reset_index()
    priority_counts.columns = ["priority", "count"]
    st.title(" :bar_chart: Bar chart")
    st.bar_chart(priority_counts.set_index("priority"))
    st.markdown("## Line chart ##") 
    st.title(" :chart_with_upwards_trend: Line chart")   
    st.line_chart(priority_counts.set_index("priority"))
    st.divider()

    st.markdown("## Add ticket problem ##")
    df = get_all_ticket()
    st.dataframe(df)
   
            
    st.sidebar.header("Filter created table: ")
    assigned_to = st.sidebar.multiselect("Select the department",
        options = df["assigned_to"].unique(),
        default = df["assigned_to"].unique())
    df_ticket =df.query("assigned_to == @assigned_to")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("High", df_ticket[df_ticket["priority"]=="High"].shape[0])
        st.metric("Low", df_ticket[df_ticket["priority"]=="Low"].shape[0])
        st.metric("Medium", df_ticket[df_ticket["priority"]=="Medium"].shape[0])
        st.metric("Critical", df_ticket[df_ticket["priority"]=="Critical"].shape[0])
    with col2:
        st.metric(" Total: ", df_ticket["priority"].count(), "1")
        st.write("Department:")
        st.write(", ".join(df_ticket["assigned_to"].astype(str).unique()))
    with col3:
        total_resolution = df_ticket["resolution_time_hours"].sum()
        st.metric("Total Resolution hours", total_resolution)

        

    priority_counts = df_ticket["priority"].value_counts().reset_index()
    priority_counts.columns = ["priority", "count"]
    
    st.title(" :bar_chart: Bar chart")
    st.bar_chart(priority_counts.set_index("priority"))
    st.markdown("## Line chart ##")    
    
    st.title(" :chart_with_upwards_trend: Line chart")
    st.line_chart(priority_counts.set_index("priority"))
    st.markdown("## Add IT Incident ##")
    with st.form ("Add new ticket problem"):
          description = st.text_input("Enter new ticket problem ")
          assigned_to = st.selectbox("assigned_to ", ["IT_Support_A", "IT_Support_B","IT_Support_C"])
          priority = st.selectbox("priority", ["Low", "Medium", "High", "Critical"])
          status = st.selectbox("Status",["Open", "Closed", "In  progress", "Resolved"])
          resolution_time_hours = st.number_input("resolution_time_hours: ")
          created_date = st.date_input("Created Date")
          submitted = st.form_submit_button("submit", type="primary")
    if submitted:
          ticket_id = insert_tickets(priority, description, status, assigned_to, created_date, resolution_time_hours)
          st.success(f"Ticket {ticket_id} inserted successfully!")
          st.rerun()


    
   
    st.markdown("## Delete Incident ##")
    with st.form ("Delete incident"):
          ticket_id = st.text_input("Incident ID to delete")
          submitted = st.form_submit_button("submit", type="primary")
    if submitted:
          delete_ticket(int(ticket_id))
          st.success("Ticket problem deleted")
          st.rerun()
          

   
    st.markdown("## Update Ticket ##") 
       
    with st.form ("update ticket"):
          ticket_id = st.text_input(" ticket ID to update")
          new_status = st.selectbox("Status",["Open", "Closed", "In  progress", "Resolved"])
          submitted = st.form_submit_button("submit", type="primary")

    if submitted:
          update_incident_status( ticket_id, new_status)
          st.success("table updated")

          st.rerun()
          


    

   
    
    