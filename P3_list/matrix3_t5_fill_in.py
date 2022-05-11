"""
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n×n
заполнив её в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число n — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и
побочной диагоналях, остальные позиции матрицы заполнить нулями.
res = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]

res = [[int(i == j or i == n - j - 1) for j in range(n)] for i in range(n)]
"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix_result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i + j + 1 == n):
            matrix_result[i][j] = 1

print_matrix(matrix_result, n, n, 3)
