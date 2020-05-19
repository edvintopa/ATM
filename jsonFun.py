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

def readFromFile():
    with open("User_Data.txt", "r") as file:
        inputString = json.loads(file)
        print(inputString)

def test():
    json_string = '[{"uName": "user1", "_PIN": "1111", "_firstname": "user", "_lastname": "one", "_balance": 0}, {"uName": "user2", "_PIN": "2222", "_firstname": "user", "_lastname": "two", "_balance": 0}, {"uName": "user3", "_PIN": "3333", "_firstname": "user", "_lastname": "three", "_balance": 0}]'

    data = json.loads(json_string)

    userData = data

    print(userData[0])

test()