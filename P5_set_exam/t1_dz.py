"""
Домашнее задание
Учитель проверяет домашнее задание в классе и получил следующие ответы: из nn школьников у mm домашнее задание съела
собака, у kk отключили свет, а pp учеников постигли оба несчастья. Напишите программу, которая определяет сколько человек выполнило домашнее задание.

Формат входных данных
На вход программе подаются числа n, m, k, p, каждое на отдельной строке.
Sample Input:

35
20
10
3
Sample Output:

8
"""
n, m, k, p = (int(input()) for _ in range(4))
print(n - m - k + p)
