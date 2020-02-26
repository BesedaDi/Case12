# Case-study #12
# Developers:   Besedina D. (%),
#               Setskov M.  (%).
def acceptCommand():
    pass
def runCommand(command):
    pass
def moveUp():
    pass
def moveDown():
    pass
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