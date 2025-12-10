from app.data.db import connect_database
import pandas as pd
from app.data.schema import create_it_tickets_table, load_csv_to_table

def insert_tickets( priority, description, status, assigned_to, created_date ,resolution_time_hours ):
    create_it_tickets_table()

    """Insert new datasets."""
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO it_ticket
        (priority,description, status, assigned_to,created_at,resolution_time_hours)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ( priority,description, status, assigned_to, created_date, resolution_time_hours))
    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()
    return ticket_id

def get_all_ticket():
    create_it_tickets_table()
   
#from CRUD operation here is the read part 
    conn = connect_database("DATA/intelligences_platform.db")
    
    df = pd.read_sql_query(
        "SELECT * FROM it_ticket ORDER BY ticket_id DESC",
        conn
    )
    print(df.to_string())
    conn.close()
    return df

#from CRUD operation here is the update part 
def update_ticket_status(ticket_id, new_status, description, created_at, resolution_time_hours):
    create_it_tickets_table()
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""UPDATE it_ticket SET status = ?, description = ?, created_at = ?, resolution_time_hours = ? WHERE ticket_id = ?""", (new_status,description, created_at, resolution_time_hours, ticket_id))
    conn.commit()
    update = cursor.rowcount
    conn.close()
    return update

#from CRUD operation here is the delete part 
def delete_ticket(ticket_id):
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM it_ticket WHERE ticket_id = ?""", (int(ticket_id),))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted