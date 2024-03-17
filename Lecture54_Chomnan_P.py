def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print("Username or Password incorrect")
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("Total price include vat 7% :",vatCalculator(priceCalculator()),"TH")
    elif userSelected ==2:
        print("Total price :", priceCalculator(),"TH")
    else:
        print("Out of menu selection")
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    result2 = totalPrice * vat / 100
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1+price2
    return totalPrice

login()