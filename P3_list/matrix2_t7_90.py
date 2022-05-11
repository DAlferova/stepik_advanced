"""
Напишите программу, которая поворачивает квадратную матрицу чисел на 90 по часовой стрелке.
Где было i стало n - j - 1, а там где было j - стало i.
matrix[i][j] = matrix[j][n-i-1] - против часовой стрелки
result = [[0] * n for _ in range(n)]

Sample Input 1:

3
1 2 3
4 5 6
7 8 9

Sample Output 1:

7 4 1
8 5 2
9 6 3

"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

matrix_result = []
for i in range(n):
    temp = [element for element in matrix[i]]
    matrix_result.append(temp)

for i in range(n):
    for j in range(n):
        matrix_result[i][j] = matrix[n - j - 1][i]

for row in matrix_result:
    print(*row)
