"""
Сумма двух-2
Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела
и конца строки. Напишите программу, выводящую на экран сумму этих чисел.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел из указанного файла.
print(sum(map(int, file.read().split())))
"""
file1 = open('nums.txt', 'r', encoding='utf-8')
# result = 0
# for line in file1:
#     if line.strip():
#         result += int(line)
result = sum(map(int, filter(None, [line.strip() for line in file1])))
print(result)

file1.close()
