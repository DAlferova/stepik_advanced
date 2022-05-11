"""
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
"""
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    one_row = []
    for j in range(m):
        one_row.append(i * j)
    matrix.append(one_row)


def print_matrix(my_matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(my_matrix[r][c]).ljust(width), end=' ')
        print()


print_matrix(matrix, n, m, 3)
