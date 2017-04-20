import PyPDF2, os

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted
True

my_textfile = open(os.path.basename('dictionary.txt'), 'r')
decr = False
for line in my_textfile:
    decr = pdfReader.decrypt(line)
    print (line)
    if decr == True:
        print (line)
        pdfReader.getPage(0)
my_textfile.close()



