import mysql.connector
import requests
import items
import time

def addPriceManually():
    price = input("PRICE:  ")
    #tries converting the number to a float, and if it can't (meaning it's not a number), then it runs again.
    try:
        float(price)
        return price
    except:
        return addPriceManually()

#sets the item
def setItem(upc, name, price):
    items.data["UPC"].append(upc)
    items.data["NAME"].append(name)
    items.data["PRICE"].append(float(price))

def addItemManually(usrInput):
    print(f"{usrInput} wasn't found in the SQL database or on Barcode Monster.  Enter it manually")
    name = input("NAME:  ")
    price = addPriceManually()
    setItem(usrInput, name, price)

def addItemFromBM(usrInput):
    try:
        response = requests.request("GET", f"https://barcode.monster/api/{usrInput}").json()
        name = list(response["description"]) #puts the item name into a list so it can be modified

        #23 chars to remove the "(from barcode.monster)" blah blah blah
        i = -23
        while i < 0:
            del name[i]
            i += 1

        #makes the itemname list back into a string
        name = ''.join(name)
        
        yn = input(f"Found on barcode.monster.  Does {name} look correct?  [y/n]:  ")
        if yn.lower() == "y":
            setItem(usrInput, name, addPriceManually())
        else:
            addItemManually(usrInput)
    except:
        addItemManually(usrInput)

def get(usrInput):
    sql = f"SELECT * FROM items WHERE upc ='{usrInput}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall() #myresult is a list type

    #try to connect to MySQL
    #empty lists return false when evaluated in python so the following code will only run if the list is not empty aka not in the MySQL database
    if myresult:
        setItem(myresult[0][0], myresult[0][1], myresult[0][2])
    else:
        addItemFromBM(usrInput)

#STEP 1 - ALWAYS EXECUTES
try:
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "public",
            password = "",
            database = "pos"
        )

    #cursor object declaration
    mycursor = mydb.cursor()
    print("Successfully connected to MySQL database...")
    time.sleep(1.5)
except:
    print("Error connecting to MySQL!  The application will fall back to using the barcode.monster API")
    time.sleep(3)