"""
CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных
из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую
последующую строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов.
Примечание 5. Если бы файл data.csv содержал информацию

name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
то вызов функции read_csv() вернул бы список:

[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]
def read_csv():
    with open('data.csv') as file:
        keys = file.readline().strip().split(',')
        return [dict(zip(keys, line.strip().split(','))) for line in file]
"""


def read_csv():
    with open('data.csv') as f:
        # keys_line = [k.strip() for k in f.readline().split(",")]
        keys_line = f.readline().strip().split(",")
        list_of_dicts = []
        for data_line in f:
            list_of_dicts.append(dict(zip(keys_line, data_line.strip().split(","))))
    return list_of_dicts


print(read_csv())
