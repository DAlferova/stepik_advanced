"""
Сократите дробь
Даны два натуральных числа mm и nn. Напишите программу, которая сокращает дробь и выводит ее.
Sample Input 1:

3
6
Sample Output 1:

1/2
"""
from fractions import Fraction

print(Fraction(int(input()), int(input())))

