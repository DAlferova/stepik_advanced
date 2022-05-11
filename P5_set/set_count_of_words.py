"""
Напишите программу для определения общего количества различных слов в строке текста.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.

Примечание 1. Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним
или большим числом пробелов.

Примечание 2. Знаками препинания .,;:-?! пренебрегаем.
Sample Input 1:

Milk is white and so is glue, Ghosts are white and they say BOO!
Sample Output 1:

11
Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night.
words = [word.lower().strip('.,;:-?!') for word in input().split()]
"""
text = input().lower().split()
text2 = []
for word in text:
    text2.append(word.strip('.,;:-?! '))
print(text2)
print(set(text2))
print(len(set(text2)))


