"""
Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как
одинаковые.

Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания
.,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
Sample Input 2:
home sweet home sweet.
Sample Output 2:
home
d = {}
for w in input().split():
    w = w.strip('.,!?:;-').lower()
    d[w] = d.get(w, 0) + 1
print(min(d.items(), key=lambda x: (x[1], x[0]))[0])


for c in '.,!?:;-':
    s = s.replace(c, ' ')


s = [word.strip('.,!?:;-') for word in input().lower().split()]
d = {word: s.count(word) for word in s}
print(min([key for key, value in d.items() if value == min(d.values())]))
"""
s = input().lower().strip('.,!?:;-').split()
count_words = {}
for word in s:
    count_words[word.strip('.,!?:;-')] = count_words.get(word.strip('.,!?:;-'), 0) + 1

min_count = min(count_words.values())
rare_words = sorted(key for key in count_words.keys() if count_words[key] == min_count)
print(rare_words[0])
