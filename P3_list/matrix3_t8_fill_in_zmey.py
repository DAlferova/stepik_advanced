"""
На вход программе подается натуральное число n m. Напишите программу, которая создает матрицу размером n×m
заполнив её в соответствии с образцом.
Sample Input 1:

3 5
Sample Output 1:

1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = [int(num) for num in input().split()]
res = [[0] * m for _ in range(n)]
value = 1
for i in range(n):
    for j in range(m):
        res[i][j] = value
        value += 1

for i in range(n):
    if i % 2 == 1:
        res[i].reverse()

print_matrix(res, n, m, 3)
