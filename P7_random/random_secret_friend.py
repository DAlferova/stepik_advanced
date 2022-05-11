"""
Тайный друг 🌶️
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число nn – общее количество учеников. Далее идут nn строк, содержащих
 имена и фамилии учеников.

Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного
друга, разделённые дефисом.

Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть тайным другом для н
ескольких учеников.

Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны и другие способы выбора тайных друзей.

Для отладки кода 🟡
Тестовые данные 🟢
Sample Input 1:

3
Светлана Зуева
Аркадий Белых
Борис Боков
Sample Output 1:

Светлана Зуева - Борис Боков
Аркадий Белых - Светлана Зуева
Борис Боков - Аркадий Белых
"""
import random

n = int(input())
students = []
friends = []
for _ in range(n):
    name = input()
    students.append(name)
    friends.append(name)

# for student in students:
#     need_choice = True
#     while need_choice:
#         name = random.choice(friends)
#         if student is not name:
#             print(f"{student} - {name}")
#             friends.remove(name)
#             need_choice = False


def create_secret_friends():
    random.shuffle(friends)
    ok = True
    for i in range(len(students)):
        if students[i] == friends[i]:
            ok = False
    if ok:
        return
    else:
        # print('!')
        create_secret_friends()


create_secret_friends()
for i in range(len(students)):
    print(f"{students[i]} - {friends[i]}")



