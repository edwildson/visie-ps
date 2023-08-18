"""
    Created by Edwildson Coelho Rodrigues
    https://edwildson.dev
    https://github.com/edwildson
    https://www.linkedin.com/in/edwildson/

    Array Average
"""

def average(array):
    count = len(array)

    return sum(array) / count

def count_average_item_array(array):
    if not isinstance(array, list) or len(array) == 0:
        print('Entrada inválida.')
        return 0

    avg = average(array)

    result = sum(1 for val in array if val > avg)
    print('result:', result)

    return result

count_average_item_array([22, 28, 33, 54, 14, 2, 76])
