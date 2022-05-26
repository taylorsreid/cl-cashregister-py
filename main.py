#ITOEN GREEN TEA UPC FOR TESTING: 073366118238
#Grenade Chews - Lychee for testing: 691683000243

'''
TODO 4 Add error handling for price input.
'''

#import crfunc #my functions file
import crfunc

#global variables
mastercontrolbool = True #master control whether to continue looping or not
version = "MySQL alpha"

#things that only run once
#crfunc.clearScreen()
print(f"Hello and welcome to the Python Command Line Cash Register, version {version}")


#things that loop
i = 0
while mastercontrolbool == True:
    crfunc.clearScreen()
    print("Scan a UPC to add an item | Void (I)tem | Void (T)ransaction | (Q)uit \n")
    if i > 0: crfunc.printTrans()
    print()
    crfunc.usrInp(input("Input:  "))
    crfunc.printTrans()
    crfunc.clearScreen()
    i+=1