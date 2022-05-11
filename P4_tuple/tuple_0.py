"""
Кортежи поддерживают:

доступ к элементу по индексу (только для получения значений элементов);
методы, в частности index(), count();
встроенные функции, в частности len(), sum(), min() и max();
срезы;
оператор принадлежности in;
операторы конкатенации (+) и повторения (*).
"""
print((1, 2, 3, 4) + (5, 6, 7, 8))
print((7, 8) * 3)
print((0,) * 10)

numbers = (2, 4, 6, 8, 10)

if 0 not in numbers:
    print('Кортеж numbers не содержит нулей')


names = ('Gvido', 'Roman' , 'Timur')
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в кортеже')


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(numbers[i])

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
languages = ('Python', 'C++', 'Java')

print(*numbers)
print(*languages, sep='\n')

#***********
not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)

sorted_tuple = tuple(sorted(not_sorted_tuple))
print(sorted_tuple)

#----
not_sorted_tuple = ('cc', 'aa', 'dd', 'bb')
tmp = list(not_sorted_tuple)
tmp.sort()

sorted_tuple = tuple(tmp)
print(sorted_tuple)

#***
notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
string1 = ''.join(notes)
string2 = '.'.join(notes)

print(string1)
print(string2)
# ****************
colors = ('red', 'green', 'blue', 'cyan')

(a, b, c, d) = colors

print(a)
print(b)
print(c)
print(d)

# students = [tuple(input().split()) for _ in range(int(input()))]

# fibonachi
n = int(input())
f1, f2 = 1, 1
for i in range(n):
    print(f1)
    f1, f2 = f2, f1 + f2