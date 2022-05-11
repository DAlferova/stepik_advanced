"""
Используя генератор множеств, дополните приведенный код, так чтобы он выбрал из списка files уникальные имена файлов c
расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением,
все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.
result = {c.lower() for c in files if c.lower().endswith('.png')}
print(*sorted({c.lower() for c in files if '.png' in c.lower()}))
png_files = {i.lower()[:-4] for i in files if i.lower()[-4:] == '.png'}
print(*sorted({i.lower() if i[-3:].lower()=='png' else '' for i in files}))
"""
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']
myset = {word.lower() for word in files if word.lower()[-3:] == 'png'}
print(*sorted(myset))
