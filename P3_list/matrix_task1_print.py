"""
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов
в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы
сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.
"""
n, m = int(input()), int(input())
my_matrix = []
for i in range(n):
    one_list = []
    for j in range(m):
        one_list.append(input())
    my_matrix.append(one_list)


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


print_matrix(my_matrix, n, m)



