"""
Напишите программу, которая рисует снежинку из 1010 ромбов.
turtle.color((random.randrange(256), random.randrange(256), random.randrange(256))
"""
import turtle as t
import random


def romb(side):
    t.forward(side)
    t.left(60)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(60)
    t.forward(side)


for _ in range(10):
    # t.color((random.randrange(256), random.randrange(256), random.randrange(256)))
    romb(100)
    t.left(155)
