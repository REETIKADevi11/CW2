import pandas as pd
from app.data.db import connect_database
from app.data.schema import create_cyber_incident_table
# this is the insert operation
def insert_incident(category, severity, status, description):
    """Insert new incident."""
    create_cyber_incident_table()
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cyber_incidents 
        (category, severity, status, description)
        VALUES (?, ?, ?, ?)
    """, ( category, severity, status, description))
    conn.commit()
    incident_id = cursor.lastrowid
    conn.close()
    return incident_id

#reading the table
def get_all_incidents():
    create_cyber_incident_table()
    """Get all incidents as DataFrame."""
    conn = connect_database()
    df = pd.read_sql_query(
        "SELECT * FROM cyber_incidents ORDER BY incident_id DESC",
        conn
       

    )
    print(df.to_string())
    conn.close()
    return df
#updating the table 
def update_incident_status( incident_id, new_status):
    create_cyber_incident_table()
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(""" UPDATE cyber_incidents SET status = ? WHERE incident_id = ?""", (new_status, incident_id))
    conn.commit()
    conn.close()
    return cursor.rowcount

#deleting data from the table
def delete_incident(incident_id):
    create_cyber_incident_table()
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cyber_incidents WHERE incident_id = ?",(int(incident_id),))
    conn.commit()
    conn.close()
    return cursor.rowcount

def get_incidents_by_type_count(conn):
    """
    Count incidents by type.
    Uses: SELECT, FROM, GROUP BY, ORDER BY
    """
    query = """
    SELECT category, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY category
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
    SELECT category, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY category
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

    

    