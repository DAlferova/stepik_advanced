"""
Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.
3
4
0 3 2 4
2 3 5 5
5 1 2 3
"""
n, m = int(input()), int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

maximum = matrix[0][0]
index_i = 0
index_j = 0
for i in range(n):
    for j in range(m):
        if maximum < matrix[i][j]:
            maximum = matrix[i][j]
            index_i = i
            index_j = j

print(str(index_i) + ' ' + str(index_j))
