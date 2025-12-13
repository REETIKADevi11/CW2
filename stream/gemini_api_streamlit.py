import streamlit as st
from google import genai
from google.genai import types
from app.data.incidents import get_all_incidents
from app.data.tickets import get_all_ticket
if "login" not in st.session_state:
    st.session_state.login = False


if not st.session_state.login:
    st.warning("You must login to access the AI analyser")
    st.stop()
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


st.subheader("Gemini API")

#implementing ai analyser for cyber incident
incidents = get_all_incidents()
if not incidents.empty:
    incidents_options = [f"{row["incident_id"]}: {row["category"]}- {row["severity"]}"
                         for index, row in incidents.iterrows()]
    selected_id = st.selectbox("Select incident to analyse:",
                               range(len(incidents)),
                               format_func = lambda i: incidents_options[i])
    incident = incidents.iloc[selected_id]
    st.subheader("Incident details")
    st.write(f"**Type:** {incident["category"]}")
    st.write(f"**Severity:** {incident["severity"]}")
    st.write(f"**Description:** {incident["description"]}")
    st.write(f"**Status:** {incident["status"]}")
if st.button("Analyse with AI",type="primary"):
    with st.spinner("AI analysing incident..."):
        analysis_prompt = f"""Analyse this cyber security incident:
        Type: {incident['category']}
        Severity: {incident['severity']}
        Description: {incident['description']}
        Status: {incident['status']}

         Provide:
         1.Root cause analysis
         2.Immediate actions needed
         3.Long term prevention measures"""
        response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a cybersecurity expert. Your name is cyber."),
        contents={"parts": [{"text": analysis_prompt}]},)

        st.subheader("AI analysis")
        container = st.empty()
        full_reply = ""
        for chunk in response:
            full_reply += chunk.text
            container.markdown(full_reply)
st.divider()
st.divider()            

#implementing ai analyser for tickets
tickets = get_all_ticket()
if not tickets.empty:
    tickets_option = [f"{row["ticket_id"]}: {row["assigned_to"]}- {row["priority"]}"
                         for index, row in tickets.iterrows()]
    selected_id = st.selectbox("Select department  to analyse:",
                               range(len(tickets)),
                               format_func = lambda i: tickets_option[i])
    ticket = tickets.iloc[selected_id]
    st.subheader("ticket details")
    st.write(f"**Type:** {ticket["assigned_to"]}")
    st.write(f"**Severity:** {ticket["priority"]}")
    st.write(f"**Description:** {ticket["description"]}")
    st.write(f"**Status:** {ticket["status"]}")
if st.button("Analyse with AI"):
    with st.spinner("AI analysing tickets..."):
        analysis_prompt = f"""Analyse this ticket problem:
        Type: {ticket['assigned_to']}
        Severity: {ticket['priority']}
        Description: {ticket['description']}
        Status: {ticket['status']}

         Provide:
         1.Root cause analysis
         2.Immediate actions needed
         3.Long term prevention measures"""
        response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a IT expert. Your name is tech."),
        contents={"parts": [{"text": analysis_prompt}]},)

        st.subheader("AI analysis")
        container = st.empty()
        full_reply = ""
        for chunk in response:
            full_reply += chunk.text
            container.markdown(full_reply)





      

    

