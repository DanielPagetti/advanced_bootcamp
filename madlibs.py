my_textfile = open('textfile.txt', 'w')
my_textfile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
my_textfile.close()


ADJECTIVE = input("Enter an adjective: ")
NOUN = input("Enter a noun: ")
ADVERB = input("Enter an adverb: ")
VERB = input("Enter a verb: ")

my_textfile = open('textfile.txt', 'r')
new_text=""
for row in my_textfile:
    wd = ""
    for word in row:
        if word != " " or word != "." :
            wd = wd + word
        else:
            print (wd)
            if wd == "ADJECTIVE":
                new_text = new_text + " " + ADJECTIVE
            elif wd == "NOUN":
                new_text = new_text + " " + NOUN
            elif wd == "ADVERB":
                new_text = new_text + " " + ADVERB
            elif wd == "VERB":
                new_text = new_text + " " + VERB
            else:
                new_text = new_text + " " + wd
            wd = ""
my_textfile.close()

my_textfile = open('textfile.txt', 'w')
my_textfile.write(new_text)
my_textfile.close()


