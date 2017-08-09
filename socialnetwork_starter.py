class User:
    # Define the fields and methods for your object here.
    def __init__ (self, name, years):
        self.username = name
        self.connections = []
        self.age = years
    def changeName(self, name):
        self.username = name
    def addConnection(self, user):
        self.connections.append(user)
    def getName(self):
        return self.username
    def getConnections(self):
        people = []
        for person in self.connections:
            people.append(person.getName())
        return people



class Network:
    # Define the fields and methods for your object here.
    def __init__ (self):
        self.users = []
    def addUser (self, user):
        self.users.append(user)
    def getUsernames (self):
        people = []
        for person in self.users:
            people.append(person.getName())
        return people
    def getUsers (self):
        return self.users

def main():
    # Define the program flow for your user interface here.
    keepRunning = True
    network = Network()
    name = input("Username: ")
    age = 0
    while age == 0 or not age.isdigit():
        age = input("Age: ")
    network.addUser(User(name, age))

    while keepRunning:
        print ("Choose an option:")
        print ("Add user(au), print users(pu), add connection(ac), print connections(pc), end (e)")
        choice = ""
        while choice not in ['au', 'pu', 'ac', 'pc', 'e']:
            choice = input ("Choose: ").lower()

        if choice == 'au':
            name = ''
            while name == '' or name in network.getUsernames():
                name = input ("Username: ")
            age = 0
            while age == 0 or not age.isdigit():
                age = input("Age: ")
            network.addUser(User(name, age))
        elif choice == 'pu':
            people = network.getUsernames()
            for person in people: print (person)
        elif choice == 'ac':
            person1 = ''
            person2 = ''
            while person1 == '' or person1 not in network.getUsernames():
                person1 = input ('Enter a user: ')
            while person2 == '' or person2 not in network.getUsernames():
                person2 = input ('Enter another user: ')
            for person in network.getUsers():
                if person.getName() == person1:
                    thisPerson1 = person
                    break
            for person in network.getUsers():
                if person.getName() == person2:
                    thisPerson2 = person
                    break
            thisPerson1.addConnection(thisPerson2)
            thisPerson2.addConnection(thisPerson1)
        elif choice == 'pc':
            user = ''
            while user == '' or user not in network.getUsernames():
                user = input ("Enter a user: ")
            for person in network.getUsers():
                if person.getName() == user:
                    thisPerson = person
                    break
            people = thisPerson.getConnections()
            for person in people: print (person)
        elif choice == 'e':
            keepRunning = False
            print ("You have left the program")




# Runs your program.
if __name__ == '__main__':
    main()
