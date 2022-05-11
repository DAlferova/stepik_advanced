"""
'ножницы' > 'бумага', 'ящерица'
'бумага' > 'камень', 'Спок'
'камень' > 'ножницы', 'ящерица'
'ящерица' > 'Спок', 'бумага'
'Спок' > 'ножницы', 'камень'

Sample Input 1:
ящерица
камень
Sample Output 1:
Руслан
"""
timur, ruslan = str(input()), str(input())
result = {'ножницы': ['бумага', 'ящерица'],
          'бумага': ['камень', 'Спок'],
          'камень': ['ножницы', 'ящерица'],
          'ящерица': ['Спок', 'бумага'],
          'Спок': ['ножницы', 'камень']}
print('Тимур' if ruslan in result[timur] else 'Руслан' if timur in result[ruslan] else 'ничья')
