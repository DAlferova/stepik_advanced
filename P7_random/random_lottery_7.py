"""
Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит
их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:
номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 7 цифр;
все 100 лотерейных билетов должны быть различными.
"""
import random


# def generate_lottery():
#     lottery = set()
#     while len(lottery) < 7:
#         lottery.add(random.randint(1, 49))
#     return sorted(lottery)

#
# all_lottery = []
# while len(all_lottery) < 100:
#     elenemt = generate_lottery()
#     if elenemt not in all_lottery:
#         all_lottery.append(generate_lottery())

# print(*sorted(all_lottery))
all_lottery = set()
while len(all_lottery) < 100:
    all_lottery.add(random.randint(1000000, 9999999))

for billet in all_lottery:
    print(billet)


