"""
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array count strings that initiates with 'a' - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
"""

def count_strings_with_initial_equals_a_array(array):
    if not isinstance(array, list) or len(array) == 0:
        print('Entrada inválida.')
        return 0
    
    result = sum(1 for val in array if val.startswith('a'))
    print('result:', result)
    
    return result

count_strings_with_initial_equals_a_array(['front-end', 'angular', 'back-end', 'database', 'async'])

