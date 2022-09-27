# Class containing helper method for interacting with player database
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
    cur.execute("SELECT * FROM player WHERE id = %s", (id,))
    data = cur.fetchone()

    # Return codename
    return data[3]
