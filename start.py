import crfunc
mastercontrolbool = True #master control whether to continue looping or not

crfunc.clearscreen()
print("Hello and welcome to the Python Command Line Cash Register")

while mastercontrolbool == True:

    crfunc.additem()

    runagain = input("Would you like to do another item?  y for yes, n for no:  ")
    if runagain.lower() != "y":
        mastercontrolbool = False
    #else: pass #clearscreen()

#os.system("pause") #stops the program from ending immediately after the last action