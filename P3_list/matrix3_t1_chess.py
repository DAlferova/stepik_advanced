"""
На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n×m,
заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка.
Выведите полученную матрицу на экран, разделяя элементы пробелами.
n, m = map(int, input().split())
for i in range(n):
    row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
    print(*row)
"""
n, m = [int(num) for num in input().split()]

desk = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 1:
            desk[i][j] = '*'

for row in desk:
    print(*row)
