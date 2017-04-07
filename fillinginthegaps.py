import shutil, os, re

spath = input("Enter Source Path: ")

NumberPattern = re.compile(r'''(\d\d\d)''',re.VERBOSE)

def searchandcopy(sourcepath,npattern):
    for folderName, subfolders, filenames in os.walk(sourcepath):
        lastnumber = 0
        for filename in filenames:
            if filename.startswith("spam") and filename.endswith(".txt"):
                actualn = 0
                print('The filename is ' + filename)
                actualn = npattern.search(filename)
                if int(actualn.group()) != lastnumber + 1:
                    print (actualn.group())

                    shutil.move(folderName+filename, folderName+ "spam" + "00" + str(lastnumber + 1) +".txt")
                else:
                    lastnumber= int(actualn.group())
                    print (lastnumber)


    print('')

searchandcopy(spath,NumberPattern)
