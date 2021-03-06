"""
Покупки в интернет-магазине 🌶️
Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем
интернет-магазина.

Формат входных данных
На вход программе подается число nn — количество строк в базе данных о продажах интернет-магазина. Далее следует n
n строк с записями вида покупатель товар количество, где покупатель — имя покупателя (строка без пробелов),
товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара (натуральное число).

Формат выходных данных
Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого покупателя —
двоеточие, затем список названий всех приобретенных им товаров в лексикографическом порядке, после названия
каждого товара — количество единиц товара. Информация о каждом товаре выводится на отдельной строке.

Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает
суммарное количество товара по данной позиции.

Тестовые данные 🟢
Sample Input 1:

5
Руслан Пирог 1
Тимур Карандаш 5
Руслан Линейка 2
Тимур Тетрадь 12
Руслан Хлеб 3
Sample Output 1:

Руслан:
Линейка 2
Пирог 1
Хлеб 3
Тимур:
Карандаш 5
Тетрадь 12
***
******************
7
Вячеслав Ручка 1
Филипп Ручка 1
Виктория Перо 3
Вячеслав Линейка 4
Виктория Тетрадь 7
Вячеслав Ручка 29
Филипп Циркуль 1
Correct output:
Виктория:
Перо 3
Тетрадь 7
Вячеслав:
Линейка 4
Ручка 30
Филипп:
Ручка 1
Циркуль 1

for _ in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].get(product, 0) + int(count)
"""
# for _ in range(n):
#     purchase = {}
#     # name, *v = input().split()
#     # sales.setdefault(name, []).append(v)
#     name, tovar, count = input().split()
#     purchase[tovar] = purchase.get(tovar, 0) + int(count)
#     # purchase.setdefault(tovar, 0). + count
#     sales.setdefault(name,{}).update(purchase)

n = int(input())
sales = {}
purchase = {}

for _ in range(n):
    name, tovar, count = input().split()
    if name not in sales:
        sales[name] = {tovar: int(count)}
    else:
        if tovar not in sales[name]:
            sales[name].update({tovar: int(count)})
        else:
            sales[name][tovar] += int(count)

for name in sorted(sales):
    print(name + ':')
    purchase = sales[name]
    for p in sorted(purchase):
        print(f'{p} {purchase[p]}')


