"""
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n×n
заполнив её в соответствии с образцом.
Sample Input 1:

5
Sample Output 1:

1  1  1  1  1
0  1  1  1  0
0  0  1  0  0
0  1  1  1  0
1  1  1  1  1
"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
res = [[1 if (i <= j and i <= n - j - 1) or (i >= j and i >= n - j - 1) else 0 for j in range(n)] for i in range(n)]
print_matrix(res, n, n, 3)
