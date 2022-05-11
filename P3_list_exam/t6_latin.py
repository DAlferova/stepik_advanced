"""
Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый столбец
которой содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная квадратная
матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы:
nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
Sample Input 1:

4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
Sample Output 1:

YES
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


def matrix_is_latin(my_matrix: list, num: int) -> bool:
    for ii in range(num):
        if sorted(my_matrix[ii]) != [*range(1, num + 1)]:
            return False
    return True


matrix90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix90[i][j] = matrix[n - j - 1][i]


if matrix_is_latin(matrix, n) and matrix_is_latin(matrix90, n):
    print('YES')
else:
    print('NO')





