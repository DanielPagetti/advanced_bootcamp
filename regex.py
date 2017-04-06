import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')

print (mo.group())

mo2 = phoneNumRegex.search('My  is 415-555-4242.')

print (mo2.group())


print('Phone number found: ' + mo.group())
