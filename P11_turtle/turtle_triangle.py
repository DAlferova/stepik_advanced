"""
Напишите программу, которая рисует правильный треугольник.
"""


def triangle(side):
    import turtle

    for i in range(3):
        turtle.forward(side)
        turtle.left(120)


n = int(input('Введите длину стороны = '))

triangle(n)
