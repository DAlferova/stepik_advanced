"""
Дополните приведенный код, так чтобы получить список, содержащий только непустые кортежи исходного списка tuples,
не меняя порядка их следования.
non_empty_tuples = [i for i in tuples if i]
non_empty_tuples = list(filter(None, tuples))
"""
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []
for element in tuples:
    if len(element) > 0:
        non_empty_tuples.append(element)
n2 = [el for el in tuples if len(el) > 0]

print(non_empty_tuples)
print(n2)
