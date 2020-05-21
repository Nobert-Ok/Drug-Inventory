#Okoye-Nobert/Joachim

#Contains the basic structure to be inherited by other child classes
#The details that are in the argument are therefore retaineed and used across classes

#This is the drug class where I assigned some attributes to it
class Drug:
    def __init__(self,drugtype,drugname,expirydate,manufacturedate,date_acquired,quantity,price):
        self.drugtype = drugtype
        self.drugname = drugname
        self.expirydate = expirydate
        self.manufacturedate = manufacturedate
        self.date_acquired = date_acquired
        self.quantity = quantity
        self.price = price

    def __str__(self):
       print("The type of drug is",self.drugtype,'and the drug name is',self.drugname,'.',
             '\nIt costs',self.price)



