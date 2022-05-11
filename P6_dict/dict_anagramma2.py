"""
Анаграммы 2
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

Формат входных данных
На вход программе подаются два предложения, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.

Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-.
Других символов в тексте нет.

Тестовые данные 🟢
Sample Input 1:
Вижу зверей,
Живу резвей
Sample Output 1:
YES
Sample Input 2:
Когда увидимся
тогда и свидимся
Sample Output 2:
NO
**********
def s(word):
    res = {}
    for i in word.lower():
        if i.isalpha():
            res[i] = res.get(i, 0) + 1
    return res
"""


def create_dict_count_of_symbols(text: str) -> dict:
    result = {}
    for s in text:
        result[s] = result.get(s, 0) + 1
    return result


def remove_symbols_from_string(text: str, symbols: str) -> str:
    for symbol in symbols:
        text = text.replace(symbol, '')
    return text


message1, message2 = input().lower(), input().lower()

word1 = remove_symbols_from_string(message1, '.,!?:;- ')
word2 = remove_symbols_from_string(message2, '.,!?:;- ')

count1 = create_dict_count_of_symbols(word1)
count2 = create_dict_count_of_symbols(word2)

print(['NO', 'YES'][count1 == count2])
