import streamlit as st
import pandas as pd
from app.data.db import connect_database
from app.data.schema import create_cyber_incident_table, create_user_table, create_it_tickets_table, create_datasets_metadata_table
from app.data.incidents import insert_incident, delete_incident, get_all_incidents, update_incident_status
from app.data.tickets import get_all_ticket, insert_tickets, delete_ticket, update_ticket_status
from app.data.datasets import get_all_dataset, insert_datasets, delete_dataset, update_dataset_status
from PIL import Image
import plotly.express as px
create_user_table()
create_cyber_incident_table()
create_it_tickets_table()
create_datasets_metadata_table()

def Dash():
        st.set_page_config(page_title = "Cyber Threat dashboard", page_icon=":bar_chart:",layout="wide")
        col1, col2, col3 = st.columns([4,2,4])
        with col2:
          if st.button("Logout", type="primary"):
           st.session_state.login = False
           st.session_state.registering = False
           st.success("You have been logged out.")
           st.rerun()
        st.divider()
        img = Image.open("cyber incident .png")
        col1 , col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("Welcome to cyber Incident domain")
            st.image(img, width = 800)
        

        st.markdown("Turning the CRUD operation into interactive table")
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

        category_counts = df["category"].value_counts().reset_index()
        category_counts.columns = ["category", "count"]
        col1 , col2, col3 = st.columns([0.3, 2, 0.3])
        with col2:
           
           st.title(" :bar_chart: Bar chart")
         #implementation of bar chart and line chart 
           fig = px.bar(category_counts,
             x="category",
             y="count",
             color="category",
             color_discrete_sequence=["#7d57c9", "#280c61", "#7d9c03", "#7a6a9c"])
           st.plotly_chart(fig, width='stretch') 
        

           st.title(" :chart_with_upwards_trend: Line chart")
           st.line_chart(category_counts.set_index("category"))



        
#performing crud operation: insert, delete and update
        st.markdown("## Add Incident ##")

     
        with st.form ("Add new incident"):
            incident_id = st.text_input("Enter incident id")
            category = st.selectbox("Incident Type", ["Malware", "Phishing", "DDos","Misconfiguration", "Unauthorised access" ])
            severity = st.selectbox("severity", ["Low", "Medium", "High", "Critical"])
            status = st.selectbox("Status",["Open", "Closed", "In  progress", "Resolved"])
            description = st.text_input("Description")
            submitted = st.form_submit_button("submit", type="primary")
        if submitted:
            try:
               incident_id = int(incident_id)
               if incident_id <= 0:
                    raise ValueError("Incident ID must be positive")
               insert = insert_incident(incident_id, category, severity,status, description )
               if insert > 0:
                    st.success(" incident update")
               else:
                    st.warning("incident id not found")
                    st.rerun()
               
            except ValueError:
               st.error("Positive integer id should be a value")
            
            

        st.markdown("## Delete Incident ##")
        with st.form ("Delete incident"):
            incident_id = st.text_input("Incident ID to delete")
       
            submitted = st.form_submit_button("submit", type="primary")
        if submitted:
        
          try:
               incident_id = int(incident_id)
               deleted = delete_incident(int(incident_id))
               if deleted > 0 : 
                    st.success(" incident deleted")
               else:
                    st.warning("incident id not found")
                    st.rerun()
               
          except ValueError:
               st.error("Positive integer id should be a value")

        st.markdown("## Update Incident ##")
        with st.form ("update incident"):
            incident_id = st.text_input("Incident ID to update")
            new_status = st.selectbox("Status",["Open", "Closed", "In  progress", "Resolved"])
            description = st.text_input("Description: ")
            submitted = st.form_submit_button("submit", type="primary")

        if submitted:
            try:
               incident_id = int(incident_id)
               if incident_id <= 0:
                    raise ValueError("Incident ID must be positive")
               update = update_incident_status( incident_id, new_status, description)
               if update > 0:
                    st.success(" incident update")
               else:
                    st.warning("incident id not found")
                    st.rerun()
               
            except ValueError:
               st.error("Positive integer id should be a value")
            
            

        

            


                
#function for the dataset metadata domain

