"""
Напишите программу, которая возводит квадратную матрицу в mm-ую степень.
Sample Input 1:

3
1 2 3
4 5 6
7 8 9
2

Sample Output 1:

30 36 42
66 81 96
102 126 150
"""


# def print_matrix(matrix, n, m, width=1):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
# # print_matrix(res, n1, n1, 3)

# n, m = [int(num) for num in input().split()]


n1 = int(input())
matrix = []
for _ in range(n1):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    matrix.append(elem)
st = int(input())


def multi_matrix(matrix_a: list, matrix_b: list, n: int, m: int, k: int) -> list:
    """
    This function perform multiply
    :param matrix_a: matrix with nxm size
    :param matrix_b: matrix with mxk size
    :param n: count of rows of matrix_a
    :param m: count of columns of matrix_a
    :param k: count of columns of matrix_b
    :return: matrix = matrix_a * matrix_b
    """
    matrix_multi = [[0] * k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for r in range(m):
                matrix_multi[i][j] += matrix_a[i][r] * matrix_b[r][j]
    return matrix_multi


def matrix_in_st(matrix1: list, nn: int, stepen: int) -> list:
    matrix_result1 = [[1] * n1 for _ in range(nn)]
    if stepen == 0:
        return matrix_result1
    if stepen == 1:
        return matrix1
    if stepen == 2:
        return multi_matrix(matrix1, matrix1, n1, n1, n1)
    return multi_matrix(matrix_in_st(matrix1, nn, stepen - 1), matrix1, n1, n1, n1)


res = matrix_in_st(matrix, n1, st)


for i in range(n1):
    for j in range(n1):
        print(res[i][j], end=' ')
    print()
