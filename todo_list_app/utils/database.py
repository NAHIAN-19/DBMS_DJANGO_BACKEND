import psycopg2

HOST = "localhost"
DB_NAME = "todo_list"
USER = "Admin"
PASSWORD = "baBualAmin1985"
PORT = 1919

def create_connection():
    try:
        conn = psycopg2.connect(
            host=HOST,
            database=DB_NAME,
            user=USER,
            password=PASSWORD,
            port=PORT
        )
        return conn
    except (psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return psycopg2.connect(
            host=HOST,
            database=DB_NAME,
            user=USER,
            password=PASSWORD,
            port=PORT
        )

conn = create_connection()
cur = conn.cursor()
Error = psycopg2.Error
