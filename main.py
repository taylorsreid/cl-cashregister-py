#ITOEN GREEN TEA UPC FOR TESTING: 073366118238

import crfunc #my functions file
import os
mastercontrolbool = True #master control whether to continue looping or not
version = "alpha"

crfunc.clear_screen()
print(f"Hello and welcome to the Python Command Line Cash Register, version {version}")

with open('current_transaction.csv','w') as f:
    f.write("UPC, NAME, PRICE\n")

i = 0
while mastercontrolbool == True:
    print("Scan a UPC to add an item | Void (I)tem | Void (T)ransaction | (Q)uit \n")
    if i > 0: crfunc.print_trans()
    print()
    crfunc.usr_inp(input("Input:  "))
    crfunc.clear_screen()
    i+=1