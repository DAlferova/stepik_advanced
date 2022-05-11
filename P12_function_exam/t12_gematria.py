"""
Sample Input 1:

4
basis
after
chief
agenda
Sample Output 1:

agenda
chief
after
basis
"""


def gematria(s: str):
    gem = 0
    for letter in s:
        gem += ord(letter.upper()) - ord('A')
    return gem


n = int(input())
words = []
for _ in range(n):
    words.append(input())

words.sort()
print(*(sorted(words, key=lambda x: gematria(x))), sep='\n')
