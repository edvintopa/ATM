import tkinter as tk

class Page(tk.Frame):
    def __init(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class LoginScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, *kwargs)
        
        label = tk.Label(self, text="Welcome to the CyberATM!")
        label.pack(side="top", fill="both", expand=True)

        button = tk.Button(self, text="Test")
        button.pack(side="top")

class AccountScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, *kwargs)
        
        label = tk.Label(self, text="Test successful")
        label.pack(side="top", fill="both", expand=True)

class Body(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = LoginScreen(self)
        p2 = AccountScreen(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        p1.show()

    def displayPage(self, ):
        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = Body(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()