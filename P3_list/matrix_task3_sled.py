"""
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу,
которая выводит след заданной квадратной матрицы.
3
1 2 3
4 5 6
7 8 9
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

sled = 0
for i in range(n):
    sled += matrix[i][i]

print(sled)
