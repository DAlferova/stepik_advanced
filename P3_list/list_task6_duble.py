"""
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
последовательности одинаковых символов заданной строки в подсписки.
a b c d
"""
symbols = list(input().split())

result = []
element = [symbols[0]]
for i in range(1, len(symbols)):
    if symbols[i] in element:
        element.append(symbols[i])
    else:
        result.append(element)
        element = []
        element.append(symbols[i])
result.append(element)
print(result)
