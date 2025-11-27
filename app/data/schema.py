import os
import pandas as pd
import sqlite3
def create_user_table(conn):
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL UNIQUE,
                   password_hash TEXT NOT NULL,
                   role TEXT DEFAULT 'user' )""")
    conn.commit()
    print("Well done! You have been able to create user table")

def create_cyber_incident_table(conn):
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS cyber_incident (incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   severity TEXT NOT NULL,
                   category TEXT ,
                   status TEXT,
                   description TEXT,
                   reported_by TEXT (username of reporter),
                   date TEXT (format: YYYY-MM-DD))""")
    conn.commit()
    print(" Cyber_incident table has been created successfully!")
    conn.close()
def create_datasets_metadata_table(conn):
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS datasets_metadata (dataset_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   category TEXT,
                   source TEXT, 
                   last_updated TEXT,
                   record_count INTEGER,
                   file_size_mb REAL,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    conn.commit()
    print("Meta Table has been created successfully!")
    conn.close()
def create_it_tickets_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE it_ticket(id PRIMARY KEY AUTOINCREMENT,
                   ticket_id TEXT UNIQUE NOT NULL,
                   priority TEXT ,
                   description TEXT,
                   status TEXT,
                   assigned_to TEXT,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   resolved_date TEXT,
                   created_date TEXT,
                   subject TEXT NOT NULL
                    )""")
    conn.commit()
    print("IT table has been successfully !")

    conn.close()

def load_csv_to_table(conn, csv_path, table_name):
    if not os.path.exists(csv_path):
        return 0
    df = pd.read_csv(csv_path)

    row_count = len(df)
    print(f"Inserted {row_count} rows into '{table_name}'.")
    return row_count
if __name__ == "__main__":
    # Connect to SQLite database (or replace with your DB connection)
    conn = sqlite3.connect("intelligence_platform.db")

    # Call the function with your CSV file and table name
    rows = load_csv_to_table(conn, "DATA/cyber_incidents.csv", "create_cyber_incident_table")

    # Close connection
    conn.close()


