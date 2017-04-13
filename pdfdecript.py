import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted
True
pdfReader.decrypt('rosebud')
pdfReader.getPage(0)
pageObj = pdfReader.getPage(0)

