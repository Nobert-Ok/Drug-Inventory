#Okoye-Nobert

from Drugclass import *

#Contains the child class of the  Drug class
#This is the abortion class where I assigned some attributes to it
class Abortion(Drug):
   def __init__(self,drugtype,drugname,expirydate,manufacturedate,date_acquired,quantity,price,drugform,age_limit):
       super().__init__(drugtype,drugname,expirydate,manufacturedate,date_acquired,quantity,price)
#This will declare the drug being used in terms of string
   def __str__(self):
       print("The type of drug is",self.drugtype,'and the drug name is',self.drugname,'.',
             '\nIt costs',self.price)
#This dislays all the abortio drugs available for purschase and ssale by both the buyer and admin
   def display(self):
        print(
            "Drug Name: " + str(self.drugname) + "\nDrug Type: " + str(self.drugtype) + "\nManufacture Date: " + str(
                self.manufacturedate) +
            "\nExpiry Date: " + str(self.expirydate) + "\nNo. in Stock: " + str(
                self.quantity) + "\nPrice: " + str(self.price))
        pass
