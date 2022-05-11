"""
Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж вида
(кличка собаки, имя владельца, фамилия владельца, возраст владельца).

Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут
перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением –
 список кличек собак (сохранив исходный порядок следования).

Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.

Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
for pet in pets:
    result.setdefault(pet[1:], []).append(pet[0]) 
"""
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for row in pets:
    result[(row[1], row[2], row[3])] = result.get((row[1], row[2], row[3]), [])
    result[(row[1], row[2], row[3])].append(row[0])
    # result.setdefault((row[1], row[2], row[3]), [])

for k, v in result.items():
    print(f"{k}  : {v}")

