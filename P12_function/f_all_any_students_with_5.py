"""
Отличники
Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться,
что в каждом классе есть хотя бы один отличник – ученик с оценкой 55 по контрольной работе. Напишите программу с
 использованием встроенных функций all(), any() для помощи Тимуру в проверке.

Формат входных данных
На вход программе подается натуральное число nn – количество классов. Затем для каждого класса вводится блок
информации вида:
натуральное число kk – количество учеников в классе;
далее вводится kk строк вида: фамилия оценка.
Формат выходных данных
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае.
f"Я написал это,\nчтобы помнить"
"""
n_classes = int(input())
good_student = []

for i in range(n_classes):
    k = int(input())
    students = {}
    for _ in range(k):
        words = input().split()
        students[words[0]] = words[1]
    is_good = any(map(lambda x: students[x] == '5', students.keys()))
    good_student.append(is_good)
# print(all(good_student))
if all(good_student):
    print("YES")
else:
    print("NO")
