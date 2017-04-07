import shutil, os

spath = input("Enter Source Path: ")

def searchandcopy(sourcepath):
    for folderName, subfolders, filenames in os.walk(sourcepath):
        print('The current folder is ' + folderName)
        for filename in filenames:
            if os.path.getsize(filename) == 100000000:
                 print('The folder is ' + folderName)


    print('')

searchandcopy(spath)
