"""
Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

thing
night
Sample Output 1:

YES
Sample Input 2:

cat
rat
Sample Output 2:

NO
"""


def create_dict_count_of_symbols(text: str) -> dict:
    result = {}
    for s in text:
        result[s] = result.get(s, 0) + 1
    return result


word1, word2 = input(), input()
count1 = create_dict_count_of_symbols(word1)
count2 = create_dict_count_of_symbols(word2)

print(['NO', 'YES'][count1 == count2])
