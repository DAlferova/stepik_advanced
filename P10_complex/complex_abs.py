"""
Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число с
наибольшим модулем и сам модуль числа на отдельных строках.

Примечание. Модуль комплексного числа можно вычислить с помощью встроенной функции abs().
print(max(numbers, key=abs))
print(abs(max(numbers, key=abs)))
"""
import cmath
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j,
           -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

abs_numbers = {abs(z): z for z in numbers}
max_abs = max(abs_numbers)

print(abs_numbers[max_abs])
print(max_abs)