def metaDash():
    st.set_page_config(page_title = "Dataset metadata dashboard", page_icon=":bar_chart:",layout="wide")    
    
    col1, col2, col3 = st.columns([4,2,4])
    with col2:
          if st.button("Logout", type="primary"):
           st.session_state.login = False
           st.session_state.registering = False
           st.success("You have been logged out.")
           st.rerun()
    st.divider()
    
    st.subheader("_Datasets_metadata Table_")
    img = Image.open("metadata.png")
    col1 , col2, col3 = st.columns([1, 2, 1])
    with col2:
            st.title("Welcome to dataset_metadata domain")
            st.image(img, width = 800)
  #calling the Crud operation of dataset
    df = get_all_dataset()
    st.title("Dataset metadata")
    st.dataframe(df)
    
    st.markdown("##")
    col1, col2 = st.columns(2)
    with col1:
            st.metric("Total dataset", df.shape[0])
            st.metric("Total row", df["rows"].sum())
            st.metric("Total columns", df["columns"].sum())

    with col2:
        st.write("Uploaded By:")
        st.write(", ".join(df["uploaded_by"].astype(str).unique()))
        st.write("Upload Dates:")
        st.write(", ".join(df["upload_date"].astype(str).unique()))


    category_counts = df["uploaded_by"].value_counts().reset_index()
    category_counts.columns = ["uploaded_by", "count"]
    col1 , col2, col3 = st.columns([0.3, 2, 0.3])
    with col2:
        st.title(" Donut chart- Dataset - Metadata")
        fig = px.pie(category_counts,
             names="uploaded_by",
             values="count",
             hole=0.4, #implementing the donut effect
             color_discrete_sequence=["#1f77b4", "#ff7f0e", "#2ca02c"])
        st.plotly_chart(fig, width ='stretch')
        st.title(" :bar_chart: Bar chart")
        fig = px.bar(category_counts,
             x="uploaded_by",
             y="count",
             color="uploaded_by",
             color_discrete_sequence=["#1f77b4", "#ff7f0e", "#2ca02c"])
        st.plotly_chart(fig, width='stretch')



        
    
    # this is a form for inserting new data
    st.markdown("## Insert Incident ##")
    with st.form ("Add new metadata problem"):
        name = st.text_input("Enter new metadata problem ")
        rows = st.number_input("Rows number: ")
        columns = st.number_input("Columns number: ")
        uploaded_by = st.selectbox("Uploaded by",["it_admin", "data_scientist", "cyber_admin"])
        upload_date = st.date_input("upload Date")
        submitted = st.form_submit_button("submit")
    if submitted:
        dataset_id = insert_datasets(name, rows, columns, uploaded_by, str(upload_date))
        st.success(f"Metadata {dataset_id} inserted successfully!")
        st.rerun()

    st.markdown("## Delete ticket ##")
    with st.form ("Delete ticket"):
        dataset_id = st.text_input("dataset ID to delete")
        submitted = st.form_submit_button("submit")
    if submitted:
        delete_dataset(int(dataset_id))
        st.success("Ticket problem deleted")
        st.rerun()
        st.markdown("## Update Ticket ##") 
    st.markdown("## Update datasets ##")
    with st.form ("update datasets"):
          dataset_id = st.text_input(" datasets ID to update")
          rows = st.number_input("number: ")
          columns = st.number_input("Columns")
          uploaded_by = st.selectbox("uploaded_by",["it_admin", "data_scientist", "cyber_admin"])
          upload_date = st.date_input("Date: ")
          submitted = st.form_submit_button("submit", type="primary")

    if submitted:
          update_dataset_status(dataset_id, rows, columns, uploaded_by, upload_date)
          st.success("table updated")

          st.rerun()

    
    # function for IT ticket domain
def ticketDash():
    st.set_page_config(page_title = "IT ticket dashboard", page_icon=":bar_chart:",layout="wide")
        
    col1, col2, col3 = st.columns([4,2,4])
    with col2:
          if st.button("Logout", type="primary"):
           st.session_state.login = False
           st.session_state.registering = False
           st.success("You have been logged out.")
           st.rerun()
    st.divider()

    st.subheader("_IT Ticket Table_")
    img = Image.open("ticket.png")
    col1 , col2, col3 = st.columns([1, 2, 1])
    with col2:
            st.title("Welcome to IT ticket domain")
            st.image(img, width = 800)

    st.markdown("## IT Ticket table ##")
    #calling the crud operation for it ticket 
    df = get_all_ticket()
    st.dataframe(df)
   
      #implementation of filters      
    st.sidebar.header("Filter created table: ")
    assigned_to = st.sidebar.multiselect("Select the department",
        options = df["assigned_to"].unique(),
        default = df["assigned_to"].unique())
    df_ticket =df.query("assigned_to == @assigned_to")
    st.title("Filtered Table")
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
    priority_counts = df_ticket["assigned_to"].value_counts().reset_index()
    priority_counts.columns = ["assigned_to", "count"]
    col1 , col2, col3 = st.columns([0.3, 2, 0.3])
    with col2:
       st.title(" Pie chart - IT tickets problem")
       fig = px.pie(priority_counts,
             names="assigned_to",
             values="count",
             color_discrete_sequence=["#de0202", "#de7c7c", "#5e2828"])
       st.plotly_chart(fig, width ='stretch')
       st.title(" :bar_chart: Bar chart")
       fig = px.bar(priority_counts,
             x="assigned_to",
             y="count",
             color="assigned_to",
             color_discrete_sequence=["#5c32a8", "#8132a8", "#a832a0"])
       st.plotly_chart(fig, width='stretch')
        

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
          try:
               incident_id = int(ticket_id)
               deleted = delete_ticket(int(ticket_id))
               if deleted > 0:
                    st.success("Ticket problem deleted")
               else:
                    st.warning("ticket id not found")
                    st.rerun()
               
          except ValueError:
               st.error("Ticket id should be a value")

          
    st.markdown("## Update Ticket ##") 
       
    with st.form ("update ticket"):
          ticket_id = st.text_input(" ticket ID to update")
          new_status = st.selectbox("Status",["Open", "Closed", "In  progress", "Resolved"])
          description = st.text_input("Description: ")
          created_at = st.date_input("Date: ")
          resolution_time_hours = st.number_input("Resolution hour: ")
          submitted = st.form_submit_button("submit", type="primary")

    if submitted:
          update_ticket_status( ticket_id, new_status, description, created_at, resolution_time_hours)
          st.success("table updated")

          st.rerun()
          


    

   
    
    