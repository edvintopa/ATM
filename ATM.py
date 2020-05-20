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
        self._balance = _balance
    
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
            self._balance += amount
    
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

#Main windows which will hold the pages (frames)
class Body(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #Initiates all pages (frames)
        for F in (StartPage, AccountPage, LoginPage, RegisterPage):

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

        btn_login = tk.Button(self, text="Login", command= _Login()).grid(row=3, column=0)
        btn_back = tk.Button(self, text="Back", command= lambda: controller.show_frame(StartPage)).grid(row=3, column=1)

        def _Login():
            entry_uName = self.entry_uName
            entry_PIN = self.entry_PIN

            if len(entry_uName) > 0 and len(entry_PIN) > 0:
                #attempt login
            else:
                messagebox.showerror("Error", "Fill in all forms")

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
        entry_firstname = self.entry_firstname.get().lower()
        entry_lastname = self.entry_lastname.get().lower()
        
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
            messagebox.showerror("Error", "Fill in all forms")       


class AccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome" + "Edvin")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        

#Runs the main windows
root = Body()
root.mainloop()