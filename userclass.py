#Edward
#this is the user parent class
class User:
    def __init__(self,fullname,email,username,password):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        print("You're",self.fullname,'and your email is',self.email )