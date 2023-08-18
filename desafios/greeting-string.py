"""
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Greeting - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
"""
import re
import datetime

def remove_spaces(s):
    return s.strip()

def change_comma_to_exclamation(s):
    return s.replace(',', '!')

def greeting(s):
    hora = datetime.datetime.now().hour
    greet = ''

    if 0 <= hora < 12:
        greet = "Bom dia,"
    elif 12 <= hora < 18:
        greet = "Boa tarde,"
    else:
        greet = "Boa noite,"

    return re.sub(r'olá|Olá', greet, s)

def change_first_letter_to_a_in_string(string):
    if not isinstance(string, str):
        print('Entrada inválida.')
        return 0
    
    print('String antes: ', string)
    
    string = remove_spaces(string)
    string = change_comma_to_exclamation(string)
    string = greeting(string)
    
    print('result:', string)
    
    return string

change_first_letter_to_a_in_string(' Olá usuário, bem-vindo ao sistema  ')
