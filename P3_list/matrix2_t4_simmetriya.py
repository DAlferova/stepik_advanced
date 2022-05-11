"""
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
3
0 1 2
1 2 3
2 3 4
3
0 1 2
3 4 5
6 7 8
"""

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


def matrix_is_symmetrical(my_matrix: list, num: int) -> bool:
    for i in range(num):
        for j in range(num):
            if i != j:
                if my_matrix[i][j] != my_matrix[j][i]:
                    return False
    return True


if matrix_is_symmetrical(matrix, n):
    print('YES')
else:
    print('NO')
