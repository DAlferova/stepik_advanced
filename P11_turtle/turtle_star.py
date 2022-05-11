"""
нарисуйте звезду.
https://stepik.org/lesson/330014/step/1?unit=313365
"""
import turtle


def cccp(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)


turtle.pensize(5)
turtle.color('red')
cccp(int(input()))
