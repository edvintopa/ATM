import tkinter as tk

#Main windows which will hold the pages
class Body(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #Initiates all pages (frames)
        for F in (StartPage, AccountPage, RegisterPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

 #Page made from inherited frame       
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the CyberATM! Please log in.").grid(row=0, column=0)

        labelUname = tk.Label(self, text="Username").grid(row=1, column=0)
        self.entry_accID = tk.Entry(self)
        self.entry_accID.grid(row=1, column=1)

        labelPwd = tk.Label(self, text="Password").grid(row=2, column=0)
        self.entry_PIN = tk.Entry(self, show="*")
        self.entry_PIN.grid(row=2, column=1)

        loginBtn = tk.Button(self, text="Sign in", command= self._login_btn_clicked).grid(row=3, column=0)

        regBtn = tk.Button(self, text="Sign up",
                            command= lambda: self.controller.show_frame(RegisterPage)).grid(row=3, column=1)

    def _login_btn_clicked(self):
        #Get input
        accID = self.entry_accID.get()
        PIN = self.entry_PIN.get()

        #Pwd check
        if accID == "test" and PIN == "0000":
            self.controller.show_frame(AccountPage)
        else:
            print("Wrong password")

class AccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome" + "Edvin")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        first_name = tk.Label(self, text= "First name").grid(row=0, column=0)
        last_name = tk.Label(self, text= "Last name").grid(row=1, column=0)
        

#Runs the main windows
root = Body()
root.mainloop()