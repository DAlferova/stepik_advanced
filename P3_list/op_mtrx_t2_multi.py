"""
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в первой матрице,
затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов
второй матрицы затем элементы второй матрицы.
Sample Input 1:

2 2
1 2
3 2

2 2
3 2
1 1
Sample Output 1:

5 4
11 8
"""
n, m = [int(num) for num in input().split()]

matrix_a = []
for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    matrix_a.append(elem)
input()

m, k = [int(num) for num in input().split()]
matrix_b = []
for _ in range(m):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    matrix_b.append(elem)

matrix_multi = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for r in range(m):
            matrix_multi[i][j] += matrix_a[i][r] * matrix_b[r][j]

for i in range(n):
    for j in range(k):
        print(matrix_multi[i][j], end=' ')
    print()
