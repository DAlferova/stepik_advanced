"""
Секретное слово
Напишите программу для расшифровки секретного слова методом частотного анализа.

Формат входных данных
В первой строке задано зашифрованное слово. Во второй строке задано одно целое число nn – количество букв в словаре. В следующих nn строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

Формат выходных данных
Программа должна вывести дешифрованное слово.

Примечание. Гарантируется, что частоты букв не повторяются.

Тестовые данные 🟢
Sample Input 1:

*!*!*?
3
а: 3
н: 2
с: 1
Sample Output 1:

ананас
"""


def create_dict_count_of_symbols(text: str) -> dict:
    result = {}
    for s in text:
        result[s] = result.get(s, 0) + 1
    return result


secret_word = input()
n = int(input())
encryption = {}
for _ in range(n):
    symbol, num = input().split(': ')
    encryption.setdefault(int(num), symbol)

word_dict = create_dict_count_of_symbols(secret_word)
for s in secret_word:
    print(encryption[word_dict[s]], end='')
