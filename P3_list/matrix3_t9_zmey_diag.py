"""
На вход программе подается натуральное число n m. Напишите программу, которая создает матрицу размером n×m
заполнив её в соответствии с образцом.
Sample Input 1:

3 5
Sample Output 1:

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = [int(num) for num in input().split()]
res = [[0] * m for _ in range(n)]
value = 1
index_sum = 0
for index_sum in range(n + m + 1):
    for i in range(n):
        for j in range(m):
            if i + j == index_sum:
                res[i][j] = value
                value += 1


print_matrix(res, n, m, 3)
