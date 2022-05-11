"""
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
Sample Input 1:

3
0 3 10
4 9 3
7 4 0
Sample Output 1:

YES
"""
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


def matrix_is_symmetrical(my_matrix: list, num: int) -> bool:
    for i in range(num):
        for j in range(num):
            if i != n - 1 - j:
                if my_matrix[i][j] != my_matrix[n - 1 - j][n - 1 - i]:
                    return False
    return True


if matrix_is_symmetrical(matrix, n):
    print('YES')
else:
    print('NO')
