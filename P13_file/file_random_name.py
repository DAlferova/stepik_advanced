"""
Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их,
каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.
Abdul Albertson
Abel Adamson
Albert Einstein
"""
import random

with open('first_names.txt') as first, open('last_names.txt') as last:
    first_names = [name.strip() for name in first.readlines()]
    last_names = [name.strip() for name in last.readlines()]
for _ in range(3):
    print(f"{random.choice(first_names)} {random.choice(last_names)}")


