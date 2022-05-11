import random
#
# for _ in range(10):
#     print(random.randint(1, 100)) #  [1;100]
# print(random.randrange(10))       #  [0;10)
# num = random.random()
# print(num)
# print(*[('Орел', 'Решка')[random.randint(0, 1)] for _ in range(n)], sep='\n')
# print(random.choice(['Орел', 'Решка']))

n = int(input())    # количество попыток
for _ in range(n):
    print(['Орел', 'Решка'][random.randint(0, 1)])
