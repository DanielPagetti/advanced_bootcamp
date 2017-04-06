import shelve

shelfFile = shelve.open('mydata')
type(shelfFile)
shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
shelfFile.close()

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
['cats']
print (list(shelfFile.values()))
[['Zophie', 'Pooka', 'Simon']]
shelfFile.close()



