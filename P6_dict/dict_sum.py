"""
Дополните приведенный код так, чтобы он вывел сумму минимального и максимального ключа в словаре my_dict.
"""
# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd',
#            9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa',
#            10.12: [1, 2, 3], 99.0: {9, 0, 1}}
#
# print(min(my_dict) + max(my_dict))

"""
Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, 
складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. 
езультирующий словарь необходимо присвоить переменной result.
"""
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

# for key in dict1:
#     # result[key] = dict1[key] + dict2[key]
#     result.setdefault(key, dict1[key] + dict2[key])

key_set = set(dict1.keys() | dict2.keys())
# print(key_set)
for k in key_set:
    result[k] = dict1.get(k, 0) + dict2.get(k, 0)

# result = {i: dict1.get(i, 0) + dict2.get(i, 0) for i in set(dict1.keys() | dict2.keys())}
print(result)

# result = dict1.copy()
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value


