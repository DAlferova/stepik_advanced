"""
На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что в записи этих
двух строк используются все десять цифр?

Формат входных данных
На вход подаются две строки, состоящие из цифр.

Формат выходных данных
Программа должна вывести YES, если в записи этих двух строк используются все десять цифр, и NO в противном случае.
Sample Input 1:

12387
94230
Sample Output 1:

NO
print(('NO', 'YES')[len(set(input() + input())) == 10])
print('YES' if set([int(i) for i in (input() + input())]) == set(range(10)) else 'NO')
"""
str1, str2 = input(), input()

all_digits = set('0123456789')
print('YES' if set(str1 + str2) == all_digits else 'NO')
print(all_digits)
print(set(str1 + str2))
