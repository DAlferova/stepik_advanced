"""
Дано пятизначное или шестизначное натуральное число.
Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
123456
25000
print(string1[0], end='')
print(int(s[:-5] + s[-5:][::-1]))
print(int(num[::-1]) if len(num) == 5 else num[0] + num[-1:0:-1])
"""
# string
string1 = str(input())
string_result = ''

if len(string1) == 6:
    string_result = string1[0]
    string1 = string1[1:]
string_result = string_result + string1[::-1]
print(int(string_result))

# list

number_list = list(input())
result_list = []
if len(number_list) == 6:
    result_list.append(number_list[0])
    number_list.pop(0)
number_list.reverse()
result_list.extend(number_list)
result_string = ''.join(result_list)
print(int(result_string))

