import psycopg2

conn = None
cursor = None

def init_db():
    global conn, cursor
    conn = psycopg2.connect(
        dbname="yourdbname",
        user="youruser",
        password="yourpassword",
        host="localhost"
    )
    cursor = conn.cursor()

def get_cursor():
    return conn, cursor
