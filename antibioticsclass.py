#Okoye-Nobert

#This has the child class of the dug class
#contains an override of the parent class and has additional arguments in terms of drug_form looking at the form ogf the drug and woundtype
# This is the antibiotics class where I assigned some attributes to it

from Drugclass import *
import unittest



class Antibiotics(Drug):
   def __init__(self,drugtype,drugname,expirydate,manufacturedate,date_acquired,quantity,price,drugform,woundtype):
       super().__init__(drugtype,drugname,expirydate,manufacturedate,date_acquired,quantity,price)
#This is the override of the parent class
   def __str__(self):
       print("The type of drug is", self.drugtype, 'and the drug name is', self.drugname, '.',
             '\nIt costs', self.price)
#This is the declarative statement that prints the drug acquired in string form
   def display(self):
        print("Drug Name: " + str(self.drugname) + "\nDrug Type: " + str(self.drugtype) + "\nManufacture Date: " + str(
                self.manufacturedate) +
            "\nExpiry Date: " + str(self.expirydate) + "\nNo. in Stock: " + str(
                self.quantity) + "\nPrice: " + str(self.price))
        pass

