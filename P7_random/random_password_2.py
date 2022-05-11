"""
Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из
строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по
одной букве в верхнем и нижнем регистре.
"""
from string import *
import random

good_letters = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
n, m = int(input()), int(input())


def generate_password(length):
    while True:
        psw = ''.join(random.sample(good_letters, length))
        if (len((set(psw) & set(ascii_uppercase))) > 0) and (len((set(psw) & set(ascii_lowercase))) > 0) and \
                (len((set(psw) & set(digits))) > 0):
            return psw


def generate_passwords(count, length):
    result = []
    for _ in range(count):
        result.append(generate_password(length))
    return result


passwords = generate_passwords(n, m)
for password in passwords:
    print(password)
