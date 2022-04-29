#ITOEN GREEN TEA UPC FOR TESTING: 073366118238

'''
TODO 1 When voiding, it prints and empty data frame.  Fix that so it doesn't.
TODO 2 Clean up the printing of the total line, the current formatting is sloppy.
TODO 3 Add an actual void function.
TODO 4 Add error handling for price input.
TODO 5 defunctionalize many of the variables and use global variables instead, this is too confusing.
TODO 6 adding 4987176077271 then 073366118238 and setting a price of 1 sets the price of 073366118238 to NaN
'''

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

os.system("pause")