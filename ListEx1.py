Menulist = []

Total = 0
while True:
    MenuName=input("Please enter your menu : ")
    if (MenuName.lower()) =="exit":
        break
    else:
        MenuPrice = float(input("Price : "))
        Menulist.append(MenuName+" : "+str(MenuPrice)+" บาท ")
        Total = Total + MenuPrice
def showBill():
    print("-"*10+"Chom resturant"+"-"*10)
    for i in Menulist:
        print(i)
    print("ราคารวม : ", Total, " บาท")

showBill()
