n, m = int(input()), int(input())    # считываем значения n и m
my_list = []

for _ in range(n):
    my_list.append([0] * m)

print(my_list)

#############
my_list = [0] * n

for i in range(n):
    my_list[i] = [0] * m

print(my_list)
###############
my_list = [[0] * m for _ in range(n)]

print(my_list)

##########
my_list = [[0] * m ] * n   # <--- wrong!
my_list[0][0] = 17

print(my_list)
###########################
n = 4                                          # количество строк (элементов)
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    my_list.append(elem)

#############################
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')   # используем необязательный параметр end
    print()                             # перенос на новую строку

########################
for row in my_list:
    for elem in row:
        print(elem, end=' ')
    print()

##### иной порядок вывода ##########
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
    print()

####################### sum
my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:      # в один цикл
    total += sum(row)
print(total)

#########  matrix  #############
rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов

matrix = [[2, 3, 1, 0],
          [9, 4, 6, 8],
          [4, 7, 2, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()


def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


# list_b = [x**3 if x < 0 else x**2 for x in list_a if x % 2 == 0]
