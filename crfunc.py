from ntpath import join
import os
import requests
from os import system, name

#VARIABLE DEFINITIONS
upc = ""
itemname = ""
allitems = {} #DICTIONARY OF DICTIONARIES TO STORE ALL ITEMS IN THE TRANSACTION???
'''
format for allitems:
{
    "upc1" : {
        "item1name" : ""
        "price" : 13.99
    }
    "upc2" : {
        "item2name" : ""
        "price" : 69.99
    }
}
etc
'''

def clearscreen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def usrinp():
    print("Scan a UPC to add an item | Void (I)tem | Void (T)ransaction | (Q)uit")
    selection = input()
    match selection:
        case "i":
            voiditem()
        case "t":
            voidtrans()
        case "q":
            yn = input("Are you sure you want to quit? Y for yes, N for no")
            if yn.lower() == "y":
                print("Goodbye and thanks for using Python Command Line Cash Register!")
                exit()
                os.system("pause")
        case _ :
            additem(selection)

def additem(selection):
    #ADD METHOD TO ADD AN ITEM TO THE DICTIONARY OF CURRENT ITEMS IN THE TRANSACTION
    #STORE DICTIONARY IN A JSON FILE SO THAT ITEMS NOT FOUND IN THE API CAN BE DEFINED AND REMEMBERED FOR A LATER DATE
    #AND SO THAT THE API ISN'T OVERUSED
    #MIGRATE TO AN SQL DATABASE LATER

    global itemname, upc

    response = requests.request("GET", f"https://barcode.monster/api/{selection}").json()
    tempitemname = list(response["description"]) #puts the item name into a list so it can be modified

    #23 chars to remove the "(from barcode.monster)" blah blah blah
    i = -23
    while i < 0:
        del tempitemname[i]
        i += 1

    #makes the itemname list back into a string
    itemname = ''.join(tempitemname)
    upc = selection

def printtrans(): #PRINTS THE TRANSACTION TO THE SCREEN
    termsize = os.get_terminal_size().columns
    spaces = termsize - (len(upc) + len(itemname))
    print(upc + (" " * spaces) + itemname)

def voiditem():
    #ADD METHOD TO REMOVE AN ITEM FROM THE DICTIONARY OF CURRENT ITEMS IN THE TRANSACTION
    pass

def voidtrans():
    #ADD METHOD TO CLEAR DICTIONARY AND START OVER
    pass