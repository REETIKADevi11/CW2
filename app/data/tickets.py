from app.data.db import connect_database
import pandas as pd


def insert_tickets(conn, ticket_id, priority, status, assigned_to, created_at, resolution_time_hours):
    """Insert new datasets."""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO it_ticket
        (ticket_id, priority, status, assigned_to, created_at, resolution_time_hours)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (ticket_id, priority, status, assigned_to, created_at, resolution_time_hours))
    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()
    return ticket_id

def get_all_ticket():
#from CRUD operation here is the read part 
    conn = connect_database()
    df = pd.read_sql_query(
        "SELECT * it_ticket ORDER BY id DESC",
        conn
    )
    conn.close()
    return df

#from CRUD operation here is the update part 
def update_ticket_status(conn, ticket_id, new_status):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(""" UPDATE it_ticket SET status = ? WHERE ticket_id = ?""", (new_status, ticket_id))
    conn.commit()
    conn.close()
    return cursor.rowcount

#from CRUD operation here is the delete part 
def delete_ticket(conn, ticket_id):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM it_ticket WHERE ticket_id = ?"""(ticket_id))
    conn.commit()
    conn.close()
    return cursor.rowcount