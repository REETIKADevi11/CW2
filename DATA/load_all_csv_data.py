import pandas as pd
import sqlite3
import os
from app.data.db import connect_database

def load_csv_to_table(conn, csv_path, table_name):

    conn = sqlite3.connect("intelligence_platform.db")
    if not os.path.exists(csv_path = "cyber_incident.csv"):
       df = pd.read_csv("cyber_incidents.csv")
       df.to_sql(name = table_name, con = conn, if_exists = 'append', index = False)
       print("Well Done! You have successfully load the cyber incident csv")
    elif not os.path.exists(csv_path= "datasets_metadata.csv"):
       df = pd.read_csv("datasets_metadata.csv")
       df.to_sql(name = table_name, con = conn, if_exists = 'append', index = False)
       print("Well Done! You have successfully load the datasets_metadata csv")
    elif not os.path.exists(csv_path= "it_ticket.csv"):
       df = pd.read_csv("it_tickets.csv")
       df.to_sql(name = table_name, con = conn, if_exists = 'append', index = False)
       print("Well Done! You have successfully load the it_ticket csv")
       
    row_count = len(df)
    return row_count
def get_incidents_by_type_count(conn):
    """
    Count incidents by type.
    Uses: SELECT, FROM, GROUP BY, ORDER BY
    """
    query = """
    SELECT incident_type, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY incident_type
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn)
    return df

def get_high_severity_by_status(conn):
    """
    Count high severity incidents by status.
    Uses: SELECT, FROM, WHERE, GROUP BY, ORDER BY
    """
    query = """
    SELECT status, COUNT(*) as count
    FROM cyber_incidents
    WHERE severity = 'High'
    GROUP BY status
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn)
    return df

def get_incident_types_with_many_cases(conn, min_count=5):
    """
    Find incident types with more than min_count cases.
    Uses: SELECT, FROM, GROUP BY, HAVING, ORDER BY
    """
    query = """
    SELECT incident_type, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY incident_type
    HAVING COUNT(*) > ?
    ORDER BY count DESC
    """
    df = pd.read_sql_query(query, conn, params=(min_count,))
    return df

# Test: Run analytical queries
conn = connect_database()

print("\n Incidents by Type:")
df_by_type = get_incidents_by_type_count(conn)
print(df_by_type)

print("\n High Severity Incidents by Status:")
df_high_severity = get_high_severity_by_status(conn)
print(df_high_severity)

print("\n Incident Types with Many Cases (>5):")
df_many_cases = get_incident_types_with_many_cases(conn, min_count=5)
print(df_many_cases)

conn.close()

    


    
    

    
    
    

