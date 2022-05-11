"""
На вход программе подается Decimal число dd. Напишите программу, которая вычисляет значение выражения


print(getcontext())
print(num.sqrt())
print(num.exp())
print(num.ln())
print(num.log10())
"""
from decimal import *
d = Decimal(input())

print(d.exp() + d.ln() + d.log10() + d.sqrt())

