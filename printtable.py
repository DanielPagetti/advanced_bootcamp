tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    for x in table:
        line = ""
        for item in x:
            line = line + " " + item
        print (line)
printTable(tableData)


