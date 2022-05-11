"""
На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу
подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть,
стоят вслед за меньшим числом.
1 2 3 4 5
1 1 3 2 2 1 1 1 1

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        counter += 1
*****
nums = tuple(map(int, input().split()))
print(sum(1 for i in range(1, len(nums)) if nums[i-1] < nums[i]))
"""
numbers = [int(item) for item in input().split(' ')]
special_element = numbers[0]
counter = 0
for item in numbers:
    if item > special_element:
        counter += 1
    special_element = item

print(counter)
