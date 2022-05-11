"""
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется список. Напишите
программу, которая разделяет список на вложенные подсписки так, что nn последовательных элементов принадлежат
разным подспискам.
Sample Input 1:

a b c d e f g h i j k l m n
3
Sample Output 1:

[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""
symbols = list(input().split())
n = int(input())
result_list = []


def chunked(symbols1, n1, shift=0):
    result = []
    el = []
    for i in range(shift, len(symbols1), n1):
        el.append(symbols1[i])
    result.append(el)

    return result


for s in range(n):
    result_list.extend(chunked(symbols, n, s))

print(result_list)
# el = []
# counter = 0
# result = []
# for s in symbols:
#     if counter < n:
#         el.append(s)
#         counter += 1
#     else:
#         result.append(el)
#         el = []
#         el.append(s)
#         counter = 1
