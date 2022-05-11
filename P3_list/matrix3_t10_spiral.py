"""
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером
n×m заполнив её "спиралью" в соответствии с образцом.
Sample Input 1:

4 5
Sample Output 1:

1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
"""


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]

res1 = 1

index_0 = 0
index_n = n - 1
index_m = m - 1

while (index_m - index_0) >= 0 and (index_n - index_0) >= 0 and res1 <= n * m:
    # заполняем строку вправо
    for j in range(index_0, index_m + 1):
        if res1 <= n * m:
            matrix[index_0][j] = res1
            res1 += 1

    # заполняем столбец вниз на size
    for i in range(index_0, index_n):
        if res1 <= n * m:
            matrix[i + 1][index_m] = res1
            res1 += 1

    # заполняем строку влево на size
    for j in range(index_0, index_m):
        if res1 <= n * m:
            matrix[index_n][- j - 2] = res1
            res1 += 1

    # заполняем столбец вверх
    for i in range(index_0 + 1, index_n):
        if res1 <= n * m:
            matrix[- i - 1][index_0] = res1
            res1 += 1

    index_0 += 1
    index_n -= 1
    index_m -= 1


print_matrix(matrix, n, m, 3)
