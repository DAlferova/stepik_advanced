"""
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы
относительно горизонтальной оси симметрии.
Sample Input 1:

4
1 2 3 4
5 6 7 8
8 6 4 2
3 4 5 6
Sample Output 1:

3 4 5 6
8 6 4 2
5 6 7 8
1 2 3 4
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


for i in range(n//2):
    for j in range(n):
        matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

for row in matrix:
    print(*row)
