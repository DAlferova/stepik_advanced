"""
Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв
латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
то результатом было бы:

Input file contains:
108 letters
20 words
4 lines
Примечание 2. Словом называется последовательность из непробельных символов.

with open('lines.txt') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')
    print(len(txt.split()), 'words')
    print(txt.count('\n') + 1, 'lines')
"""

with open('file.txt', encoding='utf-8') as file:
    my_list = [line.split() for line in file.readlines()]
    lines_count = len(my_list)
    words_count = 0
    letters_count = 0
    for line in my_list:
        words_count += len(line)
        for word in line:
            for letter in word:
                if letter.isalpha():
                    letters_count += 1
    print("Input file contains:")
    print(f"{letters_count} letters")
    print(f"{words_count} words")
    print(f"{lines_count} lines")
