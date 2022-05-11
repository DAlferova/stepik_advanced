"""
произведение элементов кортежа numbers
"""
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
res = 1
for num in numbers:
    res = res * num

print(res)


# data = 'Python для продвинутых!'
# tpl = tuple(data)
# print(tpl)