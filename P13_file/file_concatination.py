"""
Конкатенация файлов 🌶️
На вход программе подается натуральное число nn и nn строк с названиями файлов. Напишите программу, которая создает
файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.
"""
# n = 3
# list_files = ["data.txt", "lines.txt", "nums.txt"]

n = int(input())
list_files = [input() for _ in range(n)]
with open('output.txt', 'w') as output:
    for file in list_files:
        with open(file, 'r') as f:
            lines = f.read()
            output.write(lines)
