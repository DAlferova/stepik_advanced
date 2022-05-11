"""
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква
"Р" – соответствует выпадению Решки.
Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
ОРРОРОРООРРРО
ООООООРРРОРОРРРРРРР
s = input().split('О')
print(len(max(s)))

"""
text = str(input())
text += 'S'
counters = []
first_index = text.find("Р")

if first_index < 0:
    print('0')
else:
    counter = 1
    for letter in text[first_index+1:]:
        if letter == 'Р':
            counter += 1
        else:
            counters.append(counter)
            counter = 0
    print(max(counters))
# print(*counters)
