import sqlite3
def create_user_table(conn):
    conn = sqlite3.connect('intelligences_platform.db')
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
                   reported_by: TEXT (username of reporter),
                   date: TEXT (format: YYYY-MM-DD))""")
    conn.commit()
    print(" Cyber_incident table has been created successfully!")
    
def create_datasets_metadata_table(conn):
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXIST dataset_id (dataset_id PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   category TEXT,
                   source TEXT, 
                   last_updated TEXT,
                   record_count INTEGER,
                   file_size_mb REAL,
                   created_at TIMESTAMP DDEFAULT CURRENT_TIMESTAMP)""")
    conn.commit()
    print("Meta Table has been created successfully!")

def create_it_tickets_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE it_ticket(id PRIMARY KEY AUTHOINCREMENT,
                   ticket_id TEXT UNIQUE NOT NULL,
                   priority TEXT ,
                   description TEXT,
                   status TEXT,
                   assigned_to TEXT,
                   created_at TIMESTAMP DEFAULT CURRETN_TIMESTAMP,
                   resolved_date TEXT,
                   created_date TEXT,
                   sunject TEXT NOT NULL
                    )""")
    conn.commit()
    print("IT table has been successfully !")
    