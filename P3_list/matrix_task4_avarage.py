"""
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки.
4
1 2 3 4
5 6 3 15
0 2 3 1
5 2 8 5
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    av_row = sum(matrix[i]) / n
    counter = 0
    for j in range(n):
        if matrix[i][j] > av_row:
            counter += 1
    print(counter)
