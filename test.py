import tkinter as tk
from tkinter import messagebox
import json

#Blueprint class for accounts
class Account:
    #Constructor for account creation
    def __init__(self, _uName, _PIN, _firstname, _lastname, _balance):
        self._uName = _uName
        self._PIN = _PIN
        self._firstname = _firstname
        self._lastname = _lastname
        self._balance = int(_balance)
    
    #Getters for accessing private variables
    def getuName(self):
        return self._uName
    def getPIN(self):
        return self._PIN
    def getFirstname(self):
        return self._firstname
    def getLastname(self):
        return self._lastname
    def getBalance(self):
        return self._balance

    #Setters for changing information (ecxept balance, this has special methods)
    def setuName(self, input):
        self._uName = input
    def setPin(self, input):
        self._PIN = input
    def setFirstname(self, input):
        self._firstname = input
    def setLastname(self, input):
        self._lastname = input

    #Balance needs deposit and withdrawal methods
    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
    
    def withdrawal(self, amount):
        if self._balance > amount and amount > 0:
            self._balance -= amount
            messagebox.showinfo("Operation successfull!", "Successfully withdrawed " + amount)
        else:
            messagebox.showerror("Error!", "Invalid amount or insufficient funds!")

user = Account("user1", "1111", "first", "last", "0")

entry_amount = "637"

if len(entry_amount) > 0:
    try:
        amount = int(entry_amount)
        user.deposit(amount)
    except:
        print("Error")