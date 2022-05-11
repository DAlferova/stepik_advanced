"""
Необычные страны
Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными
символом табуляции '\t'.

Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения
которых больше чем 500000 человек, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести названия стран, удовлетворяющие условиям задачи, каждое на отдельное строке.
with open('population.txt') as f:
    for line in f:
        n, p = line.split('\t')
        if n.startswith('G') and int(p) > 500000:
            print(n)
"""
with open('population.txt') as f:
    for line in f.readlines():
        city = line.split("\t")
        if city[0][0] == "G" and int(city[1].strip("\n")) > 500000:
            print(city[0])