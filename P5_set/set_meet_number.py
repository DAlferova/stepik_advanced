"""
На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES
(в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

Формат входных данных
На вход программе подается строка текста, содержащая числа, разделенные символом пробела.
Примечание. Ведущие нули в числах должны игнорироваться.

Sample Input 1:

1 1 2 2 5 5 5 5 6 7 8
Sample Output 1:

NO
YES
NO
YES
NO
YES
YES
YES
NO
NO
NO
s = set()
for item in input().split():
  print(["NO", "YES"][item in s])
  s.add(item)
"""
numbers = [int(num) for num in input().split()]
set_num = set()
for num in numbers:
    if num in set_num:
        print('YES')
    else:
        print('NO')
        set_num.add(num)

