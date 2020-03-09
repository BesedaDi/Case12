# Case-study #12
# Developers:   Besedina D. (%),
#               Setskov M.  (%).
import os
import os.path

def acceptCommand():
    pass

def runCommand(command):
    pass

def moveUp():
    pass

def moveDown(currentDir):                                           #!!!!! (Диане) эту функцию в основном меню напускать от os.getcwd()
    newDir = input('Введите название нужного вам подкаталога: ')
    while True:
        try:
            os.chdir(currentDir + '\\' + newDir)
            break
        except:
            print('Такого подкаталога не существует.')
            newDir = input('Введите корректное название католога: ')
    print('Вы находитесь в данном каталоге:')
    print(os.getcwd())

def countFiles(path):
    pass

def countBytes(path):
    pass

def findFiles(target,path):
    pass


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command=acceptCommand()
        runCommand(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break
