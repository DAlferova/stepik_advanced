"""
Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет
строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.

Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь

result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
Примечание 2. Для получения ASCII кода символа используйте функцию ord().
result = {el: list(map(ord, el)) for el in words}
"""
words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {word: [ord(sym) for sym in word] for word in words}

print(result)

