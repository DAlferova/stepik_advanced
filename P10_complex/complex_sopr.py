"""
Сопряженные числа
Дано натуральное число nn и два комплексных числа z1, z2. Напишите программу, которая вычисляет и выводит
значение выражения
z_1^n + z_2^n + sopr{z_1}^n + sopr{z_2}^{n+1}.
Формат входных данных
На вход программе подается натуральное число n и два комплексных числа z1, z2.

Sample Input 1:
1
2+3j
1+4j
Sample Output 1:
(-10-4j)
"""
import cmath
n = int(input())
z1, z2 = complex(input()), complex(input())

print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))
