database = dict()

database["daniel"] = "password123"
def login(u_name, p_word):
    if u_name in database.keys():
        password = database.get(u_name)
        if password == None or password != p_word:
            print("Invalid password")
        else:
            print("Logged in Successfully")
    else:
        print("Invalid username or password") 


def signup(u_name, p_word, p_word2):
    pass

