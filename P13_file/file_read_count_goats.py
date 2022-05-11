"""
Загадка от Жака Фреско 🌶️
Однажды Жака Фреско спросили:

"Если ты такой умный, почему не богатый?"

Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:

"Были разноцветные козлы. Сколько?"

"Сколько чего?"

"Сколько из них составляет более 7% от общего количества козлов?"

Вам доступен текстовый файл goats2.txt в первой строке которого написано слово COLOURS, далее идет список всех
возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных
цветов. Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию
загадки от Жака Фреско.
"""
# from collections import Counter
# with open('goats.txt') as goats, open('answer.txt', 'w') as answer:
#     set_colours = set()
#     goats.readline()
#     line = goats.readline()
#     while "GOATS" not in line:
#         set_colours.add(line.strip())
#         line = goats.readline()
#     all_goats = [item.strip() for item in goats.readlines()]
#
#     number_of_goats = len(all_goats)
#     count_goats_dict = Counter(all_goats)
#
#     good_colors =[]
#     for colour in set_colours:
#         if count_goats_dict[colour] * 100 > 7 * number_of_goats:
#             good_colors.append(colour)
#     good_colors.sort()
#
#     print(*good_colors, file=answer, sep='\n')


with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
    cont = f1.read().split('\n')
    print(cont)
    colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
    print(colors)
    print(goats)
    print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)


