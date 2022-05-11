"""
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква
английского алфавита, Number – число от 00 до 9999 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный
корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный
from string import ascii_uppercase as letter

a, b, c, d = (choice(ascii_uppercase) for i in range(4))
"""
import string
from random import choice as ch

dg = string.digits
st = string.ascii_uppercase


def generate_index():
    return f'{ch(st)}{ch(st)}{ch(dg)}{ch(dg)}_{ch(dg)}{ch(dg)}{ch(st)}{ch(st)}'


print(generate_index())
