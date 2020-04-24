class Account:

    #Constructor
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._balance = 0
        self._history = []

    #Getters
    def get_first_name(self):
        return self._first_name
    def get_last_name(self):
        return self._last_name
    def get_balance(self):
        return self._balance
    def get_history(self):
        #fix
    
    #Setters
    def set_first_name(self, x):
        self._first_name = x
    def set_last_name(self, x):
        self._last_name = x
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount