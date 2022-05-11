"""
Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.
'1.45'
from decimal import *

num = Decimal('-1.4568769017')
num_tuple = num.as_tuple()

print(num_tuple.sign)
print(num_tuple.digits)
print(num_tuple.exponent)

print(max(cyphers) + min(cyphers) * (abs(num) >= 1))
"""
from decimal import *
# num = Decimal(input())
num = Decimal('0.1244354689')

# print(max(num.as_tuple().digits) + min(num.as_tuple().digits))
max_num = max(num.as_tuple().digits)

if abs(num.as_tuple().exponent) == len(num.as_tuple().digits):
    min_num = 0
else:
    min_num = min(num.as_tuple().digits)

print(max_num + min_num)
