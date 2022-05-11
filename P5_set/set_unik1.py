"""
Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

Формат входных данных
На вход программе в первой строке подается число nn – общее количество слов. Далее идут nn строк с словами.

Формат выходных данных
Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.
Sample Input 1:

3
Тимур
Beegeek
АнанАс
Sample Output 1:

5
4
3
for _ in range(int(input())):
    print(len(set(input().lower())))
[print(len(set(input().lower()))) for x in range(int(input()))]
words = (input().lower() for _ in range(n))
"""
n = int(input())
words = []
for i in range(n):
    words.append(input())

for word in words:
    print(len(set(word.lower())))
