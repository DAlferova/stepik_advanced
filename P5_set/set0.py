# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
#
# print(*numbers, sep='\n')
# sorted_numbers = sorted(numbers)  # list
# sortnumbers = sorted(numbers, reverse=True)
# print(*numbers, sep='\n')
# *********************************************************************************

# numbers = {1, 2, 3, 4, 5}
#
# print('до удаления:', numbers)
# num = numbers.pop()                 # удаляет случайный элемент множества, возвращая его
# print('удалённый элемент:', num)
# print('после удаления:', numbers)

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1 | myset2   # myset3 = myset1 | myset2
myset4 = myset1.intersection(myset2)    # myset4 = myset1 & myset2
myset5 = myset1.difference(myset2)    # myset5 = myset1 - myset2
myset6 = myset1.symmetric_difference(myset2)    # myset6 = myset1 ^ myset2
print(myset3)
print(myset4)
print(myset5)
print(myset6)

myset1.update(myset2)      # изменяем множество myset1  <==> myset1 |= myset2
myset1.intersection_update(myset2)      # изменяем множество myset1 <==> myset1 &= myset2
myset1.difference_update(myset2)      # изменяем множество myset1 <==>  myset1 -= myset2
myset1.symmetric_difference_update(myset2)      # изменяем множество myset1 <==> myset1 ^= myset2

digits = {int(c) for c in input()}
digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}

#
