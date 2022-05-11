"""
info1.update(info2)  info1 |= info2
"""
capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия': 'Бразилиа'}

for key, value in sorted(capitals.items(), key=lambda x: x[1]):
    print(value)

for key in sorted(capitals):
    print(key)

for key, value in capitals.items():
    print(key, '-', value)

info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
info_dict = dict(info_list)  # создаем словарь на основе списка кортежей

info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков
info_dict2 = dict(info_tuple)  # создаем словарь на основе кортежа списков
dict1 = {}
dict2 = dict()
info = dict(name='Timur', age=28, job='Teacher')
dict3 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')

keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']
info2 = dict(zip(keys, values))
print(info2)

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1


info3 = {'name': 'Bob',
         'age': 25,
         'job': 'Dev'}

item1 = info3.get('salary')
item2 = info3.get('salary', 'Информации о зарплате нет')

print(item1)
print(item2)

name2 = info.setdefault('name', 'Max')    # параметр default задан - Добавление
surname = info.pop('surname', None)  # удаление, если такого ключа нет, то переменной присвоится None
item = info.popitem()   # удаляет из словаря последний добавленный элемент, результат - кортеж
