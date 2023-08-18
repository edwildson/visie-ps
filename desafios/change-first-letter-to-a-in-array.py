"""
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Change first letter - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
"""


def change_first_letter_to_a_in_array(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        print('Entrada inválida.')
        return 0
    
    result = ['a' + string[1:] for string in arr]
    print('result:', result)
    
    return result

change_first_letter_to_a_in_array(['front-end', 'back-end', 'database'])