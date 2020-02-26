import os
def Search():
    tree =os.walk('ЭФ')
    for i in tree:
        print(i)
Search()

tree = os.walk('Абитуриенту')
tree
for i in tree:
    print(i)

import os

def passage(file_name, folder):
    for element in os.scandir(folder):
        if element.is_file():
            if element.name == file_name:
                yield folder
        else:
            yield from passage(file_name, element.path)

print(*passage('system.py', os.getcwd()))


import os
from fnmatch import fnmatch

dirpath = input('Путь к каталогу: ')
while not os.path.isdir(dirpath):  # проверка пути
    print('Такого каталога нет')
    dirpath = input('Путь к каталогу: ')

filename = input('Имя файла: ')

path_f = []
for d, dirs, files in os.walk(dirpath):
    for f in files:
        if fnmatch(f, filename):
            path = (os.path.join(d, f))
            path_f.append(path)