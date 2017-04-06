import os, re
filteri= input("Enter the Filter: ")
arqpath = input("Enter the Path: ")
filterre = re.compile(r'%s'%filteri)
result = []
for filename in os.listdir(arqpath):
    if filename.endswith(".txt"):
        my_textfile = open(os.path.basename(arqpath+filename), 'r')
        for line in my_textfile:
            result = filterre.search(line)
        my_textfile.close()
print (result.group())
