"""
Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,

и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.
"""


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda x: x in command, ignore))


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))
