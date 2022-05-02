from ntpath import join
import time
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
        if usr_inp_selection.upper() == "I":
            void_item()
        elif usr_inp_selection.upper() == "T":
            void_trans()
        elif usr_inp_selection.upper() == "Q":
            yn = input("Are you sure you want to quit? Y for yes, N for no:  ")
            if yn.upper() == "Y":
                print("Goodbye and thanks for using Python Command Line Cash Register!")
                time.sleep(3)
                exit()
                
        else:
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
    add_item_price = float(input(f"Please input a price for {add_item_name}:  "))

    with open('current_transaction.csv','a') as f:
        f.write(f"{add_item_selection}, {add_item_name}, {add_item_price}\n")

def print_trans(): #PRINTS THE TRANSACTION TO THE SCREEN
    df = pandas.read_csv('current_transaction.csv', sep=r'\s*,\s*', engine='python')
    
    print(df)
    #TODO 2
    print("\n                            TOTAL " + str(df['PRICE'].sum()))
     #old code below for formatting reference
    '''
    termsize = os.get_terminal_size().columns
    spaces = termsize - (len(glob_upc) + len(glob_item_name))
    print(glob_upc + (" " * spaces) + glob_item_name)
    '''

def void_item():
    #TODO 1
    #TODO 3
    input("Sorry, function not implemented yet.  Press enter to continue.")

def void_trans():
    #TODO 1
    #TODO 3
    input("Sorry, function not implemented yet.  Press enter to continue.")