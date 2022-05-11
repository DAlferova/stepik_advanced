"""
Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.
 -> 8
 def square(side):
  for _ in range(4):
    turtle.forward(side)
    turtle.left(90)

for _ in range(8):
  turtle.left(45)
  square(120)
"""
import turtle


def square(side):
    for i in range(18):
        turtle.left(20)
        turtle.color([["#2F4F4F", "#DC143C"][i % 3 == 0], "#4B0082"][i % 3 == 2])
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)


square(100)
turtle.done()