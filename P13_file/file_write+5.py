"""
Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка
(фамилия и оценка разделены пробелом). Оценка - целое число от 00 до 100100 включительно.

Напишите программу для добавления 55 баллов к каждому результату теста и вывода фамилий и новых результатов тестов
в файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.
"""
with open('class_scores.txt') as old_scores, open('new_scores.txt', 'w') as new_scores:
    all_lines = [line.strip().split() for line in old_scores.readlines()]
    for name, score in all_lines:
        print(f'{name} {min(100, int(score) + 5)}', end='\n', file=new_scores)
