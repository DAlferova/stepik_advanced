"""
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text
будет подсчитано количество его вхождений.
result = {elem: text.count(elem) for elem in set(text)}
"""
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for s in text:
    result[s] = result.get(s, 0) + 1
print(result)
