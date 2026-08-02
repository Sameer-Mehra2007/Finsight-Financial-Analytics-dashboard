import sqlite3
import bcrypt
print("AUTH FILE LOADED")
print(__file__)

DB_NAME ="finsight.db"

def signup(username,email,password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    try:
        cursor.execute(
            """
        INSERT INTO users(username, email, password)
        VALUES(?,?,?)
        """,
        (username, email, hashed)
        )

        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "Select password FROM USERS WHERE username=?",
        (username,)

    ) 
    user = cursor.fetchone()

    conn.close()

    if user:

        stored_hash = user[0]

        if bcrypt.checkpw(
            password.encode(),
            stored_hash.encode()
        ):
            return True

    return False           