"""
n человек, пронумерованных числами от 11 до nn, стоят в кругу. Они начинают считаться, каждый kk-й по счету
человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
Напишите программу, определяющую номер человека, который останется в кругу последним.
a = [i for i in range(1,15)]
*****
while len(list) != 1:
    for i in range(0, k-1):
        list.append(list[i])
    del list[0:k]
****
def fun(n, k):
    if n == 1: return 1
    else: return (fun(n-1, k) + k - 1) % n + 1
"""
n, k = int(input()), int(input())
list_survivors = [i for i in range(1, n+1)]

while n > 1:
    counter = 1
    while counter < k:
        list_survivors.append(list_survivors[0])
        list_survivors.pop(0)
        counter += 1
    list_survivors.pop(0)
    n = len(list_survivors)

print(list_survivors[0])
