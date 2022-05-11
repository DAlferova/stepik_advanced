"""
На вход программе подается число nn. Напишите программу, которая создает и выводит построчно список,
состоящий из nn списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')
"""

n = int(input())
my_list = []

for _ in range(n):
    element = [i + 1 for i in range(n)]
    my_list.append(element)
    print(element)

# print(my_list)
