"""
Напишите программу, которая по введенным значениям a, b, ca,b,c определяет и выводит вершину параболы.
Sample Input 1:

-2
6
1
Sample Output 1:

(1.5, 5.5)
"""
a, b, c = int(input()), int(input()), int(input())
xy = (- b / (2 * a), (4 * a * c - b * b) / (4 * a) )
print(xy)
