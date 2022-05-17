#TODO add try/except blocks to the imports in case the user doesn't have all of the libraries installed
from ntpath import join
from os import system, name
import pandas
import add
import items


def clearScreen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def usrInp(usrInput):
        if usrInput.upper() == "I":
            voidItem()
        elif usrInput.upper() == "T":
            voidTrans()
        elif usrInput.upper() == "Q":
            yn = input("Are you sure you want to quit? Y for yes, N for no:  ")
            if yn.upper() == "Y":
                add.mydb.close()
                print("Goodbye and thanks for using Python Command Line Cash Register!")
                exit()
                
        else:
            add.get(usrInput)

def printTrans():
    df = pandas.DataFrame(items.data)
    print(df)
    print(f"\n\t\t\tTOTAL:  {df['PRICE'].sum()}")

    #old code below for formatting reference
    '''
    termsize = os.get_terminal_size().columns
    spaces = termsize - (len(glob_upc) + len(glob_item_name))
    print(glob_upc + (" " * spaces) + glob_item_name)
    '''

def voidItem():
    #TODO 1
    #TODO 3
    input("Sorry, function not implemented yet.  Press enter to continue.")

def voidTrans():
    #TODO 1
    #TODO 3
    input("Sorry, function not implemented yet.  Press enter to continue.")