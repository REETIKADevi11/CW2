from app.data.db import connect_database
import pandas as pd
from app.data.schema import create_datasets_metadata_table, load_csv_to_table


def insert_datasets( name, rows, columns, uploaded_by, upload_date):
    create_datasets_metadata_table()
    """Insert new datasets."""
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO dataset_metadata
        (name,  "rows", "columns", uploaded_by, upload_date)
        VALUES ( ?, ?, ?, ?, ?)
    """, (name, rows,columns, uploaded_by, upload_date))
    conn.commit()
    insert= cursor.lastrowid
    conn.close()
    return insert

def get_all_dataset():
    create_datasets_metadata_table()
#from CRUD operation here is the read part 
    conn = connect_database("DATA/intelligences_platform.db")

    df = pd.read_sql_query(
        "SELECT * FROM dataset_metadata ORDER BY dataset_id DESC",
        conn
    )
    
    print(df.to_string())
    conn.close()
    return df

#from CRUD operation here is the update part 
def update_dataset_status(conn, dataset_id, new_status):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(""" UPDATE dataset_metadata SET status = ? WHERE dataset_id = ?""", (new_status, dataset_id))
    conn.commit()
    update = cursor.rowcount
    conn.close()
    return update

#from CRUD operation here is the delete part 
def delete_dataset( dataset_id):
    conn = connect_database("DATA/intelligences_platform.db")
    cursor = conn.cursor()
    cursor.execute(" DELETE FROM dataset_metadata WHERE dataset_id = ?", (int(dataset_id),))
    conn.commit()
    delete = cursor.rowcount
    conn.close()
    return delete