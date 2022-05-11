"""
На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк
треугольника Паскаля.
"""
import math


def pascal(n):
    row = []
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        for i in range(n+1):
            element = math.factorial(n)/(math.factorial(i)*math.factorial(n-i))
            row.append(int(element))
        return row


n = int(input())

for j in range(n):
    print(*pascal(j))


