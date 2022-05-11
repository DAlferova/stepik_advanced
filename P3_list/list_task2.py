"""
На вход программе подается число nn. Напишите программу, которая создает и выводит построчно вложенный список,
состоящий из nn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
"""

n = int(input())
my_list = []

for index in range(n):
    element = [i + 1 for i in range(index + 1)]
    my_list.append(element)

print(*my_list, sep='\n')
