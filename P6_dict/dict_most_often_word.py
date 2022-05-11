"""
Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
должно быть выведено то, что меньше в лексикографическом порядке.
"""
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry ' \
    'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon ' \
    'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple ' \
    'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
    'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate ' \
    'barley'

result = {}
for word in s.split():
    result[word] = result.get(word, 0) + 1

# for key, value in sorted(result.items(), key=lambda x: x[1]):
#     print(value)

# sorted_items = sorted(result.items(), key=lambda x: x[1])
# print(sorted_items[-1][0])
#
# print(sorted_items)
max_count = max(result.values())
often_words = [key for key in result.keys() if result[key] == max_count]
print(often_words[-1])

