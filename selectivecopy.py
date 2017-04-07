import shutil, os

spath = input("Enter Source Path: ")
npath = input("Enter New Path")

def searchandcopy(sourcepath,newpath):
    for folderName, subfolders, filenames in os.walk(sourcepath):
        print('The current folder is ' + folderName)
        for filename in filenames:
            if filename.endswith(".pdf") or filename.endswith(".zip"):
                shutil.copy(folderName+ filename, newpath)
                print('The new folder is ' + newpath)


    print('')

searchandcopy(spath,npath)




