"""
Переворот строки
Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку
в обратном порядке.
print(f.read()[::-1])
"""
with open('text.txt', encoding='utf-8') as file:
    text = file.read()
    print(text[::-1])