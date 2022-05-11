"""
Предпоследняя строка
На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его предпоследнюю строку.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести предпоследнюю строку указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Гарантируется, что файл содержит хотя бы две строки.
customers.txt
file1.readlines()[-2]
"""
file_name = input()
file1 = open(file_name, 'r', encoding='utf-8')
all_lines = file1.readlines()
print(all_lines[-2])

file1.close()