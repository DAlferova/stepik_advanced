"""
Задача: описание поставленной задачи.
"""


class ClassName:
    """
    Описание класса
    """

    def func1(matrix: list, rows: int, cols: int, width=1):
        """
        Описание функции и параметров, например таких
        :param matrix: матрица
        :param rows: количество строк
        :param cols: количество столбцов
        :param width:  требуемая длина строки
        :return: Перебор элементов матрицы по строкам
        """



        for r in range(rows):
            for c in range(cols):
                print(str(matrix[r][c]).ljust(width), end=' ')
            print()