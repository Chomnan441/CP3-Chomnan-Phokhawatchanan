def vatCaculate(TotalPrice):
    Result = TotalPrice+TotalPrice*0.07
    return int(Result)
print(vatCaculate(int(input("Please input total price : "))))