import os
import pandas as pd
import sqlite3
from app.data.db import connect_database
#creating user table 
def create_user_table():
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL UNIQUE,
                   password_hash TEXT NOT NULL,
                   role TEXT DEFAULT 'user' )""")
    conn.commit()
    conn.close()
    print("Well done! You have been able to create user table")
    
#creating cyber incident table
def create_cyber_incident_table():
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS cyber_incidents (incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   severity TEXT NOT NULL,
                   category  TEXT ,
                   status TEXT,
                   description TEXT,
                   reported_by TEXT,
                   date TEXT)""")
    conn.commit()
    print(" Cyber_incident table has been created successfully!")
    conn.close()
    #creating metadata table 
def create_datasets_metadata_table():
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS dataset_metadata (dataset_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                rows INTEGER,
                columns INTEGER,
                uploaded_by TEXT,
                upload_date TEXT
                   )""")
    conn.commit()
    print("Meta Table has been created successfully!")
    conn.close()
    #creating ticket table 
def create_it_tickets_table():
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS it_ticket(ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   priority TEXT ,
                   description TEXT,
                   status TEXT,
                   assigned_to TEXT,
                   resolved_date TEXT,
                   created_at TEXT,
                   resolution_time_hours REAL

                  
                    )""")


    conn.commit()
    print("IT table has been successfully !")
    conn.close()
#loading all the csv 
def load_csv_to_table(conn, csv_path, table_name):
    #check if csv exist or not 
    if not os.path.exists(csv_path):
        return 0
    df = pd.read_csv(csv_path)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()

    
    df.to_sql(name = table_name, con = conn, if_exists ="append", index = False)

    row_count = len(df)
    print(f"Inserted {row_count} rows into '{table_name}'.")
    return row_count
if __name__ == "__main__":
   
    conn = sqlite3.connect("DATA/intelligences_platform.db")
    


    # Call the function with your CSV file and table name
    rows = load_csv_to_table(conn, "DATA/cyber_incidents.csv", "cyber_incidents")
    rows_it = load_csv_to_table(conn, "DATA/it_tickets.csv", "it_ticket")
    rows_meta = load_csv_to_table(conn, "DATA/datasets_metadata.csv", "dataset_metadata")

    create_cyber_incident_table()
    create_it_tickets_table()
    create_datasets_metadata_table()

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM cyber_incidents;")
    print("Cyber rows:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM it_ticket;")
    print("IT rows:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM datasets_metadata;")
    print("datasets rows:", cursor.fetchone()[0])
    # Close connection
    conn.close()


