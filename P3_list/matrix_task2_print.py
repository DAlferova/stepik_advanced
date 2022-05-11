"""
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов
в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала
первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую
строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый
столбец, и так далее.
Sample Input 1:

4
2
и
швец
и
жнец
и
на
дуде
игрец
Sample Output 1:

и швец
и жнец
и на
дуде игрец

и и и дуде
швец жнец на игрец

for row in arr:
    print(*row)
print()
"""
n, m = int(input()), int(input())
my_matrix = []
for i in range(n):
    one_list = []
    for j in range(m):
        one_list.append(input())
    my_matrix.append(one_list)


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def print_matrix_column(matrix, n, m, width=1):
    for c in range(m):
        for r in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


print_matrix(my_matrix, n, m)
print()
print_matrix_column(my_matrix, n, m)
