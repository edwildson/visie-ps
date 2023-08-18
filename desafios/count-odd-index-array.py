"""
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array sum odd index - Os códigos nas demais linguagem podem ser encontrados em github.com:edwildson/visie-ps
"""

def count_strings_with_initial_equals_a_array(array):
    if not isinstance(array, list) or len(array) == 0:
        print('Entrada inválida.')
        return 0
    
    result = sum(val if index % 2 != 0 else 0 for index, val in enumerate(array))
    print('result:', result)
    
    return result

count_strings_with_initial_equals_a_array([22, 28, 33, 54, 14, 2, 76])
