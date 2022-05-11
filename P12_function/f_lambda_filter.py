"""
Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words,
имеющие длину ровно 6 символов. Слова следует вывести в алфавитном порядке на одной строке, разделив символом пробела.

Примечание. Используйте анонимную функцию в качестве критерия фильтрации.
print(' '.join(sorted(list(filter(lambda x: len(x)==6, words)))))
"""
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
         'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

result_words = sorted(filter(lambda x: len(x) == 6, words))
print(*result_words)


"""
Напишите программу, которая с помощью встроенных функций map() и filter() удаляет из списка numbers все нечетные 
элементы, большие 47, а все четные элементы нацело делит на два (целочисленное деление – //). 
Полученные числа следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.
print(*map(lambda x: [x // 2, x][x % 2], filter(lambda x: x < 48 or not x % 2, numbers)))
"""
numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
           93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27,
           57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29,
           88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

result_numbers = list(map(lambda y: y // 2 if y % 2 == 0 else y,
                          filter(lambda x: not((x % 2 != 0) and (x > 47)), numbers)
                          )
                      )
print(*result_numbers)
