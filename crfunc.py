from ntpath import join
import os
import requests
from os import system, name

#CLEAN UP THESE GLOBAL VARIABLES, THIS SHIT IS SPAGHETTI CODE
#VARIABLE DEFINITIONS
glob_upc = ""
glob_item_name = ""
'''
format for currenttransaction.json:
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

def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def usr_inp():
    print("Scan a UPC to add an item | Void (I)tem | Void (T)ransaction | (Q)uit")
    usr_inp_selection = input()
    match usr_inp_selection:
        case "i":
            void_item()
        case "t":
            void_trans()
        case "q":
            yn = input("Are you sure you want to quit? Y for yes, N for no")
            if yn.lower() == "y":
                print("Goodbye and thanks for using Python Command Line Cash Register!")
                exit()
                os.system("pause")
        case _ :
            add_item(usr_inp_selection)

def add_item(add_item_selection):
    global glob_item_name, glob_upc

    response = requests.request("GET", f"https://barcode.monster/api/{add_item_selection}").json()
    add_item_name = list(response["description"]) #puts the item name into a list so it can be modified

    #23 chars to remove the "(from barcode.monster)" blah blah blah
    i = -23
    while i < 0:
        del add_item_name[i]
        i += 1

    #makes the itemname list back into a string
    glob_item_name = ''.join(add_item_name)
    glob_upc = add_item_selection

    #TEMPORARY
    add_item_price = float(item_price())

    add_del(True, add_item_selection, add_item_name, add_item_price)

def item_price():
    price = input("Please input a price for that item:  ")
    return price

#CSV IS WRITING ITEM NAMES AS LISTS INSTEAD OF STRINGS, FIX PLEASE
def add_del(add_del_bool, add_del_upc, add_del_itemname, add_del_price):
    #going to use CSV for now then migrate to SQL
    if add_del_bool == True: #yes I know == is unecessary but it makes it more readable
        
        with open('current_transaction.csv','a') as f:
            f.write(f"{add_del_upc}, {add_del_itemname}, {add_del_price}\n")
    if add_del_bool == False:
        pass #ADD IN THE DELETION CODE

def print_trans(): #PRINTS THE TRANSACTION TO THE SCREEN
    termsize = os.get_terminal_size().columns
    spaces = termsize - (len(glob_upc) + len(glob_item_name))
    print(glob_upc + (" " * spaces) + glob_item_name)

def void_item():
    #ADD METHOD TO REMOVE AN ITEM FROM THE DICTIONARY OF CURRENT ITEMS IN THE TRANSACTION
    pass

def void_trans():
    #ADD METHOD TO CLEAR DICTIONARY AND START OVER
    pass