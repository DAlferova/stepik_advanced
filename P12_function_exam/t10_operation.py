"""
Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций
 (+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции.

Примечание 1. Приведенный ниже код, при условии, что функция arithmetic_operation() написана правильно

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
должен выводить:

30
4.0
"""
import operator


def arithmetic_operation(op):
    d = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    return lambda x, y: d[op](x, y)


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
