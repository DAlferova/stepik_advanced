"""
Случайные числа
Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне от 111 до 777
(включительно), каждое с новой строки.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем random.txt и записать в него случайные числа в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Для генерации случайных чисел используйте модуль random.
import random
numbers = [random.randint(111, 777) for _ in range(25)]
numbers_str = map(lambda s: s + '\n', map(str, numbers))
with open('random.txt', 'w') as file:
    file.writelines(numbers_str)

from random import sample as r
print(*r(range(111, 778), 25), file=open('random.txt', 'w'), sep='\n')
"""
import random
numbers = [random.randint(111, 777) for _ in range(25)]
numbers_str = map(lambda s: str(s) + '\n', numbers)
with open('random.txt', 'w') as file:
    file.writelines(numbers_str)
