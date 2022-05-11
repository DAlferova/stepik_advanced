"""
Обратный порядок
Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки
данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.
 print(*file.readlines()[::-1], sep='')
"""

with open('data.txt', encoding='utf-8') as file:
    all_lines = file.readlines()
    for line in all_lines[::-1]:
        print(line.rstrip())

with open('data.txt', encoding='utf-8') as file:
    for line in file.readlines()[::-1]:
        print(line.rstrip())
