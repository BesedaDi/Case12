
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
