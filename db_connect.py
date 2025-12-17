import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="ProjectDB",
            user="postgres",
            password="",
            host="localhost",
            port="5433"
        )
        print("Connected to ProjectDB successfully.")
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None
