"""
Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.

Примечание 1. Следующий программный код:

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
должен выводить:

False
True
True
True
True
False
False
True
False
is_num = lambda n: n.replace('.', '', 1).replace('-', '', 1).isdigit() and n.find('-') <= 0
"""

is_num = lambda s: set(s).issubset(set('1234567890.-')) and s.count('.') < 2 and s[1:].count('-') == 0
print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))