"""
Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce()
"""
from functools import reduce


def product_of_odds(data):
    result = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)
    return result


print(product_of_odds([1, 3, 5, 6]))
