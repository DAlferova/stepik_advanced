"""
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен
и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число nn – количество холодильников. В последующих nn строках вводятся строки, содержащие
латинские строчные буквы и цифры, в каждой строке от 55 до 100100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить
не нужно.
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n

import re
num = int(input())
for i in range(num):
    if re.search(r'.*a.*n.*t.*o.*n', input()):
        print(i + 1, end=' ')
"""


def anton_detected(s):
    result = str()
    anton = 'anton'
    index1 = 0
    for letter in s:
        if result != anton:
            if letter == anton[index1]:
                result += letter
                index1 += 1
    if result == anton:
        return True
    else:
        return False


n = int(input())
result_index = []
for i in range(n):
    if anton_detected(str(input())):
        result_index.append(i+1)
print(*result_index)
