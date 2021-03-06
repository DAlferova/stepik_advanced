"""
Напишите программу, которая считывает год и отображает название связанного с ним животного.
2000	Дракон
2001	Змея
2002	Лошадь
2003	Овца
2004	Обезьяна
2005	Петух
2006	Собака
2007	Свинья
2008	Крыса
2009	Бык
2010	Тигр
2011	Заяц
"""
year = int(input())

dict_zodiak = {(2000 % 12): 'Дракон',
               (2001 % 12): 'Змея',
               (2002 % 12): 'Лошадь',
               (2003 % 12): 'Овца',
               (2004 % 12): 'Обезьяна',
               (2005 % 12): 'Петух',
               (2006 % 12): 'Собака',
               (2007 % 12): 'Свинья',
               (2008 % 12): 'Крыса',
               (2009 % 12): 'Бык',
               (2010 % 12): 'Тигр',
               (2011 % 12): 'Заяц'}
print(dict_zodiak[year % 12])
