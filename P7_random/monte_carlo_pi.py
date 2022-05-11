"""
Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа \piπ.
Примечание 1. Площадь единичного круга, то есть круга с радиусом, равным R = 1R=1 равна S = \pi R^2 = \piS=πR
2
 =π.

Примечание 2. Уравнение единичной окружности имеет вид x^2+y^2 = 1
"""
import random
n = 10**6       # количество испытаний
# n = 1000
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        k += 1

print((k/n)*s0)
