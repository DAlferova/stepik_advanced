"""
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной
и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце
нужно поменять местами элемент на главной диагонали и на побочной диагонали).
3
1 2 3
4 5 6
7 8 9
Sample Output 1:

7 2 9
4 5 6
1 8 3
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


for i in range(n):
    matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i]

for row in matrix:
    print(*row)
