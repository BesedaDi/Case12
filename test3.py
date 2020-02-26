# Case-study #12
# Developers:   Besedina D. (%),
#               Setskov M.  (%)
print("1. Просмотр каталога") #Direc_brow
print("2. На уровень вверх") #level_up
print("3. На уровень вниз") #Level_down
print("4. Количество файлов и каталогов") #Quantity
print("5. Размер текущего каталога (в байтах)") #size
print("6. Поиск файла") #Search
print("7. Выход из программы") #Exit
command=input("Выберите пункт меню:")
if command==1 or command==2 or command==3 or command==4 or command==5 or command==6 or command==7:
    print("ERROR")
import os
if command==1:
    def Direc_brow():
        pass
    pass
elif command==2:
    def level_up():
        pass
    pass
elif command==3:
    def Level_down():
        pass
    pass
elif command==4:
    def Quantity():
        pass
    pass
elif command==5:
    def size():
        pass
    pass
elif command==6:
    def Search():
        name=input()
        tree = os.walk(name)
    Search()
elif command==7:
    def Exit():
        pass
    pass
