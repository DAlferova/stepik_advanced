"""
Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке,
отсортированные по убыванию (в обратном лексикографическом порядке).
"""
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
sort_fruit = sorted(fruits, reverse=True)
print(*sort_fruit, sep='\n')
