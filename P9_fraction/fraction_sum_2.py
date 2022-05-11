"""
Сумма дробей 2
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет и выводит рациональное число,
 равное значению выражения
"""
from fractions import Fraction
from math import factorial as ff
n = int(input())
result = 0
for i in range(1, n + 1):
    result += Fraction(f'1/{ff(i)}')
print(result)
