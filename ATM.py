# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

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

#Functions for loading and saving userdata from textfile
def writeFile(userList):
    json_string = json.dumps([Account.__dict__ for Account in userList])

    with open("User_Data.txt", "w") as file:
        file.write(json_string)

def readFile():
    userList = []
    with open("User_Data.txt", "r") as file:
        user_data = json.loads(file.read())
        for u in user_data:
            userList.append(Account(**u))
    return userList

#Loads and initiates global list with user data att program launch
userList = readFile()
currentUserIndex = 0

#Main windows which will hold the pages (frames)
class Body(tk.Tk):

    #Solution to my lable updates
    self.name = tk.StringVar()
    self.name.set("N/A")
    self.balance = tk.StringVar()
    self.balance.set("N/A")

    #Updates the displayed info on accountpage
    def updateUserInfo():
        self.name.set(userList[currentUserIndex].getFirstname() + " " + userList[currentUserIndex].getLastname())
        self.balance.set("Balance: " + userList[currentUserIndex].getBalance())

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #Initiates all pages (frames)
        for F in (StartPage, AccountPage, LoginPage, RegisterPage, DepositPage, WithdrawalPage, SettingsPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#Page made from inherited frame. Welcomes the user and promts them to sign in or register      
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the CyberATM!").grid(row=0, column=0)

        btn_login = tk.Button(self, text="Sign in",
                            command= lambda: controller.show_frame(LoginPage)).grid(row=1, column=0)

        btn_reg = tk.Button(self, text="Register",
                            command= lambda: controller.show_frame(RegisterPage)).grid(row=1, column=1)

#Lets the user sign in
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_accID = tk.Label(self, text="Username").grid(row=1, column=0)
        self.entry_uName = tk.Entry(self)
        self.entry_uName.grid(row=1, column=1)

        label_PIN = tk.Label(self, text="PIN").grid(row=2, column=0)
        self.entry_PIN = tk.Entry(self, show="*")
        self.entry_PIN.grid(row=2, column=1)

        btn_login = tk.Button(self, text="Login", command= self._Login)
        btn_login.grid(row=3, column=0)
        btn_back = tk.Button(self, text="Back", command= lambda: controller.show_frame(StartPage)).grid(row=3, column=1)

    def _Login(self):
            entry_uName = self.entry_uName.get()
            entry_PIN = self.entry_PIN.get()

            if len(entry_uName) > 0 and len(entry_PIN) > 0:
                uNameList = []
                for user in range(len(userList)):
                    uNameList.append(userList[user].getuName())
                
                if entry_uName in uNameList:
                    currentUserIndex = uNameList.index(entry_uName)

                    if userList[currentUserIndex].getPIN() == entry_PIN:
                        self.controller.show_frame(AccountPage)
                    
                    else:
                        messagebox.showerror("Error!", "Wrong PIN!")
                else:
                    messagebox.showerror("Error!", "User does not exist!")
            else:
                messagebox.showerror("Error!", "Fill in all forms!")

#Creates new account and stores it in text file
class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_uName = tk.Label(self, text= "Username").grid(row=0, column=0)
        self.entry_uName = tk.Entry(self)
        self.entry_uName.grid(row=0, column=1)

        label_firstname = tk.Label(self, text= "First name").grid(row=1, column=0)
        self.entry_firstname = tk.Entry(self)
        self.entry_firstname.grid(row=1, column=1)

        label_lastname = tk.Label(self, text= "Last name").grid(row=2, column=0)
        self.entry_lastname = tk.Entry(self)
        self.entry_lastname.grid(row=2, column=1)

        label_PIN = tk.Label(self, text="PIN").grid(row=3, column=0)
        self.entry_PIN = tk.Entry(self, show="*")
        self.entry_PIN.grid(row=3, column=1)

        btn_reg = tk.Button(self, text="Register", command= self._Register)
        btn_reg.grid(row=4, column=0)
        btn_back = tk.Button(self, text="Back", command= lambda: controller.show_frame(StartPage)).grid(row=4, column=1)

    def _Register(self):
        entry_uName = self.entry_uName.get()
        entry_PIN = self.entry_PIN.get()
        entry_firstname = self.entry_firstname.get()
        entry_lastname = self.entry_lastname.get()
        
        if len(entry_uName) > 0 and len(entry_PIN) > 0 and len(entry_firstname) > 0 and len(entry_lastname):
            #Checks if username is avalible
            uNameList = []
            for user in range(len(userList)):
                uNameList.append(userList[user].getuName())
        
            if entry_uName in uNameList:
                messagebox.showerror("Error!", "Username already in use!")
            else:
                userList.append(Account(entry_uName, entry_PIN, entry_firstname, entry_lastname, 0))
                messagebox.showinfo("Operation successfull!", "User registered!")
                writeFile(userList)
        else:
            messagebox.showerror("Error!", "Fill in all forms!")       

class AccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_name = tk.Label(self, textvariable=name).grid(row=0, column=0)
        label_desc = tk.Label(self, text="What would you like to do today?").grid(row=1, column=0)
        label_balance = tk.Label(self, textvariable=balance).grid(row=2, column=0)

        btn_deposit = tk.Button(self, text="Deposit", command=lambda: controller.show_frame(DepositPage)).grid(row=3, column=0)
        btn_withdraw = tk.Button(self, text="Withdraw", command=lambda: controller.show_frame(WithdrawalPage)).grid(row=3, column=1)
        btn_settings = tk.Button(self, text="Settings", command=lambda: controller.show_frame(SettingsPage)).grid(row=4, column=0)
        btn_logout = tk.Button(self, text="Log out", command=lambda: controller.show_frame(StartPage)).grid(row=4, column=1)

class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_deposit = tk.Label(self, text="Deposition").grid(row=0, column=0)
        label_amount = tk.Label(self, text="Amount:").grid(row=1, column=0)

        self.entry_amount = tk.Entry(self)
        self.entry_amount.grid(row=1, column=1)

        btn_deposit = tk.Button(self, text="Deposit", command= self._Deposit).grid(row=2, column=0)
        btn_cancel = tk.Button(self, text="Cancel", command=lambda: controller.show_frame(AccountPage)).grid(row=2, column=1)
    
    def _Deposit(self):
        entry_amount = self.entry_amount.get()
        amount = int(entry_amount)
        if len(entry_amount) > 0 and int(entry_amount) > 0:
                userList[currentUserIndex].deposit(int(entry_amount))
                writeFile(userList)
        else:
            messagebox.showerror("Error!", "Invalid amount!")

class WithdrawalPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_withdrawal = tk.Label(self, text="Withdrawal").grid(row=0, column=0)
        label_amount = tk.Label(self, text="Amount:").grid(row=1, column=0)

        self.entry_amount = tk.Entry(self)
        self.entry_amount.grid(row=1, column=1)

        btn_withdrawal = tk.Button(self, text="Withdraw", command= self._Withdrawal).grid(row=2, column=0)
        btn_cancel = tk.Button(self, text="Cancel", command=lambda: controller.show_frame(AccountPage)).grid(row=2, column=1)
    
    def _Withdrawal(self):
        entry_amount = self.entry_amount.get()
        amount = int(entry_amount)
        if len(entry_amount) > 0 and int(entry_amount) > 0:
            if userList[currentUserIndex].getBalance() > int(entry_amount):
                userList[currentUserIndex].withdrawal(int(entry_amount))
                writeFile(userList)
            else:
                messagebox.showerror("Error!", "Insufficient funds!")
        else:
            messagebox.showerror("Error!", "Invalid amount!")

class SettingsPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_settings = tk.Label(self, text="Settings").grid(row=0, column=0)

        label_uName = tk.Label(self, text= "Username").grid(row=1, column=0)
        self.entry_uName = tk.Entry(self)
        self.entry_uName.grid(row=1, column=1)

        label_firstname = tk.Label(self, text= "First name").grid(row=2, column=0)
        self.entry_firstname = tk.Entry(self)
        self.entry_firstname.grid(row=2, column=1)

        label_lastname = tk.Label(self, text= "Last name").grid(row=3, column=0)
        self.entry_lastname = tk.Entry(self)
        self.entry_lastname.grid(row=3, column=1)

        label_PIN = tk.Label(self, text="PIN").grid(row=4, column=0)
        self.entry_PIN = tk.Entry(self, show="*")
        self.entry_PIN.grid(row=4, column=1)

        btn_save = tk.Button(self, text="Save", command=self._Save).grid(row=5, column=0)
        btn_cancel = tk.Button(self, text="Cancel", command= self.controller.show_frame(AccountPage)).grid(row=5, column=1)
    
    def _Save(self):
        entry_uName = self.entry_uName.get()
        entry_PIN = self.entry_PIN.get()
        entry_firstname = self.entry_firstname.get()
        entry_lastname = self.entry_lastname.get()
        
        if len(entry_uName) > 0 and len(entry_PIN) > 0 and len(entry_firstname) > 0 and len(entry_lastname):
            #Checks if username is avalible
            uNameList = []
            for user in range(len(userList)):
                uNameList.append(userList[user].getuName())
        
            if entry_uName in uNameList:
                messagebox.showerror("Error!", "Username already in use!")
            else:
                userList.append(Account(entry_uName, entry_PIN, entry_firstname, entry_lastname, 0))
                messagebox.showinfo("Operation successfull!", "User settings changed!")
                userList.pop(currentUserIndex)
                writeFile(userList)
                self.controller.show_frame(StartPage)
        else:
            messagebox.showerror("Error!", "Fill in all forms!")

#Runs the main window
root = Body()
root.mainloop()