"""
Количество совпадающих
На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая определяет количество чисел, которые есть как в первой строке, так и во второй.

Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести количество чисел, содержащихся одновременно как в первой строке, так и во второй.

Sample Input 1:

1 3 2
4 3 2
Sample Output 1:

2
a, b = ({*input().split()} for _ in 'ab')
"""
# myset1, myset2 = set(input().split()), set(input().split())
print(len(set(input().split()) & set(input().split())))
