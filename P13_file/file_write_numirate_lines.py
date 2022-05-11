"""
Нумерация строк
Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого
 файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел.
 Нумерация строк должна начинаться с 1.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Используйте встроенную функцию enumerate().
with open('input.txt') as inp, open('output.txt', 'w') as out:
    for i, j in enumerate(inp, start=1):
        print(f'{i}) {j}', end='', file=out)

with open('input.txt') as fin, open('output.txt', 'w') as fout:
    [fout.write(f'{i}) {line}') for i, line in enumerate(fin, 1)]
"""

with open('input.txt', 'r') as file_input:
    all_lines = file_input.readlines()

with open('output.txt', 'w') as file:
    for item in enumerate(all_lines):
        file.write(f"{item[0]+1}) {item[1]}")
