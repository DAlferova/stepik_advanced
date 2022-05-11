"""
Напишите функцию sq_sum(), которая принимает произвольное количество числовых аргументов и возвращает сумму
 их квадратов.
должен выводить:

0
4
8.5
14
385
return sum(x ** 2 for x in args)
"""


def sq_sum(*args):
    res = 0
    for a in args:
        res += a * a
    return res


print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

