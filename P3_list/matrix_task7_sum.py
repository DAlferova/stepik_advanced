"""
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов:
верхней четверти; i < j i < n - 1 - j
правой четверти; i < j i > n - 1 - j
нижней четверти; i > j i > n - 1 - j
левой четверти. i > j i < n - 1 - j
4
1 2 3 4
5 6 7 8
3 4 5 6
1 2 3 4
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

sum_up = 0
sum_right = 0
sum_down = 0
sum_left = 0
for i in range(n):
    for j in range(n):
        if (i < j) and (i < n - 1 - j):
            sum_up += matrix[i][j]
        if (i < j) and (i > n - 1 - j):
            sum_right += matrix[i][j]
        if (i > j) and (i > n - 1 - j):
            sum_down += matrix[i][j]
        if (i > j) and (i < n - 1 - j):
            sum_left += matrix[i][j]
print('Верхняя четверть: ' + str(sum_up))
print('Правая четверть: ' + str(sum_right))
print('Нижняя четверть: ' + str(sum_down))
print('Левая четверть: ' + str(sum_left))


