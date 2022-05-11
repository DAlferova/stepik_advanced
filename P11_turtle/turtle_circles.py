"""
Напишите программу, которая рисует изображение символа олимпиады в соответствии с образцом.
"""
import turtle
turtle.pensize(5)
turtle.penup()
dic = {'green': (50, -50), 'red': (100, 0), 'black': (0, 0), 'cyan': (-100, 0), 'yellow': (-50, -50)}
for i in dic:
    turtle.pencolor(i)
    turtle.goto(dic[i])
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
