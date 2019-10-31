import re
from schema import Schema, And

CPF_REGEX = r'^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$'

INSERT_PERSON_SCHEMA = Schema({
    'name': And(str, error='name should be a string'),
    'cpf': And(And(str, error='cpf should be a string'),
               And(lambda s: re.match(CPF_REGEX, s),
                   error='Invalid cpf'))
})

SELECT_PERSON_SCHEMA = Schema({'id': And(int, error='name should be an integer')})
