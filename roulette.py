import random

validInput = False
while not validInput:
    money = input ("Please enter the amount of money to start: ")
    if money.isdigit():
        money = int(money)
        if money > 0: validInput = True

keepPlaying = True

while keepPlaying:
    validInp = False
    while not validInp:
        bet = input ("How much would you like to bet (type 'all' to bet all): ")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0 and bet <= money: validInp = True
        elif bet.lower() == "all":
            bet = money
            validInp = True


    pocket = random.randint(1,36)

    print("How do you want to play?")
    typeOfPlay = ""
    while not typeOfPlay in ["1","2","3"]:
      typeOfPlay = input ("Guess- color(1), even/odd(2), number(3): ")

    if typeOfPlay == "1":
        #color (red/black)
        guess = ""
        while not guess in ["r", "b"]:
            guess = input ("Please guess red(r) or black(b): ").lower()

        if (pocket % 2 == 0 and guess == "b") or (pocket % 2 == 1 and guess == "r"):
            print ("You guessed correctly!")
            money += bet
        else:
            print ("Sorry, that is incorrect...")
            money -= bet


    elif typeOfPlay == "2":
        #even/odd
        guess = ""
        while not guess in ["e", "o"]:
            guess = input ("Please guess even(e) or odd(o): ").lower()

        if (pocket % 2 == 0 and guess == "e") or (pocket % 2 == 1 and guess == "o"):
            print ("You guessed correctly!")
            money += bet
        else:
            print ("Sorry, that is incorrect...")
            money -= bet


    else:
        #number
        guess = ""
        valid = False
        while not valid:
            guess = input ("Please guess number (1-36): ")
            if guess.isdigit():
                guess = int(guess)
                if guess > 0 and guess <= 36: valid = True

        if guess == pocket:
            print ("You guessed correctly!")
            money += bet * 36
        else:
            print ("Sorry, that is incorrect...")
            money -= bet

    print("You currently have $" + str(money))

    if money == 0: playing = "n"
    else: playing = ""

    while not playing in ["y", "n"]:
        playing = input ("Do you want to play again? yes(y) or no(n): ").lower()

    if playing == "y": keepPlaying = True
    else: keepPlaying = False


print("You end with $" + str(money))
