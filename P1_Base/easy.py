"""
На вход программе подаются два целых числа aa и bb. Напишите программу, которая выводит:

сумму чисел aa и bb;
разность чисел aa и bb;
произведение чисел aa и bb;
частное чисел aa и bb;
целую часть от деления числа aa на bb;
остаток от деления числа aa на bb;
корень квадратный из суммы их 10-х степеней
 .
Формат входных данных
На вход программе подаются два целых числа a и b !=0 каждое на отдельной строке.
"""
from math import sqrt

a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(sqrt(a**10 + b**10))

#  print(a+b, a-b, a*b, a/b, a//b, a%b, (a**10+b**10)**0.5, sep='\n')
