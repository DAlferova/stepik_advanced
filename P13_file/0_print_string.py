# import string
#
# f = string.digits
# print(f)

current_week = "asb 12 fff"

# for s in current_week:
#     print(s.isdigit())
current_number = ""
for item in filter(lambda x: x.isdigit(), current_week):
    current_number += item
print(current_number)