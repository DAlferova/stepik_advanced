"""
Общая стоимость
Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина.
В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:

наименование товара;
количество товара (целое число);
цена (в рублях) товара за 11 шт (целое число).
Напишите программу, выводящую на экран общую стоимость заказа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести общую стоимость заказа.
lines = map(str.split, file)
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
"""
file1 = open('prices.txt', 'r', encoding='utf-8')

result = 0

for line in file1.readlines():
    a = line.rstrip()
    n1, count, cost = a.split()
    result += int(cost) * int(count)
print(result)
file1.close()

f = open('prices.txt', 'r', encoding='utf-8')
print(sum(map(lambda x: int(x[1]) * int(x[2]), [[el for el in line.split()] for line in f.readlines()])))
f.close()
