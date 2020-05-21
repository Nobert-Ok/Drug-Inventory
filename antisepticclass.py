#Okoye-Nobert

from Drugclass import *

#This is the child class to Drug class
#This is the antiseptic class where I assigned some attributes to it
class Antiseptic(Drug):
   def __init__(self,drugtype,drugname,expirydate,manufacturedate,date_acquired,quantity,price,drugform,drugpurpose):
       super().__init__(drugtype,drugname,expirydate,manufacturedate,date_acquired,quantity,price)

   def __str__(self):
       print("The type of drug is", self.drugtype, 'and the drug name is', self.drugname, '.',
             '\nIt costs', self.price)

   # This is the declarative statement that prints the drug acquired in string form

   def display(self):
        print(
            "Drug Name: " + str(self.drugname) + "\nDrug Type: " + str(self.drugtype) + "\nManufacture Date: " + str(
                self.manufacturedate) +
            "\nExpiry Date: " + str(self.expirydate) + "\nNo. in Stock: " + str(
                self.quantity) + "\nPrice: " + str(self.price))
        pass

#This displays all the drug details of the drugs of concern in string form


