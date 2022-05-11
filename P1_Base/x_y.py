"""
Дан набор точек на координатной плоскости.
Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки
(сначала абсцисса – xx, затем ордината – yy), разделенных символом пробела.
Sample Output 2:
Первая четверть: 2
Вторая четверть: 2
Третья четверть: 1
Четвертая четверть: 2
"""
n = int(input())
points = []
for i in range(0, n):
    points.append(tuple(int(item) for item in input().split(' ')))

counter = [0, 0, 0, 0]
for point in points:
    print(point)
    x, y = point[0], point[1]
    if x > 0:
        if y > 0:
            counter[0] += 1
        elif y < 0:
            counter[3] += 1
    elif x < 0:
        if y > 0:
            counter[1] += 1
        elif y < 0:
            counter[2] += 1

print('Первая четверть: ' + str(counter[0]))
print('Вторая четверть: ' + str(counter[1]))
print('Третья четверть: ' + str(counter[2]))
print('Четвертая четверть: ' + str(counter[3]))
