# Case-study #12
# Developers:   Besedina D. (55%),
#               Setskov M.  (45%).
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
        moveDown(os.getcwd())
    elif command == 4:
        path = input()
        countFiles(path)
    elif command == 5:
        countBytes()
    elif command == 6:
        findFiles()
    elif command == 7:
        print('Работа программы завершена.')
        
def moveUp():
    path = os.getcwd()
    up_dir = os.path.dirname(path)
    os.chdir(up_dir)
    path = os.getcwd()
    print(path)

def moveDown(currentDir):
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
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            countFiles(path + '\\' + i)
        if os.path.isfile(path + '\\' + i):
            return len(os.listdir(path))

def files(path_for_getsize):
    files_list = []
    for file in os.listdir(path_for_getsize):
        path = os.path.join(path_for_getsize, file)
        if not os.path.isdir(path):
            files_list.append(path)
        else:
            files_list += files(path)
    return files_list

def countBytes():
    path_for_getsize = input('Введите директорию для подсчета суммарного объема всех файлов: ')
    size = 0
    for each_dir in files(path_for_getsize):
        size += os.path.getsize(each_dir)
    return size
    

def findFiles(target,path):
    targetsList = []
    target = input('Введите часть или полное имя файла, список путей к которму вам необходимо найти: ')
    path = input('Введите директорию, в которой нужно произвести поиск: ')
    for each_dir in files(path):
        if each_dir.find(target) != -1:
            targetsList.append(each_dir)
    if targetsList != []:
            return targetsList
    else:
        return 'Файлы не найдены.'


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
