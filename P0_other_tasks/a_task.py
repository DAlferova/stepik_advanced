# функиция sum_of_numbers находит пары чисел в списке list, которые в сумме равны n
def sum_of_numbers(list, n):
    # инициализируем значения переменных
    result = []
    i = 0
    # находим размер списка
    len_list = len(list)
    # первый цикл проходится по первому слагаемому из списка list
    while i < (len_list - 1):
        # начальное значение второго слагаемого всегда на 1 больше первого слагаемого
        j = i + 1
        # вложенный цикл проходится по второму слагаемому из списка list
        while j < len_list:
            # проверяем: если сумма слагаемых равна n, то добавляем эти слагаемые в результирующий список result
            if (list[i] + list[j]) == n:
                result.append((list[i], list[j]))
            j += 1
        i += 1
    return result


numbers = [1, 12, 5, 7, 3, 875, 343, 8, 43, 56, 6, 2, 10, 54]
# sum = 15
sum = 14
# вызываем функцию нахождения пар сумма которых равна sum из списка numbers
outlist = sum_of_numbers(numbers, sum)
# сравниваем вывод функции, выводим найденные пары слагаемых или сообщение о невозможности нахождения таких пар
if outlist:
    print('Числа из списка, суммы которых равна', sum, ':', outlist)
else:
    print('Совпадений не найдено')
