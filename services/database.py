# Class containing helper methods for interacting with player database
from sql_database import database_connection


def user_exists(id):
    # Establish connection
    conn = database_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM player WHERE id = %s;", (id,))

    # Return True if id exists, False if id doesn't exist
    if cur.fetchone():
        cur.close()
        conn.close()
        return True
    else:
        cur.close()
        conn.close()
        return False


def get_user(id):
    # Establish connection
    conn = database_connection()
    cur = conn.cursor()

    # If user exists, return the user's codename
    if user_exists(id):
        cur.execute("SELECT * FROM player WHERE id = %s;", (id,))
        data = cur.fetchone()

        cur.close()
        conn.close()
        return data[3]
    # Else, return error statement
    else:
        cur.close()
        conn.close()
        return "ERROR: User does not exist!"


def add_user(id, codename):
    # Establish connection
    conn = database_connection()
    cur = conn.cursor()

    # If user already exists in the table, print error statement
    if user_exists(id):
        cur.close()
        conn.close()

        print("ERROR: User already exists!")
    # Else, add the player to the table
    else:
        cur.execute("INSERT INTO player (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s);",
                (id, None, None, codename))

        conn.commit()
        cur.close()
        conn.close()


def del_user(id):
    # Establish connection
    conn = database_connection()
    cur = conn.cursor()

    # If user exists in the table, delete them from the table
    if user_exists(id):
        cur.execute("DELETE FROM player WHERE id = %s;", (id,))

        conn.commit()
        cur.close()
        conn.close()
    # Else, print error statement
    else:
        cur.close()
        conn.close()
        print("ERROR: User does not exist!")
