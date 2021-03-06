"""
Напишите программу для определения, является ли число произведением двух чисел из данного набора,
выводящую результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число (0 < n < 1000) – количество чисел в наборе. В последующих n строках
вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число,
которое является или не является произведением двух каких-то чисел из набора.

"""
n = int(input())
list_numbers =[]
for i in range(0, n):
    list_numbers.append(int(input()))
number = int(input())
multi = False

for i in range(0, n):
    for j in range(0, n):
        if (i != j) and list_numbers[i] * list_numbers[j] == number:
            multi = True

if multi:
    print("ДА")
else:
    print("НЕТ")
