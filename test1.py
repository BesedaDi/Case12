# Case-study #12
# Developers:   Besedina D. (%),
#
# Программа которая позволяет пользоватею получать информацию о файлоовй сиситеме
# Терминальная навигация в файловой системе
print("1. Просмотр каталога") #Direc_brow
print("2. На уровень вверх") #level_up
print("3. На уровень вниз") #Level_down
print("4. Количество файлов и каталогов") #Quantity
print("5. Размер текущего каталога (в байтах)") #size
print("6. Поиск файла") #Search_цикл
print("7. Выход из программы") #Exit
command=input("Выберите пункт меню:")
import os
if command == 1:
    def Direc_brow():
        pass


    pass
if command == 2:
    def level_up():
        pass


    pass


if command == 3:
    def Level_down():
        pass


    pass
if command == 4:
    def Quantity():
        pass


    pass
if command == 5:
    def size():
        pass


    pass
if command == 6:
    def Search():
        name = input()
        tree = os.walk(name)
        print(tree)


    Search()
if command == 7:
    def Exit():
        pass


    pass
else:
    print("ERROR")
