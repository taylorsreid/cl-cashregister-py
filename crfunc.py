#TODO add try/except blocks to the imports in case the user doesn't have all of the libraries installed
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
            yn = input("Are you sure you want to quit? [y/n]:  ")
            if yn.upper() == "Y":
                add.mydb.close()
                print("Goodbye and thanks for using Python Command Line Cash Register!")
                exit()
                
        else:
            add.get(usrInput)

def printTrans():
    df = pandas.DataFrame(items.data)
    if df.empty == False:
        print(df)
        print(f"\n\t\t\tTOTAL:  ${round(df['PRICE'].sum(), 2)}")
    else:
        pass

    #old code below for formatting reference
    '''
    termsize = os.get_terminal_size().columns
    spaces = termsize - (len(glob_upc) + len(glob_item_name))
    print(glob_upc + (" " * spaces) + glob_item_name)
    '''

def voidItem():
    selection = input("Line number to remove:  ")
    #if selection.isnumeric():
    try:
        del items.data["UPC"][int(selection)]
        del items.data["NAME"][int(selection)]
        del items.data["PRICE"][int(selection)]
    except:
        print("Not a valid line number.  Try again.")
        voidItem()

def voidTrans():
    yn = input(f"Are you sure you wish to void the ENTIRE transaction?  [y/n]:  ")
    if yn.lower() == "y":
        del items.data["UPC"][0:]
        del items.data["NAME"][0:]
        del items.data["PRICE"][0:]