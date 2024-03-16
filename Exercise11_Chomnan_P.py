Number_Of_TreeLayers = int(input("Input the number of * symbol: "))
print((Number_Of_TreeLayers-1) * " " + "*")
for i in range(Number_Of_TreeLayers-1):
    print((Number_Of_TreeLayers-(i+2)) * " " + ((i+1)*2) * "*"+"*")