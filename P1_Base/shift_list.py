"""
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
Sample Input 1:
1 2 3 4 5
Sample Output 1:
5 1 2 3 4
print(*[a[-1]] + a[:-1])
"""
numbers = [int(item) for item in input().split(' ')]
numbers.insert(0, numbers.pop(-1))
print(*numbers)