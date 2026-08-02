import sqlite3

print("DATABASE.PY LOADED")
def create_users_table():
    print("FUNCTION STARTED")

    #st.write("DATABASE FILE LOADED")
    conn = sqlite3.connect("finsight.db")
    print(type(conn))
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER primary key
AUTOINCREMENT,
        USERNAME TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """) 
    print("COMMITTING...")
    conn.commit()
    print("SUCCESS")
    conn.close()