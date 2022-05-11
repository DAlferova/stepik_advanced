"""
Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Фибоначчи.
Sample Input 1:
7
1 1 2 3 5 8 13
"""


def fibonachi(num: int) -> list:
    f1, f2 = 1, 1
    result = []
    for i in range(n):
        # print(f1)
        result.append(f1)
        f1, f2 = f2, f1 + f2
    return result


n = int(input())
res_fibo = fibonachi(n)
print(*res_fibo)
