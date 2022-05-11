"""
Создать Decimal число можно из обычного целого числа (int), из числа с плавающей точкой (float) или из строки (str).
"""
from decimal import *

d1 = Decimal(1)
d2 = Decimal(567)
d3 = Decimal(-93)
d4 = Decimal('12345')
d5 = Decimal('52.198')

print(d1, d2, d3, d4, d5, sep='\n')


# from decimal import Decimal as D
#
# num1 = D('1.5') + D('3.2')
# num2 = D('1.4') * D('2.58')
#
# print(num1)
# print(num2)