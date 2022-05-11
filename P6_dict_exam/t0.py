# d = {('foo', 100), ('bar', 200), ('baz', 300)}
# print(d)
# d1 = dict([('foo', 100), ('bar', 200), ('baz', 300)])
# print(d1)
# d2 = dict(foo=100, bar=200, baz=300)
# print(d2)
# d3 = {}
# d3['foo'] = 100
# d3['bar'] = 200
# d3['baz'] = 300
# print(d3)
# d4 = {'foo': 100, 'bar': 200, 'baz': 300}
# print(d4)

# data = [
#     'a',
#     'b',
#     {
#         'foo': 1,
#         'bar':
#         {
#             'x' : 10,
#             'y' : 20,
#             'z' : 30
#         },
#         'baz': 3
#     },
#     'c',
#     'd'
# ]

# print(data[2]['bar'][30])

# print(data[2]['bar']['baz']['z'])

# print(data[2]['foo'][30])

# print(data[3]['bar']['z'])

# print(data[2]['bar']['z'])

# student = {'name': 'Emma', 'class': 9, 'marks': 75}
# student.popitem() # last remove
# print(student)

student = {'name': 'Emma', 'class': 9, 'marks': 75}
del student['class']
print(student)
#
student = {'name': 'Emma', 'class': 9, 'marks': 75}
student.pop('class')
print(student)


# recipients.update({'Scripps': 131, 'Math': 3456})
# recipients.update([('Scripps', 131), ('Math', 3456)])
