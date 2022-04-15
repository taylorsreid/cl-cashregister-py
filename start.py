#ITOEN GREEN TEA UPC FOR TESTING: 073366118238

import crfunc #my functions file
import os
mastercontrolbool = True #master control whether to continue looping or not
version = "alpha"

crfunc.clearscreen()
print(f"Hello and welcome to the Python Command Line Cash Register")
print(f"Version {version}")

while mastercontrolbool == True:

    crfunc.usrinp()
    crfunc.clearscreen()
    crfunc.printtrans()
