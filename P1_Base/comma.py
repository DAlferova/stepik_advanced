"""
На вход программе подаётся натуральное число. Напишите программу, которая
вставляет в заданное число запятые в соответствии со стандартным
американским соглашением о запятых в больших числах.
Sample Input 3:
12345
Sample Output 3:
12,345

num = int(input())
print(f'{num:,}')

print('{:,}'.format(int(input())))
"""
number = str(input())
if len(number) <= 3:
    print(number)
else:
    while len(number) % 3 != 0:
        number = "0" + number
    list_numbers = []
    for i in range(1, len(number)//3 + 1):
        list_numbers.append(number[(3 * i - 3):(3 * i)])
    result = str(int(list_numbers[0]))
    for i in range(1, len(list_numbers)):
        result = result + "," + list_numbers[i]
    print(result)
