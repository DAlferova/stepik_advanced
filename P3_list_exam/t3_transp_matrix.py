"""
Напишите программу, которая транспонирует квадратную матрицу.
Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести транспонированную матрицу.

Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

Примечание 2. Задачу можно решить без использования вспомогательного списка.
Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

1 4 7
2 5 8
3 6 9
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


def print_matrix_column(matrix1, n, m, width=1):
    for c in range(m):
        for r in range(n):
            print(str(matrix1[r][c]).ljust(width), end=' ')
        print()


print_matrix_column(matrix, n, n)

