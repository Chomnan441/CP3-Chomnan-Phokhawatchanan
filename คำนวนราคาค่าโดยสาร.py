distance = int(input())
if distance == 0:
    cost = 0
elif distance >0 and distance <=1:
    cost = 35
elif distance > 1 and distance <= 10:
    cost = 35+(distance-1)*5.5
elif distance > 10 and distance <= 20:
    cost = 35+(9*5.5)+(distance-10)*6.5
elif distance > 20 and distance <= 40:
    cost = 35+(9*5.5)+(10*6.5)+(distance-20)*7.5
elif distance > 40 and distance <= 60:
    cost = 35+35+(9*5.5)+(10*6.5)+(10*7.5)+(distance-40)*8
elif distance > 60 and distance <= 80:
    cost = 35+35+(9*5.5)+(10*6.5)+(10*7.5)+(10*8)+(distance-60)*9
elif distance > 80:
    cost = 35+35+(9*5.5)+(10*6.5)+(10*7.5)+(10*8)+(10*9)+(distance-80)*10.5
print(cost)