# Case-study #12
# Developers:   Besedina D. (50%),
#               Setskov M.  (%).
import os
import os.path

def acceptCommand():
    command = input()
    while type(command) != int:
        try:
            command = int(command)
            while command > 7:
                answer = 'ERROR'
                print(answer)
                command = int(input())
            return command
        except ValueError:
            print('ERROR')
            command = input()
def runCommand(command):
    if command == 1:
        path = os.getcwd()
        print(os.listdir(path))
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown()
    elif command == 4:
        path = input()
        countFiles(path)
    elif command == 5:
        countBytes()
    elif command == 6:
        findFiles()
    elif command == 7:
        print('Работа программы завершена.')
        pass
def moveUp():
    import os
    path = os.getcwd()
    up_dir = os.path.dirname(path)
    os.chdir(up_dir)
    path = os.getcwd()
    print(path)

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
    import os
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            # print('спускаемся',path + '\\' + i)
            countFiles(path + '\\' + i)
            # print('возвращаемся в',path)
        if os.path.isfile(path + '\\' + i):
            return len(os.listdir(path))
            print(len(os.listdir(path)))
    pass

def countBytes(path):
    pass

def findFiles(target,path):
    pass


def main():
    while True:
        print(os.getcwd())
        print("1. Просмотр каталога")
        print("2. На уровень вверх")
        print("3. На уровень вниз")
        print("4. Количество файлов и каталогов")
        print("5. Размер текущего каталога (в байтах)")
        print("6. Поиск файла")
        print("7. Выход из программы")
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            break
main()
