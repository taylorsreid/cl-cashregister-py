from ntpath import join
import requests
from os import system, name

#VARIABLE DEFINITIONS
mastercontrolbool = True #DETERMINES WHETHER TO CONTINUE LOOPING
allitems = {} #DICTIONARY OF DICTIONARIES TO STORE ALL ITEMS IN THE TRANSACTION???


def clearscreen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def printtrans():
    #ADD METHOD TO PRINT THE WHOLE TRANSACTION TO THE SCREEN HERE?  PASS IS A PLACEHOLDER, USE THE DICTIONARY TO PRINT
    pass

def additem():
    #ADD METHOD TO ADD AN ITEM TO THE DICTIONARY OF CURRENT ITEMS IN THE TRANSACTION
    #STORE DICTIONARY IN A JSON FILE SO THAT ITEMS NOT FOUND IN THE API CAN BE DEFINED AND REMEMBERED FOR A LATER DATE
    #AND SO THAT THE API ISN'T OVERUSED
    #MIGRATE TO AN SQL DATABASE LATER
    pass

def removeitem():
    #ADD METHOD TO REMOVE AN ITEM FROM THE DICTIONARY OF CURRENT ITEMS IN THE TRANSACTION
    pass

while mastercontrolbool == True:

    #ITOEN GREEN TEA UPC FOR TESTING: 073366118238

    UPC = input("Please input a UPC:  ")
    response = requests.request("GET", f"https://barcode.monster/api/{UPC}").json()
    itemname = list(response["description"]) #puts the item name into a list so it can be modified

    #23 chars to remove the "(from barcode.monster)" blah blah blah
    i = -23
    while i < 0:
        del itemname[i]
        i += 1

    #makes the itemname list back into a string
    itemname = ''.join(itemname)
    print(itemname)

    runagain = input("Would you like to do another item?  y for yes, n for no:  ")
    if runagain.lower() != "y":
        mastercontrolbool = False
    else: clearscreen()

#os.system("pause") #stops the program from ending immediately after the last action