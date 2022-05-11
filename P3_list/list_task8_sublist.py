"""
На вход программе подается строка текста, содержащая символы. Из данной строки формируется список.
Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
"""


def chunked(symbols_list, n):
    sublist = []
    for shift in range(n):
        for i in range(shift, len(symbols_list), n):
            sub_el = symbols_list[i:i + n]
            if len(sub_el) == n:
                sublist.append(sub_el)
            # sublist.append(symbols_list[i:i + n])
    return sublist


symbols = list(input().split())
result = [[]]
for s in symbols:
    result.append([s])
# for j in range(2, len(symbols)+1):
#     # print(chunked(symbols, j))
#     result.extend(chunked(symbols, j))
#
# print(result)


def chunked2(symbols_list, n):
    sublist = []
    for j in range(len(symbols)):
        sub_el = symbols_list[j:j + n]
        if len(sub_el) == n:
            sublist.append(sub_el)
    return sublist


for j in range(2, len(symbols)+1):
    result.extend(chunked2(symbols, j))

print(result)
