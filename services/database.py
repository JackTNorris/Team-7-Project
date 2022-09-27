# Class containing helper methods for interacting with player database
from sql_database import database_connection

# Global variables
conn = database_connection()
cur = conn.cursor()


def user_exists(id):
    cur.execute("SELECT * FROM player WHERE id = %s;", (id,))

    # Return True if id exists, False if id doesn't exist
    if cur.fetchone():
        return True
    else:
        return False


def get_user(id):
    # If user exists, return the user's codename
    if user_exists(id):
        cur.execute("SELECT * FROM player WHERE id = %s;", (id,))
        data = cur.fetchone()

        return data[3]
    # Else, return error statement
    else:
        return "ERROR: User does not exist!"


def add_user(id, codename):
    # If user already exists in the table, print error statement
    if user_exists(id):
        print("ERROR: User already exists!")
    # Else, add the player to the table
    else:
        cur.execute("INSERT INTO player (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s);",
                (id, None, None, codename))


def del_user(id):
    # If user exists in the table, delete them from the table
    if user_exists(id):
        cur.execute("DELETE FROM player WHERE id = %s;", (id,))
    # Else, print error statement
    else:
        print("ERROR: User does not exist!")
