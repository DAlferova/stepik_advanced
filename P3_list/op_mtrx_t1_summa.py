"""
Напишите программу для вычисления суммы двух матриц.
Sample Input 1:

2 4
1 2 3 4
5 6 7 1

3 2 1 2
1 3 1 3
Sample Output 1:

4 4 4 6
6 9 8 4
"""
n, m = [int(num) for num in input().split()]

matrix_a = []
for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    matrix_a.append(elem)
input()
matrix_b = []
for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    matrix_b.append(elem)

matrix_sum = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix_sum[i][j] = matrix_a[i][j] + matrix_b[i][j]

for i in range(n):
    for j in range(m):
        print(matrix_sum[i][j], end=' ')
    print()

