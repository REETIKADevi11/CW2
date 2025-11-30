import sqlite3
from pathlib import Path
DB_PATH = Path("DATA") / "intelligences_platform.db"
def connect_database(db_path = DB_PATH):
    conn = sqlite3.connect('DATA/intelligences_platform.db')
    return sqlite3.connect(str(db_path))









