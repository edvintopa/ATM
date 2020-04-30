import tkinter as tk

class Body(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, AccountPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the CyberATM! Please log in.")
        label.pack(pady=10,padx=10)

        self.entry_accID = tk.Entry(self)
        self.entry_accID.pack()
        self.entry_PIN = tk.Entry(self, show="*")
        self.entry_PIN.pack()

        loginBtn = tk.Button(self, text="Login",
                            command= self._login_btn_clicked)
        loginBtn.pack()

        createAcc = tk.Button(self, text="Register new")
        createAcc.pack()

    def _login_btn_clicked(self):
        accID = self.entry_accID.get()
        PIN = self.entry_PIN.get()

        if accID == "test" and PIN == "0000":
            self.controller.show_frame(AccountPage)
        else:
            print("Wrong password")

class AccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome" + "Edvin")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

root = Body()
root.mainloop()