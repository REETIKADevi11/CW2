from app.data.db import connect_database
import pandas as pd


def insert_datasets(conn, dataset_id, name, rows, columns, uploaded_by, upload_date):
    """Insert new datasets."""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datasets_metadata
        (dataset_id, category, name, , rows, columns, uploaded_by, upload_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (dataset_id, name, rows,columns, uploaded_by, upload_date))
    conn.commit()
    dataset_id = cursor.lastrowid
    conn.close()
    return dataset_id

def get_all_dataset():
#from CRUD operation here is the read part 
    conn = connect_database()
    df = pd.read_sql_query(
        "SELECT * datasets_metadata ORDER BY dataset_id DESC",
        conn
    )
    conn.close()
    return df

#from CRUD operation here is the update part 
def update_dataset_status(conn, dataset_id, new_status):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(""" UPDATE datasets_metadata SET status = ? WHERE dataset_id = ?""", (new_status, dataset_id))
    conn.commit()
    conn.close()
    return cursor.rowcount

#from CRUD operation here is the delete part 
def delete_dataset(conn, dataset_id):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM datasets_metadata WHERE dataset_id = ?"""(dataset_id))
    conn.commit()
    conn.close()
    return cursor.rowcount