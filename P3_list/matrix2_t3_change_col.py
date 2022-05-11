"""
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа nn и mm — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел, затем числа ii и jj — номера столбцов, подлежащих обмену.
3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)
"""
n, m = int(input()), int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
cols = [int(c) for c in input().split()]

matrix_result = [[0] * m for _ in range(n)]


def print_matrix(my_matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(my_matrix[r][c]).ljust(width), end=' ')
        print()


for i in range(n):
    for j in range(m):
        if j == cols[0]:
            matrix_result[i][j] += matrix[i][cols[1]]
        elif j == cols[1]:
            matrix_result[i][j] += matrix[i][cols[0]]
        else:
            matrix_result[i][j] += matrix[i][j]

print_matrix(matrix_result, n, m)
