"""
На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает
список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной
строке.
Sample Input 1:
a b c d e f
2
Sample Output 1:
[['a', 'b'], ['c', 'd'], ['e', 'f']]

def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))

"""
symbols = list(input().split())
n = int(input())
el = []
counter = 0
result = []
for s in symbols:
    if counter < n:
        el.append(s)
        counter += 1
    else:
        result.append(el)
        el = []
        el.append(s)
        counter = 1

result.append(el)
print(result)
