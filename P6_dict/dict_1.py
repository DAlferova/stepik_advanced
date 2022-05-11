# keys = ['name', 'age', 'job']
# values = ['Timur', 28, 'Teacher']
# info2 = dict(zip(keys, values))
# print(info2)
# del info2
# print(info2)

l1 = [x for x in range(1, 16)]
l2 = [x*x for x in range(1, 16)]
result = dict(zip([x for x in range(1, 16)], [x*x for x in range(1, 16)]))
# result = dict(zip(range(1, 16), [i * i for i in range(1, 16)]))
print(result)

result = {}
for i in range(1, 16):
    result[i] = i * i
    # result.setdefault(i, i ** 2)
    # result[i] = result.get(i, i ** 2)

print(result)

result = {x: x * x for x in range(1, 16)}
print(result)

