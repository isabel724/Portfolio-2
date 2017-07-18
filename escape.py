import time

def printMessage(message):
    print(message)
    time.sleep(1)

def choose(choices):
    for choice in range(len(choices)):
        print("Option " + str(choice+1) + ": " + choices[choice])

    while True:
        userChoice = input("Please enter your choice (#) ")
        if userChoice.isdigit():
            userChoice = int(userChoice)
            if userChoice > 0 and userChoice <= len(choices):
                return (userChoice-1)

def printIntro():
    printMessage ("There is a nameless serial killer on the loose. It is your task to defend yourself against this maniac.")
    printMessage ("You will have options to choose your defense.")
    printMessage ("Choose the number of the option in order to use it and follow that route.")
    printMessage ("This bloodthirsty killer is notorious for his unconvential methods. ")
    printMessage ("Beware and make wise decisions for your sake!")
    print()

def main():
    print ("Hello! Welcome to Escape.")
    name = input ("What is your name?: ")
    printIntro()

    printMessage ("You are sitting in your living room reading Harry Potter, when you hear a knock on the door...")
    printMessage ("You look through the window in your peephole-less cabin in the middle of the woods...")
    printMessage ("You see an unknown man at the door holding a pickaxe. He sees your face struck with terror in the window...")
    printMessage ("'" + name + "!' he calls out quietly through the door...")
    printMessage ("With three easy strokes, he rips through your door. Now you must decide what to do...")

    currentChoices = ["Run into the house", "Run out the back door"]
    choiceNumber = choose(currentChoices)
    if choiceNumber == 0:
        printMessage ("You have chosen to run into the house.")
        currentChoices = ["Grab a weapon", "Go hide"]
        choiceNumber = choose(currentChoices)
        if choiceNumber == 0:
            printMessage ("You choose to grab a weapon.")
            currentChoices = ["Knife", "Revolver", "Baseball Bat"]
            choiceNumber = choose(currentChoices)
            if choiceNumber == 0:
                printMessage("You run into the kitchen and grab a knife.")
                printMessage("You plunge a knife into his heart and he immediately collapses as he clutches onto his soaked black t shirt.")
                printMessage("He suffers a long, plainful death as his blood pools onto your wooden floors.")
                printMessage("You call the police and you are arrested for first degree murder. Your trial begins the next month... ")
            elif choiceNumber == 1:
                printMessage("You search around frantically for a minute, then grab your revolver.")
                printMessage("You shoot him and the bullets pierces his arm.")
                printMessage("He falls to the ground and swerve past him to run to the police station.")
                printMessage("The police arrive, arrest the nameless serial killer, and he is charged for intrusion and attempted murder.")
            else:
                printMessage("You grab your late brother's baseball bat.")
                printMessage("You swing the bat towards his head and he dodges.")
                printMessage("He grabs a hold of your arm and stabs you repeatdly.")
                printMessage("You die a slow, painful death.")
        else:
            printMessage ("You choose to go hide.")
            currentChoices = ["In cabinet", "Under bed", "Closet"]
            choiceNumber = choose(currentChoices)
            if choiceNumber == 0:
                printMessage("You curl up into a ball in the kitchen cabinet.")
                printMessage("He crosses by you and searches for you around the house.")
                printMessage("He opens the cabinet next to you")
                printMessage("and grabs some twinkies.")
                printMessage("After an hour, he leaves.")
                printMessage("Fortunately, he never kills you, but you never catch him.")
                printMessage("You immediately get a security system for your protection.")
            elif choiceNumber == 1:
                printMessage("You run upstairs and dive under your bed.")
                printMessage("The first checks is under the bed in your room.")
                printMessage("You roll to the other side of the bed.")
                printMessage("He notices the ruffling and goes to investigate.")
                printMessage("You jump up and sprint.")
                printMessage("He chases you around the room and grabs a hold of your nightgown.")
                printMessage("He stabs you in the back with his imfamous carving knife and you drop dead.")
            else:
                printMessage("You run upstairs and get into your closet in a pile of clothes.")
                printMessage("He walks up to you room, checks under your bed and approaches the closet.")
                printMessage("He opens it and you realize you are screwed because you have nowhere to run.")
                printMessage("'Hello " + name + "' he says, a smile creeping up onto his face.'")
                printMessage("He shoots you and you collapse on a pile of clothes.")
                printMessage("He stabs you again to ensure you are dead and for his satisfaction.")
                printMessage("Finally, the sweet release of death embraces you.")
    else:
        printMessage ("You have chosen to run out the back door.")
        currentChoices = ["Run to the street", "Run into the forest"]
        choiceNumber = choose(currentChoices)
        if choiceNumber == 0:
            printMessage("You ran to the street")
            currentChoices = ["Go to neighbor's house", "Run to police"]
            choiceNumber = choose(currentChoices)
            if choiceNumber == 0:
                printMessage("You have ran to your neighbor, Eddy's, door.")
                printMessage("The nameless killer takes a shortcut through your woods.")
                printMessage("He gets caught in your neighbor's bear trap while you are banging on Eddy's door.")
                printMessage("Your neighbor comes out with a gun and points at you.")
                printMessage("'" + name + "?' Eddy asks, confused.")
                printMessage("When he realizes what has just occured with the killer, he shoots him.")
                printMessage("The murderer dies.")
            else:
                printMessage("You start running towards the police station, as fast as possible.")
                printMessage("The station is 3 long blocks away.")
                printMessage("After running for 2 blocks, he catches you.")
                printMessage("A neighbor sees and calls the cops.")
                printMessage("They quickly arrive at the scene.")
                printMessage("A violent shootout occurs.")
                printMessage("'Ma'am? Are you alright?' a police officer asks, approaching you.")
                printMessage("The serial killer is arrested, and you are finally safe.")
        else:
            printMessage("You ran into the forest")
            currentChoices = ["Climb a tree", "Keep running"]
            choiceNumber = choose(currentChoices)
            if choiceNumber == 0:
                printMessage("You find a tree with lower branches and climb it.")
                printMessage("He never sees you run out of your cabin.")
                printMessage("He searches the entire house and after an hour, looks for you in the forest.")
                printMessage("He looks around for a bit and he figures that you have ran away.")
                printMessage("He leaves without you ever seeing his face.")
                printMessage("Hence, he is never caught.")
            else:
                printMessage("Once you reach the forest, you hit a dead sprint and keep going.")
                printMessage("You run for what feels like hours.")
                printMessage("You eventually come to a highway.")
                printMessage("You realize to late that you have ran onto the highway when a car fails to stop.")
                printMessage("The car runs you over.")
                printMessage("You are admitted into the hospital and later declared dead on the operating table.")

main()
