"""
Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел
1, 2, 3, \ldots, n^21,2,3,…,n
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
  которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы:
nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
проверяем:
1) чтобы не было нулей в квадрате,
2) чтобы был заполнен разными числами от 1 до n в количестве n^2
3) суммы по строкам, столбцам, диагоналям были равны.
3
8 1 6
3 5 7
4 9 2
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


def check0(my_matrix: list, my_n: int) -> bool:
    for i in range(my_n):
        for j in range(my_n):
            if my_matrix[i][j] == 0:
                return False
    return True


def different_numbers(my_matrix: list, my_n: int) -> bool:
    numbers = []
    for i in range(my_n):
        numbers.extend(my_matrix[i])
    for el in range(1, n * n + 1):
        if not (el in numbers):
            return False
    return True


def check_sum(my_matrix: list, my_n: int) -> bool:
    sled = 0
    for i in range(my_n):
        sled += matrix[i][i]
    sub_sled = 0
    for i in range(my_n):
        sub_sled += matrix[i][n-i-1]
    if sled != sub_sled:
        return False
    for i in range(my_n):
        if sum(my_matrix[i]) != sled:
            return False
    return True


if check0(matrix, n) and different_numbers(matrix, n) and check_sum(matrix, n):
    print('YES')
else:
    print('NO')
