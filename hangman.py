import random

words = ["eddy", "ball", "cat", "dog", "fish", "hamster"]

word = list(words[random.randint(0,len(words)-1)])
guessed = [""] * len(word)

print("_ " * len(word))

done = False

while not done:
    guessLetter = input ("Please enter you guess: ")
    if guessLetter in word:
        for letter in range(len(word)):
            if word[letter] == guessLetter:
                guessed[letter] = guessLetter

    for x in guessed:
        if x == '': print ("_", end = " ")
        else: print (x, end = " ")
    print()

    if word == guessed: done = True

for x in word:
    print (x, end = "")
