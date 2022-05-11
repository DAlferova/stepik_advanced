"""
Даны три списка student_ids, student_names, student_grades, содержащие информацию о студентах.

Дополните приведенный код, используя генератор, так чтобы получить список result, содержащий вложенные словари
в соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].

Примечание 1. Для параллельной итерации по всем трем спискам одновременно можно использовать встроенную функцию zip().
"""
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# inner_dict = dict(zip(student_names, student_grades))
# print(inner_dict)
# result = [ids: {info: inner_dict[info]} for ids in student_ids for info in inner_dict]

# info = tuple(zip(student_ids, student_names, student_grades))
# print(info)
# result = {x: {y: z} for x, y, z in info}
# big_dict = {x: {y: z} for x, y, z in tuple(zip(student_ids, student_names, student_grades))}
result = [{x: {y: z}} for x, y, z in tuple(zip(student_ids, student_names, student_grades))]

print(result)
