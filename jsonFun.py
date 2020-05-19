import json

class Account:
    #Constructor for account creation
    def __init__(self, PIN, firstname, lastname):
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

user1 = Account("0000", "John", "Johnsson")

f = open("User_Data.txt", "w+")

users = f.read()

users = users + user1.toJson() + "\n"

f.write(users)