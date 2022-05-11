# result = list(map(lambda x: x.split(), ['a', 'a b', 'a b c']))
#
# print(result)
#
# high_ord_func = lambda x, func: x + func(x)
#
# result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)
#
# print(result)
"""
Требовалось написать программу, которая:

преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
находит произведение чисел из списка numbers.
Программист торопился и написал программу неправильно. Доработайте его программу.
"""
from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num ** 2, 1), floats))
filter_result = list(filter(lambda name: len(name) > 4 and (name == name[::-1]), words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
result = list(filter(lambda x: True, primes))
print(result)