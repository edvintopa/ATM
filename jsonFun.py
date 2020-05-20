import json

class Account:
    #Constructor for account creation
    def __init__(self, uName, _PIN, _firstname, _lastname, _balance):
        self.uName = uName
        self._PIN = _PIN
        self._firstname = _firstname
        self._lastname = _lastname
        self._balance = _balance
    
    #Getters for accessing private variables
    def getPIN(self):
        return self._PIN
    def getFirstname(self):
        return self._firstname
    def getLastname(self):
        return self._lastname
    def getBalance(self):
        return self._balance

    #Setters for changing information or loading users from file
    def setPin(self, input):
        self._PIN = input
    def setFirstname(self, input):
        self._firstname = input
    def setLastname(self, input):
        self._lastname = input
    #setBalance will not be accessible by the user, for obvious reasons.
    def setBalance(self, input):
        self._balance = input

    #Balance is changed deposit and withdrawal methods
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdrawal(self, amount):
        if self._balance > amount and amount > 0:
            self._balance -= amount
    
def writeFile(userList):
    usersArray = json.dumps([Account.__dict__ for Account in userList])

    with open("User_Data.txt", "w") as file:
        file.write(usersArray)

def readFile():
    userList = []
    with open("User_Data.txt", "r") as file:
        user_data = json.loads(file.read())
        for u in user_data:
            userList.append(Account(**u))
    return userList

#users = readFromFile()
#print(users[0].getBalance())
