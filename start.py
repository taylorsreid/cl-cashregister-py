import crfunc #my functions file
import os
mastercontrolbool = True #master control whether to continue looping or not

crfunc.clearscreen()
print("Hello and welcome to the Python Command Line Cash Register")

while mastercontrolbool == True:

    crfunc.additem()
    crfunc.printtrans()

    runagain = input("Would you like to do another item?  y for yes, n for no:  ")
    if runagain.lower() != "y":
        mastercontrolbool = False
    else:
        crfunc.clearscreen()
        print("GOODBYE!")
        os.system("pause") #stops the program from ending immediately after the last action