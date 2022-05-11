"""
Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и
строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.
Sample Input 1:

abcABC9
Sample Output 1:

YES
Sample Input 2:

abAB34
Sample Output 2:

NO
"""
password = input()
good_len = (len(password) > 6)
has_digit = any(map(lambda x: x.isdigit(), password))
has_big = any(map(lambda x: x.istitle(), password))
has_small = any(map(lambda x: x.islower(), password))
if good_len and has_digit and has_big and has_small:
    print("YES")
else:
    print("NO")
