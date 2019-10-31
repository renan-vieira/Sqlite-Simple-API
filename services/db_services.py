def add_person(client, person):
    """
    Performs an insert in database
    :param client: sqlite connection object
    :param person: a tuple with the person entry
    :return: status of commit into database
    """

    sql = 'INSERT INTO people (name, cpf) VALUES(?, ?)'
    print(sql)
    db_cursor = client.cursor()
    db_cursor.execute(sql, person)
    res = client.commit()

    return db_cursor.lastrowid


def get_person(client, id):
    """
    Query tasks by priority
    :param client: sqlite connection object
    :param id: the entry id (primary key) of the person to be retrieved
    :return:
    """
    cursor = client.cursor()
    cursor.execute("SELECT * FROM people WHERE id=?", (id,))

    row = cursor.fetchall()

    return row
