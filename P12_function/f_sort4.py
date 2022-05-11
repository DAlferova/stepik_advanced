"""
Интересная сортировка-1
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если два числа имеют
одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним
пробелом.
Sample Input 1:

12 14 79 7 4 123 45 90 111
Sample Output 1:

12 111 4 14 123 7 45 90 79
"""
numbers = [num for num in input().split()]


def sum_digits(x: str):
    return sum([int(item) for item in x])


numbers.sort(key=sum_digits)
print(*numbers)
