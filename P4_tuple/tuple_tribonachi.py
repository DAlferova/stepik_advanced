"""
Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.
1,1, 1, 3, 5, 9, 17, 31, 57, 105 …
"""


def tribonachi(num: int) -> list:
    f1, f2, f3 = 1, 1, 1
    result = []
    for i in range(n):
        # print(f1)
        result.append(f1)
        f1, f2, f3 = f2, f3, f1 + f2 + f3
    return result


n = int(input())
res_tribo = tribonachi(n)
print(*res_tribo)
