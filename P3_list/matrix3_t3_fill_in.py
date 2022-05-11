"""
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m
и заполняет её числами от 1 до n*⋅m в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust().
for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1

4 5
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = [int(num) for num in input().split()]
matrix_result = [[1] * m for _ in range(n)]

value = 1
for i in range(n):
    for j in range(m):
        matrix_result[i][j] = value
        value += 1

print_matrix(matrix_result, n, m, 3)


# for row in matrix_result:
#     print(*row)
