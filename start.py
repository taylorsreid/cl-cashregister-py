#ITOEN GREEN TEA UPC FOR TESTING: 073366118238

import crfunc #my functions file
import os
mastercontrolbool = True #master control whether to continue looping or not
version = "alpha"

crfunc.clear_screen()
print(f"Hello and welcome to the Python Command Line Cash Register")
print(f"Version {version}")

with open('current_transaction.csv','w') as f:
    f.write("UPC, NAME, PRICE\n")

while mastercontrolbool == True:

    crfunc.usr_inp()
    crfunc.clear_screen()
    crfunc.print_trans()
