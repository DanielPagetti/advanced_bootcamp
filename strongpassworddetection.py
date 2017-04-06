import re

passw = input("Type Your Passwrod: ")

pwdcheck = re.compile(r'''(
     (?=.*[a-z]) # use positive lookahead to see if at least one lower case letter exists
     (?=.*[A-Z]) # use positive lookahead to see if at least one upper case letter exists
     (?=.*\d)    # use positive lookahead to see if at least one digit exists
     [A-Za-z0-9@#$%^&!+=]{8,}  # match any character in [] at least 8 times
     )''', re.VERBOSE)

def checkpwd(pwd,pwdcheck):
    if pwdcheck.match(pwd):
        return "Strong"
    else:
        return "Weak"


print (checkpwd(passw,pwdcheck))
