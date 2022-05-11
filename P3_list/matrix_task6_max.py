"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
i >= j and i <= n - 1 - j
i <= j and i >= n - 1 - j
3
1 4 5
6 7 8
1 1 6
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

maximum = matrix[0][0]
for i in range(n):
    for j in range(n):
        if (((i >= j) and (i <= n - 1 - j)) or ((i <= j) and (i >= n - 1 - j))) and (maximum < matrix[i][j]):
            maximum = matrix[i][j]

print(maximum)
