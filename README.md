# Drug-Inventory
I installed pyside2 at the beginning of the program. For the testing we used the unittest. In order words, we imported unittest to test the different classes and its scenario

Note*** The admin has a default password of admin123 and it cannot be changed

What does the programme do- This is a drug inventory app that allows the user in this case a buyer or admin(super user) to access the stock of drugs available and to influence them by buying, selling, adding and deleting them.

modules used

Abortion- Contains all the procedures for the abortion drugs Antibiotics-Contains all the procedures for the antibiotic drugs User-Contains all the procedures the User can influence on all the drugs Antiseptic-Contains all the procedures for the antiseptic drugs Antimalarial-Contains all the procedures for the antimalarial drugs Drug-Contains the basic procedures for all the drugs function-Contains the kuser functions Inventory-Contains all the procedures for the inventory

class Parent classes User Drugs

Child classes Antibiotics Antimalarial Abortion Antiseptic

The program allows the user to : Add drugs Remove drugs Check the expiry date of drugs Check the Manufacturing date Check prices of drugs to be given to the patient Show the number of drugs View type of drugs available

Basic Pseudocode To view Drugs: The list is looped through The drug names are shown for the owner to use

To add Drugs: Show drugs available Owner chooses type of drug to be added If he chooses type of drug, then, Questions are asked under the types of drugs eg(type of drug, name of drug to be added, the expiry date, the manufactured date, date of acquire, quantity available, etc ) Owner inputs his answers These inputs are given variables and the variables are added to the list Shows the owner the new list

To remove drugs: Show the drugs available Owner chooses drug name to be removed The drugs are then removed from the list

Check the expiry date of drugs: Shows drugs available Owner chooses drug name The expiry date of the drug is shown

Check the Manufacturing date: Shows drugs available Owner chooses drug name The manufactured date of the drug is shown
