import re

phoneNumRegex = re.compile(r'\S\S\S\S\S@\S\S.\S\S\S.\S\S\S')
mo = phoneNumRegex.search('My number dofJLajlkajdkjAF; dpagetti@br.ibm.com is 415-555-4242 SAKDJLajflkAJF;Lkjlksadjsalkdj.')

print (mo.group())



print('Phone number found: ' + mo.group())
