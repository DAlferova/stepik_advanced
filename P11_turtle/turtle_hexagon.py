"""
Напишите программу, которая рисует правильный шестиугольник.
def hexagon(side):
  for _ in '1' * 6:
    turtle.forward(side)
    turtle.right(60)

def count(size, num):
  for _ in range(num):
    hexagon(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.left(60)

count(60, 6)
"""
import turtle


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


hexagon(100)
