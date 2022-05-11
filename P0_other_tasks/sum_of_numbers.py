def sum_of_numbers(numlist: list, n: int) -> list:
    """
    функция sum_of_numbers находит пары чисел в списке numlist, которые в сумме равны n
    :param numlist: в параметр передаем список в котором необходимо найти пары чисел
    :param n: в этот параметр передаем значение которому должна быть равна сумма пары чисел из списка numlist
    :return: вывод индексов чисел из списка numlist сумма значений которых равна n

    """
    if not isinstance(n, int):
        raise TypeError("аргумент суммы n должен иметь тип данных int")
    result = []
    len_list = len(numlist)

    for i in range(0, len_list - 1):
        for j in range(i + 1, len_list):
            if (numlist[i] + numlist[j]) == n:
                result.append((i, j))
    return result
