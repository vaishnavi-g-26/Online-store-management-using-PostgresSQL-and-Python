# database.py
import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",          # PostgreSQL server
            database="online_store",   # your database name
            user="postgres",           # your PostgreSQL username
            password="your_password",  # your PostgreSQL password
            port="5432"                # default PostgreSQL port
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None
