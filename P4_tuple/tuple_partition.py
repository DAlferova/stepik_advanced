s1 = 'abc-de'.partition('-')
s2 = 'abc-de'.partition('.')
s3 = 'abc-de-fgh'.partition('-')

print(s1)
print(s2)
print(s3)
# выведет:
#
# ('abc', '-', 'de')
# ('abc-de', '', '')
# ('abc', '-', 'de-fgh')