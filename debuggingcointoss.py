import random
guess = ''
rep =""
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
    rep ="tails"
elif toss == 1:
    rep ="heads"
if rep == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if rep == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
