# Class containing helper method for interacting with player database


def user_exists(id):
    conn = psycopg2.connect("dbname=something user=someone")
    cur = conn.cursor()
    cur.execute("SELECT * FROM player WHERE id = %s;", (id))
    if cur.fetchone():
        return True
    else:
        return False


def get_user(id):
    print('return the name fo the user with the given id in the database')
    return "Mitchell"
