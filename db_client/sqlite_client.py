import sqlite3


def create_connection():
    """ create a database connection to a SQLite database """
    try:
        client = sqlite3.connect('table.db', check_same_thread=False)
    except sqlite3.Error as e:
        print(e)

    return client


def create_table(client, create_table_sql):
    """ Create a sqlite table"""
    try:
        c = client.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)
