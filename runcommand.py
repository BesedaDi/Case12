def runCommand(command):
    if command==1:
        acceptCommand()
    elif command ==2:
        moveUp()
    elif command == 3:
        moveDown()
    elif command == 4:

        countFiles()
    elif command == 5:
        countBytes()
    elif command == 6:
        findFiles()
    elif command == 7:
        print('Работа программы завершена.')
        break