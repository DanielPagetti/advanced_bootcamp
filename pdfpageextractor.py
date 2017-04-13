import PyPDF2
pdfFileObj = open('Automate_the_Boring_Stuff_sample_ch17.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
