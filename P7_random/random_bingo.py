"""
Для игры в бинго требуется карточка размером 5 \times 55×5, содержащая различные (уникальные) целые числа
от 1 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 00).

Игра-лото "Cупер Бинго". Играть в лотерею онлайн бесплатно

Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.

Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно 3 символа. Для этого
используйте строковый метод ljust().

Примечание 2. Пример возможного ответа:

1  16 31 46 61
10 30 42 47 68
3  18 0  48 63
9  19 34 49 70
5  20 35 50 65
Возможны и другие способы генерации карточки для игры в бинго.
line = sample(range(1, 76), 25)
"""
import random
bingo = []
uniq_numbers = set()
while len(uniq_numbers) < 25:
    uniq_numbers.add(random.randint(1, 75))
# print(uniq_numbers)

for i in range(5):
    temp = [0 for _ in range(5)]
    bingo.append(temp)

for r in range(5):
    for c in range(5):
        bingo[r][c] = uniq_numbers.pop()
bingo[2][2] = 0

for r in range(5):
    for c in range(5):
        print(str(bingo[r][c]).ljust(3), end='')
    print()
