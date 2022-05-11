"""
На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами
 *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала
записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 11 до 88, снизу вверх)).
b6
"""
desk = [['.'] * 8 for _ in range(8)]
point = str(input())

chess_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
chess_i = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}

i = chess_i[point[1]]
j = chess_j[point[0]]

desk[i][j] = 'N'


def put_asterisks(matrix: list, ii: int, jj: int):
    if (ii >= 0) and (ii <= 7) and (jj >= 0) and (jj <= 7):
        matrix[ii][jj] = '*'


put_asterisks(desk, i - 1, j - 2)
put_asterisks(desk, i - 2, j - 1)
put_asterisks(desk, i - 2, j + 1)
put_asterisks(desk, i - 1, j + 2)
put_asterisks(desk, i + 1, j + 2)
put_asterisks(desk, i + 2, j + 1)
put_asterisks(desk, i + 2, j - 1)
put_asterisks(desk, i + 1, j - 2)

for row in desk:
    print(*row)
