"""
Урок информатики
Даны по 1010-балльной шкале оценки по информатике трех учеников. Напишите программу, которая выводит множество оценок,
которые есть и у первого и у второго учеников, но которых нет у третьего ученика.

Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной
строке).

Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии
 с условием задачи.

Примечание. Оценка ученика находится в диапазоне от 00 до 10 включительно.
Sample Input 1:

1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:

5 3 2

4 2 5 10 6 2
10 4 7 6 3 10
1 2 1 5 9 5

10 6 4
int(i) for i in input().split()
a, b, c = [set(map(int, input().split())) for _ in range(3)]


Напишите программу, которая выводит множество оценок, имеющихся у учеников,
которые встречаются не более, чем у двух из указанных учеников.
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 10 2 10 2 6 7 10 10 6
1 4 6 9 8 7 0 9 0 9 8 10
Напишите программу, которая выводит множество оценок третьего ученика,
которые не встречаются ни у первого, ни у второго ученика. в порядке убывания
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10
Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.
1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 8 8 7 0 6 0 3 8 1
print(*sorted(b -  a, key=int))
"""
a, b, c = (set(int(i) for i in input().split()) for _ in 'abc')
# print(*sorted((a & b) - c, reverse=True))

# print(*sorted(((a | b | c) - (b & c & a))))

# print(*sorted(c - a - b, reverse=True))

print(*sorted(set(range(11)) - c - a - b))
