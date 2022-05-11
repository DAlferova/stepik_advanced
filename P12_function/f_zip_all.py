"""
Внутри шара
На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (xx), ординат (yy) и
аппликат (zz) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с введенными
координатами внутри либо на поверхности шара с центром в начале координат и радиусом R = 2R =2.

Формат входных данных
На вход программе подаются три строки текста с вещественными числами, разделенными символом пробела – абсциссы,
ординаты и аппликаты точек в трехмерной системе координат.

Формат выходных данных
Программа должна вывести True если все точки с введенными координатами находятся внутри или на границе шара и
False, если вне.

Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.
Примечание 2. Уравнение поверхности шара (сферы) имеет вид x^2+y^2+z^2 = R^2x
Примечание 3. Для решения задачи используйте встроенные функции all() и zip().
Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков.
Sample Input 1:
0.0 1.0 2.0
0.0 0.0 1.1
0.0 1.0 1.5
Sample Output 1:
False
Sample Input 2:
0.0 0.0
1.5 0.0
1.1 1.1
Sample Output 2:
True
"""
abscissas = [float(a) for a in input().split()]
ordinates = [float(b) for b in input().split()]
applicates = [float(c) for c in input().split()]

# result = all(map(lambda x, y, z: x ** 2 + y ** 2 + z ** 2 <= 4, abscissas, ordinates, applicates))
result = all(map(lambda p: p[0] ** 2 + p[1] ** 2 + p[2] ** 2 <= 4, zip(abscissas, ordinates, applicates)))
print(result)