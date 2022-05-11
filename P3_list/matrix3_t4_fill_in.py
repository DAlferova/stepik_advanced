"""Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.
Sample Input 1:

3 7
Sample Output 1:

1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21

for j in range(m):
    for i in range(n):
        matrix[i][j] = j * n + i + 1

"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = [int(num) for num in input().split()]
matrix_result = [[1] * m for _ in range(n)]

value = 1
for j in range(m):
    for i in range(n):
        matrix_result[i][j] = value
        value += 1

print_matrix(matrix_result, n, m, 3)

