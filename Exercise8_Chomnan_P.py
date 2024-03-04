print("----CHO store----")
Username = input("Username : ")
Password = input("Password : ")
U_VIP = "VIP159"
U_Normal = "Member459"
P_VIP = "159"
P_Normal = "459"
PassVIP = "CorrectVIP"
Pass2 = "Correct"
PriceNewjeans = 24
ItemNewjeans = "1"
PriceRedvelet = 21
ItemRedvelet = "2"
PriceAespa = 22
ItemAespa = "3"
PriceLe_sserafim = 24
ItemLe_sserafim="4"
PriceIdie = 22
ItemIdie="5"
if Username==U_VIP and Password==P_VIP:
    print("Welcome our VIP member")
    Discount = 0.05 # discount 5 % and free shipping
    ID = "VIP"
elif Username ==U_Normal and Password==P_Normal:
    print("Welcome our member")
    Shipping = 1.5 #$
    ID = "Normal"
else:
    print("ID or pass incorrect sign in again")
    ID="Incorrect"
if ID == "VIP" or ID == "Normal" :
    print("List of products")
    print("1) NewJeans, 2nd EP 'Get Up' :", PriceNewjeans,"$")
    print("2) Red Velvet, The 3rd album 'Chill Kill' :", PriceRedvelet,"$")
    print("3) Aespa, The 3rd mini album 'MY World' :", PriceAespa,"$")
    print("4) Le sserafim, 3rd mini album 'Easy' :", PriceLe_sserafim,"$")
    print("5) (G)I-DLE, The 2nd album 'Regular' :", PriceIdie,"$")
    Item = input("Select item >> ")
    Number = int(input("The number of items >> "))
    if Item == "1" :
            ItemPrice = PriceNewjeans
    elif Item =="2" :
            ItemPrice = PriceRedvelet
    elif Item == "3" :
            ItemPrice = PriceAespa
    elif Item =="4" :
            ItemPrice = PriceLe_sserafim
    elif Item =="5" :
            ItemPrice = PriceIdie
    else:
        print("Did't select item in the list")
        ItemPrice = 0
    if ID == "VIP" and ItemPrice !=0:
        TotalPrice = ItemPrice*Number - 0.05*(ItemPrice*Number)
        print("Total price :", TotalPrice,"$")
        print("Thank you for shopping with us")
    elif ID == "Normal" and ItemPrice !=0 :
        if Number !=0:
            TotalPrice = ItemPrice*Number+1.5
            print("Total price :", TotalPrice, "$")
            print("Thank you for shopping with us")
        else:
            TotalPrice = 0
            print("Total price :", TotalPrice, "$")
            print("Thank you for shopping with us")
    elif ItemPrice ==0 :
        print("Thank you")







