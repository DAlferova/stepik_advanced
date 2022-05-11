"""
Строка запроса
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения.
Она начинается после вопросительного знака и идет до конца адреса. Например:

https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:

https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса,
сформированную из этих параметров.

Примечание 1. В итоговой строке параметры должны быть отсортированы в лексикографическом порядке ключей словаря.

Примечание 2. Следующий программный код:

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
должен выводить:

age=28&name=timur
game=2&sport=hockey&time=17
Примечание 3. Вызывать функцию build_query_string() не нужно, требуется только реализовать.
def build_query_string(params):
    res = [f'{k}={v}' for k, v in params.items()]
    return '&'.join(sorted(res))
"""


def build_query_string(d: dict) -> str:
    query_string = ''
    for key in sorted(d.keys()):
        query_string += str(key) + '=' + str(d[key]) + '&'
    return query_string[:-1]


print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
