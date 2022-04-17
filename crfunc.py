from ntpath import join
import os
import requests
from os import system, name
import pandas

def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def usr_inp(usr_inp_selection):
    match usr_inp_selection:
        case "i":
            void_item()
        case "t":
            void_trans()
        case "q":
            yn = input("Are you sure you want to quit? Y for yes, N for no:  ")
            if yn.lower() == "y":
                print("Goodbye and thanks for using Python Command Line Cash Register!")
                exit()
                os.system("pause")
        case _ :
            add_item(usr_inp_selection)

def add_item(add_item_selection):
    try:
        response = requests.request("GET", f"https://barcode.monster/api/{add_item_selection}").json()
        add_item_name = list(response["description"]) #puts the item name into a list so it can be modified

        #23 chars to remove the "(from barcode.monster)" blah blah blah
        i = -23
        while i < 0:
            del add_item_name[i]
            i += 1

        #makes the itemname list back into a string
        add_item_name = ''.join(add_item_name)
    
    except:
        add_item_name = input("Sorry, item not found, give it a name:  ")

    #glob_upc = add_item_selection

    #TEMPORARY
    add_item_price = float(input("Please input a price for that item:  "))

    with open('current_transaction.csv','a') as f:
        f.write(f"{add_item_selection}, {add_item_name}, {add_item_price}\n")

def print_trans(): #PRINTS THE TRANSACTION TO THE SCREEN
    print(pandas.read_csv('current_transaction.csv'))
     
     #TODO old code below for formatting reference
    '''
    termsize = os.get_terminal_size().columns
    spaces = termsize - (len(glob_upc) + len(glob_item_name))
    print(glob_upc + (" " * spaces) + glob_item_name)
    '''

def void_item():
    #ADD METHOD TO REMOVE AN ITEM FROM THE DICTIONARY OF CURRENT ITEMS IN THE TRANSACTION
    print("Sorry, function not implemented yet.")
    pass

def void_trans():
    #ADD METHOD TO CLEAR DICTIONARY AND START OVER
    print("Sorry, function not implemented yet.")
    pass