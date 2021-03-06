"""
Интересная сортировка-2
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
Sample Input 1:

111 14 79 7 4 123 90 45 12 171
Sample Output 1:

12 111 4 14 123 7 45 90 171 79
"""


def sum_digits(x):
    return sum([int(item) for item in str(x)])


numbers = [int(num) for num in input().split()]
numbers.sort()
numbers.sort(key=sum_digits)
print(*numbers)
