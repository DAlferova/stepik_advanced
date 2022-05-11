"""
Общие числа
На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в п
орядке возрастания, которые есть как в первой строке, так и во второй.

Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести множество чисел, встречающихся в обеих строках.


Sample Input 1:

1 2 3
1 2 4 5
Sample Output 1:

1 2


1 2 3 4 5 6 7 8 9 10
10 9 8 7 6 5 4 3 2 1
--
1 2 3 4 5 6 7 8 9 10
print(*sorted(set(input().split()) & set(input().split()), key=int))
print(*sorted(map(int, set(input().split()) & set(input().split()))))
"""
# myset1, myset2 = set(input().split()), set(input().split())
# myset3 = myset1.intersection(myset2)
# sorted_list = sorted(myset3)
# print(*sorted_list)

# print(*sorted(set(input().split())&set(input().split())))

# myset = set(input().split()).intersection(set(input().split()))
# mylist = sorted(int(item) for item in myset)
# print(*mylist)

print(*sorted(int(item) for item in set(input().split()).intersection(set(input().split()))))


