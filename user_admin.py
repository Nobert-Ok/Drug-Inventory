#Okoye-Nobert/Joachim

from userclass import *
from Drugclass import *
from user_admin import *
from Drugclass import *
from abortionclass import *
from antibioticsclass import *
from antimalarialclass import *
from antisepticclass import *
from userclass import *
#this is the admin class
class Admin(User):

    def __init__(self, fullname,email,username,type, password):
        super().__init__(fullname,email,username,password)

    def __str__(self):
        print("You're",self.fullname,'and your password is',self.password )

# this is the user type function
# When a user inputs an invalid car that is not on the list the while loop comes in to play and thats because
# the user inputs an non integer the code exists or crashes making me have some set examples
    def user_type(self,type):
        name = input('Please enter a login name?')
        print('Welcome', name,'\nYour password is admin123')


        #open Admin user class
        # input a valid argument here
        password = 'admin123'
        user_password = input('Please enter your admin password:')
        if user_password == password:
            self.type = "Admin"
            print('You are an Admin')
            f = open(name, 'a')
            f.write(name)
            f.write('\nThis file contains the record of the activities you would be doing on this inventory')
            f.write('\nFeel free to make all enquiries you need.')
            f.close()
            f = open(name, 'a')
            f.write('\nUser has logged into the Inventory app as the admin')
            f.close()
            f = open(name, 'a')
            f.write('\nThe password entered is valid and the user can proceed with the program')
            f.close()

        elif user_password != password:
            print('Wrong Password! Try Again')
            f = open(name, 'a')
            f.write('\nThe password entered is invalid and the user is exited from the program')
            f.close()
            exit()


    # this is the function function that takes in a list
    def list(self,druglist):
        for ye in druglist:
            print(ye.drugtype,':-',ye.drugname)

    def add(self,druglist):
        name = input('What is your login name?')
        print("To add an antibiotics drug press 1\n"
              "To add an antiseptic drug press 2\n"
              "To add an antimalarial drug press 3\n"
              "To add an abortion drug press 4\n")
        decide = int(input('Enter your choice here:'))
        f = open(name, 'a')
        f.write('\nThe user has chosen the option to add more drugs to the inventory')
        f.close()

        if decide == 1:
            drugtype = "Antibiotics"
            print('Please input the following info for storage.')
            drugname = input("Name of drug e.g(ACICLOVIR):").upper()
            expirydate = input('Expiry date(DD-MM-YYYY):')
            manufacturedate = input('Manufactured date(DD-MM-YYYY):')
            date_acquired = input('Date of acquiry(DD-MM-YYYY):')
            quantity = int(input("What is the quantity of the drug acquire:"))
            price = int(input('What is the price tag:'))
            drugform = input('What form is the drug(e.g pill/syrup):')
            woundtype = input('What type of wound is this used for:')
            newdrug = Antibiotics(drugtype, drugname, expirydate, manufacturedate, date_acquired,
                                  quantity, price, drugform, woundtype)

            print('Your new drug is:', newdrug.drugname)
            druglist.append(newdrug)
            f = open(name, 'a')
            f.write('\nThe user just added an antibiotics to the inventory')
            f.write('\nAdding an antibiotics was successful')
            f.close()

        elif decide == 2:
            drugtype = "Antimalarial"
            print('Please input the following info for storage.')
            drugname = input("Name of drug e.g(QUININE):").upper()
            expirydate = input('Expiry date(DD-MM-YYYY):')
            manufacturedate = input('Manufactured date(DD-MM-YYYY):')
            date_acquired = input('Date of acquiry(DD-MM-YYYY):')
            quantity = int(input("What is the quantity of the drug acquire:"))
            price = int(input('What is the price tag:'))
            drugform = input('What form is the drug(e.g pill/syrup):')
            bloodtype = input('What is the blood type of the user:')
            newdrug = Antimalarial(drugtype, drugname, expirydate, manufacturedate, date_acquired,
                                   quantity, price, drugform, bloodtype)

            print('Your new drug is:', newdrug.drugname)
            druglist.append(newdrug)
            f = open(name, 'a')
            f.write('\nThe user just added an antimalarial drug to the inventory')
            f.write('\nAdding an antimalarial was successful')
            f.close()

        elif decide == 3:
            drugtype = "Antiseptic"
            print('Please input the following info for storage.')
            drugname = input("Name of drug e.g(CALAMINE):").upper()
            expirydate = input('Expiry date(DD-MM-YYYY):')
            manufacturedate = input('Manufactured date(DD-MM-YYYY):')
            date_acquired = input('Date of acquiry(DD-MM-YYYY):')
            quantity = int(input("What is the quantity of the drug acquire:"))
            price = int(input('What is the price tag:'))
            drugform = input('What form is the drug(e.g pill/syrup)')
            drugpurpose = input('What would this drug be used for(eg lotion,cleaning, etc)')
            newdrug = Antiseptic(drugtype, drugname, expirydate, manufacturedate, date_acquired,
                                 quantity, price, drugform, drugpurpose)

            print('Your new drug is:', newdrug.drugname)
            druglist.append(newdrug)
            f = open(name, 'a')
            f.write('\nThe user just added an antiseptic to the inventory')
            f.write('\nAdding an antiseptic was successful')

            f.close()

        elif decide == 4:
            drugtype = "Abortion"
            print('Please input the following info for storage.')
            drugname = input("Name of drug e.g(OXYTOCIN):").upper()
            expirydate = input('Expiry date(DD-MM-YYYY):')
            manufacturedate = input('Manufactured date(DD-MM-YYYY):')
            date_acquired = input('Date of acquiry(DD-MM-YYYY):')
            quantity = int(input("What is the quantity of the drug acquire:"))
            price = int(input('What is the price tag:'))
            drugform = input('What form is the drug(e.g pill/syrup)')
            agelimit = int(input('What age is the user of the drug'))
            newdrug = Abortion(drugtype, drugname, expirydate, manufacturedate, date_acquired,
                               quantity, price, drugform, agelimit)

            print('Your new drug is:', newdrug.drugname)
            druglist.append(newdrug)
            f = open(name, 'a')
            f.write('\nThe user just added an abortion drug to the inventory')
            f.write('\nAdding an abortion drug was successful')
            f.close()
        else:
            print("Please enter a valid number")

    # this is the view function
    # When a user inputs an invalid car that is not on the list the while loop comes in to play and thats because
    # the user inputs an non integer the code exists or crashes making me have some set examples
    def view(self,druglist):
        name = input('What is your login name?')
        # For loop to iterate printing of all drugs in the list
        for drug in range(0, len(druglist)):
            print("________________")

            print("Drug " + str(drug + 1))
            print()
            druglist[drug].display()
            print("\n")
        f = open(name , 'a')
        f.write('\nThe user has chosen the option to view drugs in the inventory \nThe drug view was successful!!')
        f.close()

    # this is the delete function
    # When a user inputs an invalid car that is not on the list the while loop comes in to play and thats because
    # the user inputs an non integer the code exists or crashes making me have some set examples
    def deletedrug(self,druglist):
        name = input('What is your login name?')
        info = input('What drug do you want to remove? e.g(CIPROFLAXIN)').upper()
        len_list = len(druglist)
        count = 1
        for ye in druglist:
            if ye.drugname == info:
                druglist.remove(ye)
                print(ye.drugname + ' has been deleted')
                f = open(name, 'a')
                f.write(
                    '\nThe user has chosen the option to delete drugs from the inventory \nDrug deletion was successful!!')
                f.close()
                break
            elif count >= len_list:
                print('The drug you inputted doesn\'t exist')
                f = open(name, 'a')
                f.write(
                    '\nThe user has chosen the option to delete drugs from the inventory \nDrug deletion was not successful!!')
                f.close()
            count += 1

    # this is the pricing function
    # When a user inputs an invalid drug that is not on the list the while loop comes in to play and thats because
    # the user inputs an non integer the code exists or crashes making me have some set examples
    def price(self,druglist):
        name = input('What is your login name?')
        info = input("Which drug do you want to view its pricing? e.g(MEFLOQUINE)").upper()
        len_list = len(druglist)
        count = 1
        for ye in druglist:
            if ye.drugname == info:
                print(ye.drugname + " is worth", str(ye.price))
                break
            elif count >= len_list:
                print('The drug you inputted doesn\'t exist')
                f = open(name, 'a')
                f.write(
                    '\nThe user has chosen the option to delete drugs from the inventory \nDrug deletion was not successful!!')
                f.close()
            count += 1
        f = open(name, 'a')
        f.write('\nThe user has chosen the option to check the price of drugs in the inventory \nPrice checking was successful!!')
        f.close()

    # this is the quantity check function
    # When a user inputs an invalid car that is not on the list the while loop comes in to play and thats because
    # the user inputs an non integer the code exists or crashes making me have some set examples
    def quantity(self,druglist):
        name = input('What is your login name?')

        info = input("Which drug do you want to view its quantity? e.g(MEFLOQUINE)").upper()
        len_list = len(druglist)
        count = 1
        for ye in druglist:
            if ye.drugname == info:
                print(ye.drugname, 'is', str(ye.quantity), " in stock")
                f = open(name, 'a')
                f.write(
                    '\nThe user has chosen the option to check the quantity of drugs in the inventory \nQuantity Check was successful')
                f.close()
            elif count >= len_list:
                print('The drug you inputted doesn\'t exist')
                f = open(name, 'a')
                f.write(
                    '\nThe user has chosen the option to delete drugs from the inventory \nDrug deletion was not successful!!')
                f.close()
            count += 1



    # this is the option function
    # When a user inputs an invalid car that is not on the list the while loop comes in to play and thats because
    # the user inputs an non integer the code exists or crashes making me have some set examples
    def options2(self):
        print('______________________________')
        print('\nWelcome to Soulful Pharmacy\n')
        print('\n_____________________________\n')
        print("To view drugs. Press 1. \n"
              "To add a drug. Press 2. \n"
              "To remove a drug. Press 3 \n"
              "To check prices. Press 4. \n"
              "To show quantity of drug. Press 5 \n"
              )


