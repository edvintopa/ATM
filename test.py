PASSWORD_FNAME = "User_Data.txt"

def get_existing_users():
    with open("r", PASSWORD_FNAME ) as fp:
         for line in fp.readlines():
             # This expects each line of a file to be (name, pass) seperated by whitespace
             username, password = line.split()
             yield username, password

def is_authorized(username, password):
    return any((user == (username, password) for user in get_existing_users()) 

def ask_user_credentials():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    return name, password

def checkdetails():
    name, password = ask_user_credentials()
    if is_authorized(name, password):
       return "Welcome Back, " + name
    if user_exists(name):
       return "Password entered is wrong"
    return "Name not found. Please Sign Up."

def getdetails():
    name, password = ask_user_credentials()
    if not user_exists(name):
       return "Name Unavailable. Please Try Again"
    # Not sure tho what would You like to do here