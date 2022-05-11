"""
На вход программе подается натуральное число n m. Напишите программу, которая создает матрицу размером n×m
заполнив её в соответствии с образцом.
Sample Input 1:

5 5
Sample Output 1:

1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1

matrix = [[(j + i) % m + 1 for j in range(m)] for i in range(n)]
"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = [int(num) for num in input().split()]
row = [j + 1 for j in range(m)]

for i in range(n):
    print(*row)
    element = row.pop(0)
    row.insert(m-1, element)


# print_matrix(res, n, m, 3)