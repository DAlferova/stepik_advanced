"""
Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и
возвращает приветствие в соответствии с образцом.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.

Примечание 2. Следующий программный код:

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
должен выводить:

Hello, Timur!
Hello, Timur and Roman!
Hello, Timur and Roman and Ruslan!
Примечание 3. Функция greet() должна принимать как минимум один обязательный аргумент!

return 'Hello, ' + ' and '.join([name, *args]) + '!'
"""


def greet(name, *args):
    res = f'Hello, {name}'
    for person in args:
        res += f' and {person}'
    return res + '!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))