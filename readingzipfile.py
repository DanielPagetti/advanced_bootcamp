import zipfile, os
newZip = zipfile.ZipFile('example', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

os.chdir('C:\\Users\\IBM_ADMIN\\Desktop\\advanced_bootcamp\\advanced_bootcamp\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
'Compressed file is 3.63x smaller!'
exampleZip.close()
