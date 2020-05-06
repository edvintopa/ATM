# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import tkinter as tk

#Blueprint class for accounts
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

        login_Btn = tk.Button(self, text="Sign in",
                            command= lambda: controller.show_frame(LoginPage)).grid(row=1, column=0)

        reg_Btn = tk.Button(self, text="Register",
                            command= lambda: controller.show_frame(RegisterPage)).grid(row=1, column=1)

#Lets the user sign in
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_accID = tk.Label(self, text="ID").grid(row=1, column=0)
        self.entry_accID = tk.Entry(self)
        self.entry_accID.grid(row=1, column=1)

        label_PIN = tk.Label(self, text="PIN").grid(row=2, column=0)
        self.entry_PIN = tk.Entry(self, show="*")
        self.entry_PIN.grid(row=2, column=1)

        btn_login = tk.Button(self, text="Login", command= self._login()).grid(row=3, column=0)
        btn_back = tk.Button(self, text="Back", command= lambda: controller.show_frame(StartPage)).grid(row=3, column=1)

    def _login(self):
        #The account ID is the line where the user info is stored in the users file
        entry_accID = self.entry_accID.get()
        entry_PIN = self.entry_PIN.get()

        #Reads users from txt file and enters them into a list
        file = open("test.txt","r")
        users = file.readlines()

        currentUser = users[2].split(",")

        currentLogin = Account(currentUser[0],currentUser[1],currentUser[2])

        if entry_PIN == currentLogin.getPIN():
            self.controller.show_frame(AccountPage)
        else:
            print("Error")


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_firstname = tk.Label(self, text= "First name").grid(row=0, column=0)
        label_lastname = tk.Label(self, text= "Last name").grid(row=1, column=0)



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