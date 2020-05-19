import json

class Account:
    #Constructor for account creation
    def __init__(self, uName, PIN, firstname, lastname):
        self.uName = uName
        self._PIN = PIN
        self._firstname = firstname
        self._lastname = lastname
        self._balance = 0
    
    #Getters for accessing private variables
    def getPIN(self):
        return self._PIN
    def getFirstname(self):
        return self._firstname
    def getLastname(self):
        return self._lastname
    def getBalance(self):
        return self._balance

    #Setters for changing information (ecxept balance, these have special methods)
    def setPin(self, input):
        self._PIN = input
    def setFirstname(self, input):
        self._firstname = input
    def setLastname(self, input):
        self._lastname = input

    #Balance needs deposit and withdrawal methods
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdrawal(self, amount):
        if self._balance > amount and amount > 0:
            self._balance -= amount
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
def saveToFile():
    #example accounts
    user1 = Account("user1", "1111", "user", "one")
    user2 = Account("user2", "2222", "user", "two")
    user3 = Account("user3", "3333", "user", "three")
    usersList = [user1, user2, user3]
    
    usersArray = json.dumps([Account.__dict__ for Account in usersList])

    with open("User_Data.txt", "w") as file:
        file.write(usersArray)

#load balance aswell
def readFromFile():
    with open("User_Data.txt", "r") as file:
        data = json.loads(file.read())

        users = []
        for x in len(data):
            currentUser = data[x]

            uName = currentUser["uName"]
            PIN = currentUser["_PIN"]
            firstname = currentUser["_firstname"]
            lastname = currentUser["_lastname"]

            users.append(Account(uName, PIN, firstname, lastname))
        
        print(users[0].getLastname)

        #currentUser = data[2]
        #print(currentUser["_lastname"])


readFromFile()