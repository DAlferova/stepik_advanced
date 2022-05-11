"""
Длинные строки
Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все
строки наибольшей длины из файла, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.
One
Twenty one
Two
Twenty two
то результатом будет:

Twenty one
Twenty two
"""
with open('lines.txt', encoding='utf-8') as file:
    all_lines = file.readlines()
    max_len = max(map(len, all_lines))
    for line in all_lines:
        if len(line) == max_len:
            print(line.rstrip())
