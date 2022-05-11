# def my_func(x, y):
#     print(x + y)
#
# my_func(10, y=20)
# my_func(x=10, y=20)
# my_func(10, 20)

def fancy(length, char1, char2):
    return (char1 + char2) * length + char1


print(fancy(5, '-', '*'))


def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(3))

def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(3, '.'))

def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(2, ':', '|'))

def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(4, char2='#'))

def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(char2='$', length=3))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
#
# print(fancy(char2='!'))

def func(*args):
    return max(args) + min(args)


print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))

print('*'*20)
# s1 = 'python'
# s2 = 'stepicon'
# s3 = 'beegeek'
#
# print(min(s1, s2, s3))
# print(max(s1, s2, s3))

s1 = 'python'
s2 = 'stepicon'
s3 = 'beegeek'

print(min(s1, s2, s3, key=len))
print(max(s1, s2, s3, key=len))

def f(x):
    return x**2


def g(x):
    return x**3


funcs = [f, g]
print(funcs[0](5), funcs[1](5))


def comparator(pair):
    return pair[0] + pair[1]


pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
pairs.sort(key=comparator, reverse=True)
print(pairs)

listA = [2, 3, 4]
listB = [3, 2, 1]

result = sum(map(pow, listA, listB))
print(result)


from operator import mul
from functools import reduce

result = reduce(mul, range(1, 6))
print(result)


from operator import add
from functools import reduce

result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)

print('*' * 20)
"""
True
True
False
False
True
"""
func1 = lambda x: (x % 19 == 0) or (x % 13 == 0)
print(func1(19))
print(func1(13))
print(func1(20))
print(func1(15))
print(func1(247))

print('*' * 20)
"""
False
False
True
False
False
True
"""
func = lambda s: s.lower()[0] == 'a' and s.lower()[-1] == 'a'
print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))


