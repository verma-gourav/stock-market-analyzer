import sqlite3
import os

def get_connection():
    db_path = os.path.join("db", "market_data.db")
    return sqlite3.connect(db_path)