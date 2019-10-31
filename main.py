from flask import Flask, request, jsonify
from schema import SchemaError

from db_client.sqlite_client import create_connection, create_table
from exceptions.service_errors import ServiceError, ServiceBodyError
from views.views import INSERT_PERSON_SCHEMA, SELECT_PERSON_SCHEMA
from services.db_services import add_person, get_person

app = Flask(__name__)
app.debug = True
app.config['JSON_SORT_KEYS'] = False

sql_create_people_table = """ CREATE TABLE IF NOT EXISTS people (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        cpf text
                                    ); """

with app.app_context():
    sqlite_client = create_connection()
    create_table(sqlite_client, sql_create_people_table)


@app.errorhandler(ServiceError)
def service_errors(error):
    """
    It orchestrates application raised exceptions
    :param error: the raised error
    :return: a json with the message and status code
    """

    response = {'error': {'message': error.message, 'code': error.status_code}}

    return jsonify(response), error.status_code


@app.route('/insert_person', methods=['PUT'])
def insert_person():
    """
    Endpoint which inserts a new person register on database
    :return: An exception or a success message
    """
    body = request.get_json()

    try:
        INSERT_PERSON_SCHEMA.validate(body)
    except SchemaError as err:
        raise ServiceBodyError(str(err))

    with sqlite_client:
        person = (body.get('name'), body.get('cpf'))
        message = add_person(sqlite_client, person)

    return jsonify({'id': message})


@app.route('/select_person', methods=['GET'])
def select_person():
    """
    Endpoint which selects a registered person
    :return: An exception or a success message
    """
    body = request.get_json()

    try:
        SELECT_PERSON_SCHEMA.validate(body)
    except SchemaError as err:
        raise ServiceBodyError(str(err))

    with sqlite_client:
        message = get_person(sqlite_client, body.get('id'))

    return jsonify({'name': message[0][1], 'cpf': message[0][2]})


app.run(port=8080, host='0.0.0.0')
