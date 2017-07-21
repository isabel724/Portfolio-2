import random

tries = 0
diceNumber = random.randint (1,6)
guessed = False

while tries < 3 and not guessed:
    guess = ""
    while not guess in ["1", "2", "3", "4", "5", "6"]:
      guess = input ("Please enter a guess for the number rolled (1-6)")
    guess = int(guess)

    if diceNumber == guess:
        print ("You guess correctly!")
        guessed = True
    else:
        tries += 1
        if tries < 3: print("That is incorrect, please try again...")
        else: print ("You lose! The number was " + str(diceNumber))
