import os
# testpath = input('Введите адрес: ')
def summ(testpath):

    if os.path.exists(testpath):
        if os.path.isfile(testpath):
            print('ФАЙЛ')
        elif os.path.isdir(testpath):
            print('КАТАЛОГ')
            spisok = os.listdir(testpath)
            summ=len(spisok)

            print('Список объектов в нем: ', spisok, 'Кол-во объектов в нем:', summ)
# print(summ(testpath))

testpath = input('Введите адрес: ')

if os.path.exists(testpath):
    if os.path.isfile(testpath):
        print('ФАЙЛ')
    elif os.path.isdir(testpath):
        print('КАТАЛОГ')
        print('Список объектов в нем: ', os.listdir(testpath))
else:
    print('Объект не найден')