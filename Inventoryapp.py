#Okoye-Nobert
from user_admin import *
from Drugclass import *
from abortionclass import *
from antibioticsclass import *
from antimalarialclass import *
from antisepticclass import *
from userclass import *


#User Login Logic
#Calls user login method from the admin class
'''
Note the password is admin123
Note the password is admin123
Note the password is admin123
Note the password is admin123
Note the password is admin123
Note the password is admin123
Note the password is admin123
Note the password is admin123
Note the password is admin123
'''
#User Login Logic
#Calls user login method from the admin class
admin1 = Admin('name','password','username', 'type','password')
admin1.user_type(type)


# this is the list of my drugs
druglist = []
drug1 = Antiseptic('Antiseptic','ACICLOVIR','12-09-2022','1-09-2022','4-09-2022',25,'$45','pill','eye_ointment')
drug2 = Antiseptic('Antiseptic','CALAMINE','23-09-2022','1-09-2022','4-09-2022',45,'$60','pill','lotion')
drug3 = Antiseptic('Antiseptic','CHLORHEXIDINE','2-09-2022','1-09-2022','4-09-2022',20,'$35','pill','lotion')
drug4 = Antiseptic('Antiseptic','ARTESUNATE','14-09-2022','1-09-2022','4-09-2022',28,'$70','pill','lotion')
drug5 = Antiseptic('Antiseptic','THIMESEROL','25-09-2022','1-09-2022','4-09-2022',50,'$4.5','pill','lotion')

# ('=====================')
# ('=====================')

drug6 = Abortion('Abortion','MISOPROSTOL','12-09-2022','1-09-2022','4-09-2022',25,'$45','pill','puncture')
drug7 = Abortion('Abortion','CYTOTEC','23-09-2022','1-09-2022','4-09-2022',45,'$60','pill','tetanus')
drug8 = Abortion('Abortion','OXYTOCIN','2-09-2022','1-09-2022','4-09-2022',20,'$35','pill','avulsion')
drug9 = Abortion('Abortion','PITOCIN','14-09-2022','1-09-2022','4-09-2022',28,'$70','pill','laceration')
drug10 = Abortion('Abortion','MIFEPREX','25-09-2022','1-09-2022','4-09-2022',50,'$4.5','pill','abrasion')

# ('=====================')
# ('=====================')

drug11 = Antibiotics('Antibiotics','AMOXICILLIN','12-09-2022','1-09-2022','4-09-2022',25,'$45','pill','16')
drug12 = Antibiotics('Antibiotics','DOXYCYCLINE','23-09-2022','1-09-2022','4-09-2022',45,'$60','pill','18')
drug13 = Antibiotics('Antibiotics','CEPHALEXIN','2-09-2022','1-09-2022','4-09-2022',20,'$35','pill','17')
drug14 = Antibiotics('Antibiotics','CLINDAMYCIN','14-09-2022','1-09-2022','4-09-2022',28,'$70','pill','18')
drug15 = Antibiotics('Antibiotics','CIPROFLAXIN','25-09-2022','1-09-2022','4-09-2022',50,'$4.5','pill','18')

print('=====================')
print('=====================')

drug16 = Antimalarial('Antimalarial','QUININE','12-09-2022','1-09-2022','4-09-2022',25,'$45','pill','16')
drug17 = Antimalarial('Antimalarial','CHLOROQUINE','23-09-2022','1-09-2022','4-09-2022',45,'$60','pill','18')
drug18 = Antimalarial('Antimalarial','HALOFANTRINE','2-09-2022','1-09-2022','4-09-2022',20,'$35','pill','17')
drug19 = Antimalarial('Antimalarial','ARTESUNATE','14-09-2022','1-09-2022','4-09-2022',28,'$70','pill','18')
drug20 = Antimalarial('Antimalarial','MEFLOQUINE','25-09-2022','1-09-2022','4-09-2022',50,'$4.5','pill','18')

druglist.append(drug1)
druglist.append(drug2)
druglist.append(drug3)
druglist.append(drug4)
druglist.append(drug5)
druglist.append(drug6)
druglist.append(drug7)
druglist.append(drug8)
druglist.append(drug9)
druglist.append(drug10)
druglist.append(drug11)
druglist.append(drug12)
druglist.append(drug13)
druglist.append(drug14)
druglist.append(drug15)
druglist.append(drug16)
druglist.append(drug17)
druglist.append(drug18)
druglist.append(drug19)
druglist.append(drug20)

admin1.list(druglist)

# this is my while loop for my whole program. It enables the user do more functions
answer = "yes"
while answer == "yes":
    admin1.options2()
    try:
        options_number2 = int(input("Enter your choice here:"))
        if options_number2 == 1:
            admin1.view(druglist)
        # return the view drugs option


        # allow admin to add drugs
        elif options_number2 == 2:
            admin1.add(druglist)

        # allow admin to delete drugs
        elif options_number2 == 3:
            admin1.deletedrug(druglist)

        # allow admin to check price of  drugs
        elif options_number2 == 4:
            admin1.price(druglist)


        # allow admin to show quantity drugs
        elif options_number2 == 5:
            admin1.quantity(druglist)
    except ValueError:
        print('Please enter a valid character(number)!')

    else:
            print('')
        # rerun the options method
    answer = input("Do you want to do anything else?yes or no:\n ").lower()


