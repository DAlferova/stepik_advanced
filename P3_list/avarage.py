"""
for li in list1:
    total += sum(li)
    counter += len(li)
    
total = sum([sum(i) for i in list1])
counter = sum([len(i) for i in list1])
"""


list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for li in list1:
    for lj in li:
        total += lj
        counter += 1
print(total/counter)
